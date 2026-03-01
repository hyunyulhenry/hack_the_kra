"""
data.go.kr 한국마사회 API 신규 등록/삭제 확인 스크립트

전체 API 목록을 저장해두고 diff 비교하여
구체적으로 어떤 API가 추가/삭제되었는지 확인.

cron 예시 (매월 1일 오전 9시):
  0 9 1 * * cd /path/to/hack_the_kra && python scripts/check_new_apis.py
"""

import re
import sys
import io
import json
import requests
from pathlib import Path
from datetime import datetime

# Windows cp949 인코딩 문제 방지 (cron 환경 포함)
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

SEARCH_URL = "https://www.data.go.kr/tcs/dss/selectDataSetList.do"
BASE_PARAMS = {
    "dType": "API",
    "keyword": "한국마사회",
    "perPage": 30,
}
STATE_FILE = Path(__file__).parent / ".api_state.json"


def parse_page(html: str) -> list[dict]:
    """HTML 페이지에서 API 항목(ID + 이름)을 파싱."""
    # 패턴: fn_preview('ID', 'API') ... <span class='sr-only'> 제목 </span> 미리보기
    items = re.findall(
        r"fn_preview\('(\d+)'.*?<span class=['\"]sr-only['\"]>\s*(.*?)\s*</span>\s*미리보기",
        html,
        re.DOTALL,
    )
    results = []
    for pk, raw_title in items:
        name = re.sub(r"<[^>]+>", "", raw_title).strip()
        if name:
            results.append({"id": pk, "name": name})
    return results


def fetch_api_list() -> list[dict]:
    """data.go.kr에서 한국마사회 API 전체 목록을 수집."""
    all_apis = []
    total = 0
    page = 1

    while True:
        params = {**BASE_PARAMS, "currentPage": page}
        resp = requests.get(SEARCH_URL, params=params, timeout=30)
        resp.raise_for_status()
        html = resp.text

        # 총 건수 파싱 (첫 페이지에서만)
        if page == 1:
            m = re.search(r"총\s*(\d+)\s*건", html)
            total = int(m.group(1)) if m else 0

        items = parse_page(html)
        if not items:
            break

        all_apis.extend(items)

        if total and len(all_apis) >= total:
            break
        page += 1
        if page > 30:
            break

    return all_apis


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"apis": [], "last_checked": "never"}


def save_state(apis: list[dict]):
    STATE_FILE.write_text(
        json.dumps(
            {"apis": apis, "last_checked": datetime.now().isoformat()},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def diff_apis(old: list[dict], new: list[dict]) -> tuple[list[dict], list[dict]]:
    """이전 목록과 비교하여 추가/삭제된 API 반환."""
    old_keys = {(a.get("id"), a["name"]) for a in old}
    new_keys = {(a.get("id"), a["name"]) for a in new}

    added = [{"id": k[0], "name": k[1]} for k in new_keys - old_keys]
    removed = [{"id": k[0], "name": k[1]} for k in old_keys - new_keys]

    return sorted(added, key=lambda x: x["name"]), sorted(removed, key=lambda x: x["name"])


def main():
    state = load_state()
    prev_apis = state["apis"]
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    try:
        current_apis = fetch_api_list()
    except Exception as e:
        print(f"[ERROR] {now} — API 목록 수집 실패: {e}")
        return

    if not prev_apis:
        print(f"[INIT] {now} — 최초 실행, {len(current_apis)}개 API 저장")
        save_state(current_apis)
        return

    added, removed = diff_apis(prev_apis, current_apis)

    if added or removed:
        print(f"[CHANGED] {now} — 한국마사회 API 변동 감지! ({len(prev_apis)} → {len(current_apis)}개)")
        if added:
            print(f"\n  ✚ 신규 등록 ({len(added)}개):")
            for api in added:
                url = f"https://www.data.go.kr/data/{api['id']}/openapi.do" if api["id"] else ""
                print(f"    - {api['name']}  {url}")
        if removed:
            print(f"\n  ✖ 삭제/변경 ({len(removed)}개):")
            for api in removed:
                print(f"    - {api['name']}")
    else:
        print(f"[OK] {now} — 변동 없음 ({len(current_apis)}개)")

    save_state(current_apis)


if __name__ == "__main__":
    main()
