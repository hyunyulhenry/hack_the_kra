# 관련 논문 목록
> 마지막 업데이트: 2026-03-01

---

## 핵심 논문 (필독)

### 1. Benter (1994) ✅
**A Computer Based Horse Race Handicapping and Wagering System: A Report**
- 저자: William Benter
- 출처: *Efficiency of Racetrack Betting Markets* (Hausch, Lo, Ziemba 편저), Academic Press
- 핵심 내용: Combined Multinomial Logit 모델, 공중 배당률 통합, Δr² 지표
- 파일: `benter_1994.pdf`
- 출처: gwern.net

---

## 방법론 관련 논문

### 2. Kelly (1956) ✅
**A New Interpretation of Information Rate**
- 저자: John L. Kelly Jr.
- 출처: *Bell System Technical Journal*, 35(4), pp.917-926
- 핵심 내용: Kelly Criterion 원문
- 파일: `kelly_1956.pdf`
- 출처: Princeton University

### 3. Harville (1973) ⚠️ 수동 다운로드 필요
**Assigning Probabilities to the Outcomes of Multi-Entry Competitions**
- 저자: David A. Harville
- 출처: *Journal of the American Statistical Association*, 68(342), pp.312-316
- 핵심 내용: Harville Formula — 단승 확률 → 복승/삼복승 확률 변환
- ⚠️ KRA 데이터로 보정 파라미터 재추정 필수 (홍콩 파라미터 사용 불가)
- 파일: `harville_1973.pdf` ← 미다운로드
- 링크: https://www.tandfonline.com/doi/abs/10.1080/01621459.1973.10482425

### 4. Hausch, Ziemba & Rubinstein (1981) ⚠️ 수동 다운로드 필요
**Efficiency of the Market for Racetrack Betting**
- 저자: Donald Hausch, William Ziemba, Mark Rubinstein
- 출처: *Management Science*, 27(12), pp.1435-1452
- 핵심 내용: 경마 시장 비효율성 실증, 복승식 시장 엣지 존재 확인
- 파일: `hausch_ziemba_rubinstein_1981.pdf` ← 미다운로드
- 링크: https://pubsonline.informs.org/doi/10.1287/mnsc.27.12.1435

---

## 추가 참고 논문 (선택)

| 저자 | 연도 | 제목 | 핵심 |
|------|------|------|------|
| Lo & Bacon-Shone | 1994 | Approximating the Ordering Probabilities of Multi-Entry Competitions | Harville 편향 보정 |
| Sung & Johnson | 2010 | A Quantitative Analysis of Market Efficiency in Hong Kong Horse Race Betting | HK 시장 효율성 |
| Ziemba & Hausch | 1987 | *Dr. Z's Beat the Racetrack* (서적) | 실전 베팅 전략 |
| Colle (Alezan AI) | 2022 | What AI can do for horse-racing? (arXiv:2207.04981) | CV+SL+GT 융합 로드맵. 배당률이 단일 최강 피처임을 재확인. 기수-말 궁합 점수화 아이디어 |
| Nguyen | 2024 | Optimizing Horse Racing Predictions through Ensemble Learning | LightGBM+XGBoost+CatBoost 스태킹, XGBoost 메타모델 → v3 아키텍처에 반영 |
| Gupta & Singh | 2023 | Horse Race Results Prediction Using ML with Feature Selection (IJISAE) | SHAP 기반 명시적 피처 선택 단계 → 파이프라인에 반영 |