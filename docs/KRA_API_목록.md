# KRA 공공데이터포털 API — 예측 모델용 분류
> 총 220개 중 예측에 관련된 API만 분류. 마지막 업데이트: 2026-03-01

---

## Phase 1 — 역사 데이터 수집 (즉시 신청)

| # | API 이름 | 용도 | 우선순위 | 링크 |
|---|---------|------|---------|------|
| 1 | AI기반연구용_경주결과상세 | 44개 필드, 장구/DQ/복연배당 | ⭐⭐⭐⭐⭐ | [15150068](https://www.data.go.kr/data/15150068/openapi.do) |
| 2 | AI학습용_경주결과 | 27개 필드, 백업용 | ⭐⭐⭐⭐ | [15143803](https://www.data.go.kr/data/15143803/openapi.do) |
| 3 | AI학습용_경주계획 | 경주 조건, 레이팅, 상금 | ⭐⭐⭐⭐⭐ | [15143802](https://www.data.go.kr/data/15143802/openapi.do) |
| 4 | 확정배당율 통합 정보 | 전 승식 확정배당 | ⭐⭐⭐⭐⭐ | [15058559](https://www.data.go.kr/data/15058559/openapi.do) |
| 5 | 경마 매출액 및 확정배당율 | 풀 규모, 매출 | ⭐⭐⭐⭐ | [15057896](https://www.data.go.kr/data/15057896/openapi.do) |
| 6 | 경주마 레이팅 정보 | 등급 1~6 레이팅 | ⭐⭐⭐⭐⭐ | [15057323](https://www.data.go.kr/data/15057323/openapi.do) |
| 7 | 기수최근1년성적비교 | 기수 능력 평가 | ⭐⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EA%B8%B0%EC%88%98%EC%B5%9C%EA%B7%BC1%EB%85%84) |
| 8 | 조교사 상세정보 | 조교사 기본 정보 | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%A1%B0%EA%B5%90%EC%82%AC+%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4) |
| 9 | 경주기록 정보 | 경주별 기본 정보 | ⭐⭐⭐⭐ | [15058305](https://www.data.go.kr/data/15058305/openapi.do) |
| 10 | 경주성적정보 | 경주 성적 상세 | ⭐⭐⭐⭐ | [15063979](https://www.data.go.kr/data/15063979/openapi.do) |
| 11 | 경주마 성적 정보 | 마필별 성적 | ⭐⭐⭐⭐ | [15058779](https://www.data.go.kr/data/15058779/openapi.do) |
| 12 | 경주별상세성적표 | 상세 성적표 | ⭐⭐⭐⭐ | [15089492](https://www.data.go.kr/data/15089492/openapi.do) |
| 13 | 경마경주정보 | 경주 조건 상세 | ⭐⭐⭐ | [15063951](https://www.data.go.kr/data/15063951/openapi.do) |
| 14 | RC경마경주정보 | 부담중량, 체중 등 | ⭐⭐⭐⭐ | [15063950](https://www.data.go.kr/data/15063950/openapi.do) |

---

## Phase 2 — 모델 검증 후 (경주 당일 실시간)

| # | API 이름 | 용도 | 우선순위 | 링크 |
|---|---------|------|---------|------|
| 15 | 출전마 체중 정보 | 당일 체중 + 변화 (서울) | ⭐⭐⭐⭐ | [3075629](https://www.data.go.kr/dataset/3075629/openapi.do) |
| 16 | 홈페이지_서울출전마체중 | 서울 체중 | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%84%9C%EC%9A%B8%EC%B6%9C%EC%A0%84%EB%A7%88%EC%B2%B4%EC%A4%91) |
| 17 | 홈페이지_부산경남출전마체중 | 부산 체중 | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EB%B6%80%EC%82%B0%EA%B2%BD%EB%82%A8%EC%B6%9C%EC%A0%84%EB%A7%88%EC%B2%B4%EC%A4%91) |
| 18 | 홈페이지_제주출전마체중 | 제주 체중 | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%A0%9C%EC%A3%BC%EC%B6%9C%EC%A0%84%EB%A7%88%EC%B2%B4%EC%A4%91) |
| 19 | 기수변경 정보 | 기수 변경 (강한 시그널) | ⭐⭐⭐⭐⭐ | [15057181](https://www.data.go.kr/data/15057181/openapi.do) |
| 20 | 홈페이지_서울기수변경말취소 | 서울 기수변경/말취소 | ⭐⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%84%9C%EC%9A%B8%EA%B8%B0%EC%88%98%EB%B3%80%EA%B2%BD) |
| 21 | 홈페이지_부산경남기수변경말취소 | 부산 기수변경/말취소 | ⭐⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EB%B6%80%EC%82%B0%EA%B2%BD%EB%82%A8%EA%B8%B0%EC%88%98%EB%B3%80%EA%B2%BD) |
| 22 | 홈페이지_제주기수변경말취소 | 제주 기수변경/말취소 | ⭐⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%A0%9C%EC%A3%BC%EA%B8%B0%EC%88%98%EB%B3%80%EA%B2%BD) |
| 23 | 출전표 상세정보 | 출전마 상세 | ⭐⭐⭐⭐ | [15058677](https://www.data.go.kr/data/15058677/openapi.do) |
| 24 | 제재내역 | 출전 자격 필터 | ⭐⭐⭐ | [15037098](https://www.data.go.kr/data/15037098/openapi.do) |
| 25 | 출발심사 결과 (서울) | 출발 관련 | ⭐⭐⭐ | [15140260](https://www.data.go.kr/data/15140260/openapi.do) |
| 26 | 경마시행당일_경주결과종합 | 당일 결과 실시간 | ⭐⭐⭐⭐ | [15119524](https://www.data.go.kr/data/15119524/openapi.do) |
| 27 | 경마시행당일_확정배당율종합 | 당일 확정 배당 | ⭐⭐⭐⭐⭐ | [15119558](https://www.data.go.kr/data/15119558/openapi.do) |
| 28 | 경마시행당일_기수변경상세 | 당일 기수변경 상세 | ⭐⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EA%B8%B0%EC%88%98%EB%B3%80%EA%B2%BD%EC%83%81%EC%84%B8) |

---

## Phase 3 — 수익성 확인 후 (피처 엔지니어링 심화)

| # | API 이름 | 용도 | 우선순위 | 링크 |
|---|---------|------|---------|------|
| 29 | 마필 구간별 경주기록 | 페이스 분석 (선행/추입) | ⭐⭐⭐⭐⭐ | [15057859](https://www.data.go.kr/data/15057859/openapi.do) |
| 30 | 경마코너별통과순위_주로빠르기 | 코너별 통과 순위 | ⭐⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%BD%94%EB%84%88%EB%B3%84%ED%86%B5%EA%B3%BC) |
| 31 | 조교사일일조교일자 | 조교 빈도 대리 지표 | ⭐⭐⭐ | [15089712](https://www.data.go.kr/data/15089712/openapi.do) |
| 32 | 조교사월별조교강도 | 조교 강도 | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%A1%B0%EA%B5%90%EC%82%AC%EC%9B%94%EB%B3%84%EC%A1%B0%EA%B5%90%EA%B0%95%EB%8F%84) |
| 33 | 조교사월별조교시간 | 조교 시간 | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%A1%B0%EA%B5%90%EC%82%AC%EC%9B%94%EB%B3%84%EC%A1%B0%EA%B5%90%EC%8B%9C%EA%B0%84) |
| 34 | 기수 성적 정보 | 6개월 슬라이딩 윈도우 | ⭐⭐⭐⭐ | [15056591](https://www.data.go.kr/data/15056591/openapi.do) |
| 35 | 기수기간별성적비교 | 기수 성적 추이 | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EA%B8%B0%EC%88%98%EA%B8%B0%EA%B0%84%EB%B3%84) |
| 36 | 기수통산성적비교 | 기수 통산 성적 | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EA%B8%B0%EC%88%98%ED%86%B5%EC%82%B0%EC%84%B1%EC%A0%81) |
| 37 | 혈통정보기본 | 거리 적성 추정 | ⭐⭐⭐ | [15109000](https://www.data.go.kr/data/15109000/openapi.do) |
| 38 | 해외경주성적정보 | 수입마 과거 성적 | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%ED%95%B4%EC%99%B8%EA%B2%BD%EC%A3%BC%EC%84%B1%EC%A0%81) |
| 39 | 경주마 상세정보 | 마필 기본 정보 | ⭐⭐⭐ | [15058115](https://www.data.go.kr/data/15058115/openapi.do) |
| 40 | 마필종합 상세정보 | 마필 종합 정보 | ⭐⭐⭐ | [15057985](https://www.data.go.kr/data/15057985/openapi.do) |
| 41 | 일별훈련 상세정보 | 훈련 내역 | ⭐⭐⭐ | [15058782](https://www.data.go.kr/data/15058782/openapi.do) |
| 42 | 경주마 등급변동내역 | 등급 승강급 이력 | ⭐⭐⭐⭐ | [15058076](https://www.data.go.kr/data/15058076/openapi.do) |
| 43 | 경주마 수영조교정보 | 수영 훈련 (컨디션) | ⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%88%98%EC%98%81%EC%A1%B0%EA%B5%90) |
| 44 | 마필,기수,조교사 통산경주기록 | 통산 기록 | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%ED%86%B5%EC%82%B0%EA%B2%BD%EC%A3%BC%EA%B8%B0%EB%A1%9D) |
| 45 | 경주마인기투표정보 | 대중 인기도 (배당 대리) | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%9D%B8%EA%B8%B0%ED%88%AC%ED%91%9C) |
| 46 | 승식별 최고배당률 정보 | 이상 배당 탐지 | ⭐⭐ | [15059267](https://www.data.go.kr/data/15059267/openapi.do) |
| 47 | 경주마_일자별_통산전적 | 시계열 전적 | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%9D%BC%EC%9E%90%EB%B3%84+%ED%86%B5%EC%82%B0%EC%A0%84%EC%A0%81) |
| 48 | 경주마 경주전 1년간 진료내역 | 부상/컨디션 | ⭐⭐⭐ | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%A7%84%EB%A3%8C%EB%82%B4%EC%97%AD) |

---

## 보조/메타 정보

| # | API 이름 | 용도 | 링크 |
|---|---------|------|------|
| 49 | 경주로정보 | 트랙 메타데이터 | [15063953](https://www.data.go.kr/data/15063953/openapi.do) |
| 50 | 레츠런파크 트랙정보 | 트랙 상세 | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%ED%8A%B8%EB%9E%99%EC%A0%95%EB%B3%B4) |
| 51 | 출전표용어 | 필드 코드 해석 | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%B6%9C%EC%A0%84%ED%91%9C%EC%9A%A9%EC%96%B4) |
| 52 | 발매금액정보 | 매출 규모 | [15063972](https://www.data.go.kr/data/15063972/openapi.do) |
| 53 | 심판리포트정보 | DQ/진로방해 상세 | [data.go.kr 검색](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=%EC%8B%AC%ED%8C%90%EB%A6%AC%ED%8F%AC%ED%8A%B8) |

---

## 예측과 무관한 API (제외)

승마체험, 문화센터, 주차장, 온실가스, 학생승마, 경매, 포입씨암말, 말품평, 승마장,
전자입찰, 좌석정보, 마이크로칩, CCC문화강의, 교육마, 세계경주일정, 마주정보(영문),
말소재변경이력, 농정빅데이터 등 약 170개 API → 예측 모델에 불필요
