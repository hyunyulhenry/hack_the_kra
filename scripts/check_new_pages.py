"""
race.kra.co.kr 신규 페이지/섹션 등록 확인 스크립트

totalMenu.do 의 전체 내부 링크 목록을 저장해두고 diff 비교하여
새로 추가되거나 삭제된 페이지를 감지.

cron 예시 (매월 1일 오전 9시):
  0 9 1 * * cd /path/to/hack_the_kra && python scripts/check_new_pages.py
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

MENU_URL = "https://race.kra.co.kr/totalMenu.do"
BASE_URL = "https://race.kra.co.kr"
STATE_FILE = Path(__file__).parent / ".pages_state.json"

# 감지 대상 외 노이즈 경로 (로그인, 외부링크, 정적 리소스 등)
EXCLUDE_PATTERNS = [
    r"^/SSOlogin",
    r"^/memb/",
    r"^/login",
    r"^http",        # 외부 링크
    r"javascript:",
    r"#",
    r"\.pdf$",
    r"\.xls",
    r"\.zip$",
]


def _is_excluded(href: str) -> bool:
    return any(re.search(pat, href) for pat in EXCLUDE_PATTERNS)


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Referer": "https://race.kra.co.kr/seoulMain.do",
}


def fetch_page_list() -> list[dict]:
    """totalMenu.do 에서 모든 내부 경로를 수집."""
    resp = requests.get(MENU_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    html = resp.text

    # href="..." 또는 href='...' 패턴 전체 추출
    raw_hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)

    seen = set()
    pages = []
    for href in raw_hrefs:
        href = href.strip()
        if not href or _is_excluded(href):
            continue
        # 경로만 추출 (쿼리스트링 제거해 정규화)
        path = href.split("?")[0].rstrip("/")
        if not path or path in seen:
            continue
        seen.add(path)
        pages.append({"path": path, "url": BASE_URL + path})

    return sorted(pages, key=lambda x: x["path"])


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"pages": [], "last_checked": "never"}


def save_state(pages: list[dict]):
    STATE_FILE.write_text(
        json.dumps(
            {"pages": pages, "last_checked": datetime.now().isoformat()},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def diff_pages(
    old: list[dict], new: list[dict]
) -> tuple[list[dict], list[dict]]:
    """이전 목록과 비교하여 추가/삭제된 경로 반환."""
    old_paths = {p["path"] for p in old}
    new_paths = {p["path"] for p in new}

    new_map = {p["path"]: p for p in new}

    added = [new_map[p] for p in sorted(new_paths - old_paths)]
    removed = [{"path": p, "url": BASE_URL + p} for p in sorted(old_paths - new_paths)]

    return added, removed


def main():
    state = load_state()
    prev_pages = state["pages"]
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    try:
        current_pages = fetch_page_list()
    except Exception as e:
        print(f"[ERROR] {now} — 페이지 목록 수집 실패: {e}")
        return

    if not prev_pages:
        print(f"[INIT] {now} — 최초 실행, {len(current_pages)}개 경로 저장")
        save_state(current_pages)
        return

    added, removed = diff_pages(prev_pages, current_pages)

    if added or removed:
        print(
            f"[CHANGED] {now} — race.kra.co.kr 페이지 변동 감지! "
            f"({len(prev_pages)} → {len(current_pages)}개)"
        )
        if added:
            print(f"\n  ✚ 신규 경로 ({len(added)}개):")
            for p in added:
                print(f"    - {p['path']}")
                print(f"      {p['url']}")
        if removed:
            print(f"\n  ✖ 삭제/변경 ({len(removed)}개):")
            for p in removed:
                print(f"    - {p['path']}")
    else:
        print(f"[OK] {now} — 변동 없음 ({len(current_pages)}개 경로)")

    save_state(current_pages)


if __name__ == "__main__":
    main()
