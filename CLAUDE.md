# CLAUDE.md — KRA 경마 예측 시스템 프로젝트

> Bill Benter 방법론 기반 한국마사회(KRA) 경마 예측 및 베팅 시스템
> 마지막 업데이트: 2026-03-01

---

## 프로젝트 목표

벤터의 1994년 논문 방법론을 KRA(한국마사회)에 적용해
**통계적 엣지를 가진 경마 예측 모델**을 구축하고
실제 베팅을 통해 수익성을 검증하는 것.

---

## 프로젝트 구조

```
hack_the_kra/
├── CLAUDE.md
├── .env                  # API 키 (git 제외)
├── requirements.txt
├── db/kra.duckdb         # 메인 DB (git 제외)
├── docs/
│   ├── KRA_API_목록.md   # Phase별 API 분류 (220개 중 53개)
│   └── 모델_전략.md      # 3-Stage 아키텍처, 피처 전략
├── rules/                # KRA 경마 규칙, 베팅 규칙
├── papers/               # 벤터 논문 및 관련 논문 PDF
├── scripts/
│   └── check_new_apis.py # API 신규 등록 모니터링 (cron용)
├── src/
│   ├── collect/          # API 수집 → DuckDB 적재
│   ├── features/         # 피처 엔지니어링
│   ├── model/            # Logit → LightGBM, Combined Model
│   └── betting/          # Kelly Criterion
└── notebooks/
```

---

## 데이터 소스

- **1순위**: `AI기반연구용_경주결과상세` API — 44개 필드 (장구/DQ/복연배당 포함)
  - ⚠️ 역사 데이터 깊이 미확인 → 승인 후 `race_dt=20220101` 테스트 필수
- **백업**: `AI학습용_경주결과` API — 27개 필드
- **API 수집 불가**: 경주 전 배당률 시계열, 부산/제주 당일 체중 → 스크래핑 필요

→ Phase별 전체 API 목록: [docs/KRA_API_목록.md](docs/KRA_API_목록.md)

---

## 벤터 방법론

### 핵심 모델: Combined Multinomial Logit
```
Logit(combined_i) = α × Logit(public_odds_i) + β₁X₁ + β₂X₂ + ... + βₙXₙ
P(horse i wins) = exp(logit_i) / Σ exp(logit_j)
```
- **공중 배당률을 변수로 통합**하는 것이 핵심 — 단독 펀더멘털 모델보다 압도적으로 우수
- **Δr²** = r²(combined) - r²(public odds alone) > 0 이면 수익 가능 (벤터 달성값: 0.0178)
- 모델 훈련 목표: 서울 3년치 3,600+ 경주

→ 3-Stage 아키텍처 및 피처 전략: [docs/모델_전략.md](docs/모델_전략.md)

---

## 참고 문서

| 파일 | 내용 |
|------|------|
| [rules/KRA_경마_기본규칙.md](rules/KRA_경마_기본규칙.md) | 등급 체계, 트랙, 부담중량, 착순 규정 |
| [rules/KRA_베팅_규칙.md](rules/KRA_베팅_규칙.md) | 승식, 환수율, 세금, 베팅 한도 |
| [papers/README.md](papers/README.md) | 벤터 논문 및 관련 논문 목록 |
| [docs/KRA_API_목록.md](docs/KRA_API_목록.md) | Phase 1/2/3 API 분류 및 신청 링크 |
| [docs/모델_전략.md](docs/모델_전략.md) | 3-Stage 아키텍처, 피처 전략, 개발 로드맵 |

---

## TODO

### 즉시
- [ ] data.go.kr Phase 1~3 API 전체 신청 → [docs/KRA_API_목록.md](docs/KRA_API_목록.md) 참조
- [ ] 역사 데이터 깊이 테스트: `race_dt=20220101`

### 데이터 수집
- [ ] 서울 3년치 (2022~2024) 수집
- [ ] DuckDB 스키마 설계 및 구축

### 모델 개발
- [ ] 기초 피처 엔지니어링
- [ ] Multinomial Logit 베이스라인 (v1 — 벤터 재현)
- [ ] LightGBM + 공중 배당률 통합 (v2)
- [ ] KRA용 Harville 파라미터 재추정
- [ ] Holdout 검증 + Δr² 측정
- [ ] Optuna 하이퍼파라미터 튜닝

### 실전 운용
- [ ] Kelly Criterion 베팅 사이즈 계산기
- [ ] 실시간 배당률 스크래퍼 (race.kra.co.kr)
- [ ] 더비온 앱 연동 검토

### 정기 점검 (3개월마다)
- [ ] data.go.kr 한국마사회 API 신규 등록 확인 (현재 220개, 2026-03-01 기준)
- [ ] 기존 API 변경/폐지 여부 확인
