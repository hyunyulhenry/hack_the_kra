# KRA 사이트 스크래핑 목록 (race.kra.co.kr)
> 전수조사 기준: 2026-03-02
> API(data.go.kr)로 수집 불가한 데이터 위주로 정리

---

## 스크래핑 우선순위

### Priority 1 — API 미제공, 예측 모델 핵심

| # | URL | 데이터 내용 | 주요 컬럼/필드 | 파라미터 |
|---|-----|------------|--------------|---------|
| 1 | `/chulmainfo/trackView.do` | **트랙 상태** | 흙질상태, 습도율(%), 트랙길이(1800m), 직선거리(450m), 높이차 | `meet=1/2/3` |
| 2 | `/raceFastreport/ChuljumaWeightWeight.do` | **당일 마체중** | 경주번호, 말이름, 체중, 전회체중, 증감 | `meet=1/2/3` |
| 3 | `/raceFastreport/ChulmapyoChange.do` | **기수변경 상세** | 말이름, hrNo, jkNo, 기존기수→교체기수, 교체사유, 등록시간 | `meet=1/2/3` |
| 4 | `/racehorse/accessoryState.do` | **말 부상/질병 기록** | 등록일, 말이름, 기수, 마주, 질병명(복합성장애/파행/골절 등) | `meet=1` |
| 5 | `/referee/DecisionItem.do` | **징계/제재 내역** | 날짜, 경주, 이름, 처방사항, 처방기간, 처방기관 | `meet=1/2/3` |

> ⚠️ 트랙 상태(흙질/습도)는 API에 전혀 없음. 날씨 피처의 핵심.

---

### Priority 2 — API 보완 또는 조교 관련

| # | URL | 데이터 내용 | 주요 컬럼/필드 | 특이사항 |
|---|-----|------------|--------------|---------|
| 6 | `/trainer/monthlyTrainTough.do` | **월별 조교 강도** | 기수명, 훈련강도(회/마리), 전체평균 | Excel 다운로드 가능 |
| 7 | `/trainer/monthlyTrainRatio.do` | **마사별 출주율** | 마사명, 부마출주율(%), 두수, 지난달/평년 비교 | Excel 다운로드 가능 |
| 8 | `/trainer/monthlyTrainTerm.do` | **월별 훈련 시간** | 순위, 평균 훈련시간, 최고/최저 | `meet=1/2/3`, 월별 필터 |
| 9 | `/trainer/dailyDayTrainList.do` | **일일 조교 두수** | 날짜, 두수, 조교마수 | 집계 데이터 |
| 10 | `/referee/StartingRacingTrainCheckList.do` | **출발심사 합격률** | 마명, 날짜, 심사기관, 심사마수, 합격마수, 합격율 | |
| 11 | `/racehorse/byeondongPeriodSearch.do` | **마필 입/퇴장 변동** | SearchSelect 1~7 (입장마/퇴장마/공개도마 등), 날짜범위 최대 365일 | `fromDate`, `toDate` |

---

### Priority 3 — 성적 검색 (API보다 조건 풍부)

| # | URL | 데이터 내용 | 주요 컬럼/필드 |
|---|-----|------------|--------------|
| 12 | `/raceScore/ConditionScoreSearch.do` | **조건별 성적 검색** | 날짜범위(1993~), 거리(1000~2300m), 등급(C0~C9/1~6급), 날씨, 트랙상태, 부담중량(47~65kg), 기수수 — POST to `/jockey/ScoreRankMostChuljuList.do` |
| 13 | `/raceScore/ConditionMaxAvgRecordSearch.do` | **거리별 최고/평균/최저 기록** | 거리, 출주수, 우승수, 최고기록, 평균기록, 최저기록 |
| 14 | `/raceScore/RecordDistanceDistanceTopRecord.do` | **거리별 역대 최고기록** | 거리, 기록, 말이름, 기록일, 경주등급, 나이, 기수, 조교사 |
| 15 | `/thisweekrace/ThisWeekScoretableDailyScoretable.do` | **이번주 확정 배당** | 단승, 연승, 쌍승, 삼중복승 실수치 | `meet=0~3` |

---

## 공통 URL 파라미터

```
meet=1   서울경마
meet=2   제주경마
meet=3   부산경마
meet=0   전체 (일부 페이지만 지원)

rcDate=YYYYMMDD   경주 날짜
rcNo=N            경주 번호 (1~11)
pageIndex=N       페이지 번호
```

---

## API와 중복 (스크래핑 불필요)

| URL | 대응 API |
|-----|---------|
| `/raceScore/ScoretableScoreList.do` | AI기반연구용_경주결과상세 |
| `/jockey/RankScoreYearCompare.do` | 기수 성적 정보 |
| `/trainer/profileTrainerList.do` | 조교사 상세정보 |
| `/racehorse/ProfileHorsenameKinds.do` | 경주마 상세정보 |
| `/chulmainfo/ChulmaDetailInfoList.do` | 출전표 상세정보 |

---

## 실시간 배당률 (race.kra.co.kr에 없음)

race.kra.co.kr 전체를 탐색한 결과, **경주 중 실시간 토트 배당률은 이 사이트 어디에도 없음** (확인 완료).
현장 단말 또는 더비온 앱 수준에서만 제공. 별도 스크래핑 방안 필요.

---

## 모니터링

신규 페이지/섹션 추가 여부는 `scripts/check_new_pages.py` 로 주기적 확인.
totalMenu.do의 전체 내부 링크 목록을 저장해두고 diff 비교.
