<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/brand/banner-dark.svg">
  <img alt="Younghwan Chae, Ph.D." src="docs/images/brand/banner-light.svg" width="100%">
</picture>

<p align="center">
  <b>한국 주식 오픈소스 퀀트 인프라와 수치 최적화 시스템을 만듭니다.</b><br/>
  기계공학 박사(<i>수치 최적화</i>) · 낮에는 <b>두산로보틱스</b> ML · 인지 엔지니어로 일합니다.
</p>

<p align="center">
  <b>한국어</b> · <a href="README.md">English</a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://younghwan91.github.io/">Homepage</a> ·
  <a href="https://www.linkedin.com/in/younghwan-chae/">LinkedIn</a> ·
  <a href="mailto:chyohw97@gmail.com">Email</a> ·
  <a href="https://github.com/younghwan91/resume/releases/latest/download/resume_ko.pdf">이력서 (PDF)</a>
</p>

---

### 아키텍처 개요

```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "nodeSpacing": 8, "rankSpacing": 16, "padding": 4}, "themeVariables": {"fontSize": "10px"}}}%%
flowchart LR
    K1["🇰🇷 키움 · 뉴스 · 재무 클라이언트"] --> K2[("quant-airflow<br/>TimescaleDB")] --> K3["swing-it · sector-flow<br/>daytrade-it · scalp-it"]
    KC["krx-quant-core"] --> K3
    U1["🇺🇸 Sharadar"] --> U2[("DuckDB")] --> U3["portfolio-research<br/>macro-sector-agent"]
    C1["🪙 거래소 API"] --> C2["quantbox"] --> C3["crypto-quant-insights"]

    classDef src  fill:#2563EB,stroke:#1E40AF,color:#FFFFFF
    classDef pipe fill:#7C3AED,stroke:#5B21B6,color:#FFFFFF
    classDef db   fill:#D97706,stroke:#92400E,color:#FFFFFF
    classDef core fill:#0D9488,stroke:#115E59,color:#FFFFFF
    classDef res  fill:#059669,stroke:#065F46,color:#FFFFFF
    classDef eng  fill:#EA580C,stroke:#9A3412,color:#FFFFFF
    class K1,U1,C1 src
    class K2 pipe
    class U2 db
    class KC core
    class K3,U3,C3 res
    class C2 eng
```

### 주요 오픈소스 프로젝트

| 저장소 | 분야 | 설명 |
|--------|------|------|
| [**fin-checkup**](https://github.com/younghwan91/fin-checkup) | 개인 재무 | 재무 건전성 점검 및 포트폴리오 진단 CLI/도구 |
| [**kiwoom-client**](https://github.com/younghwan91/kiwoom-client) | 한국 주식 | 키움증권 REST/WebSocket 시세 · 주문 API 파이썬 클라이언트 |
| [**sector-flow**](https://github.com/younghwan91/sector-flow) | 한국 주식 | KRX 섹터 순환 및 기관 · 외국인 수급 흐름 분석 |
| [**krx-quant-core**](https://github.com/younghwan91/krx-quant-core) | 한국 주식 | KRX 데이터 · 시그널 · 백테스트 공통 퀀트 코어 라이브러리 |
| [**quant-airflow**](https://github.com/younghwan91/quant-airflow) | 데이터 파이프라인 | Airflow + TimescaleDB 기반 한국 주식 시세 · 재무 데이터 적재 |
| [**swing-it**](https://github.com/younghwan91/swing-it) | 알파 검증 | 랜덤 널 대조군 · Purged CV · Deflated Sharpe 기반 KOSPI/KOSDAQ 알파 검증 |
| [**portfolio-research**](https://github.com/younghwan91/portfolio-research) | 미국 주식 | 워크포워드 검증(Deflated Sharpe, PBO) 기반 미국 주식 팩터 · 자산배분 엔진 |

<details>
<summary>전체 생태계 (클라이언트 · 리서치 · 도구)</summary>

- **한국:** [krx-news-client](https://github.com/younghwan91/krx-news-client) · [krx-fundamentals-client](https://github.com/younghwan91/krx-fundamentals-client) · [daytrade-it](https://github.com/younghwan91/daytrade-it) · [scalp-it](https://github.com/younghwan91/scalp-it) · [kiwoom-order-guard](https://github.com/younghwan91/kiwoom-order-guard)
- **미국 · 크립토:** [macro-sector-agent](https://github.com/younghwan91/macro-sector-agent) · [quantbox](https://github.com/younghwan91/quantbox) · [crypto-quant-insights](https://github.com/younghwan91/crypto-quant-insights)
- **리서치 · 도구:** [automated-stock-trading-systems](https://github.com/younghwan91/automated-stock-trading-systems) · [resume](https://github.com/younghwan91/resume)

</details>

### 기술 스택

- **언어:** Python, C/C++, SQL, LaTeX
- **ML · 최적화:** PyTorch, 수치 최적화, 센서 퓨전, 4D 레이더 · 컴퓨터 비전
- **데이터 · 인프라:** PostgreSQL / TimescaleDB, DuckDB, Apache Airflow, Docker, Linux

---

<p align="center">
  <sub><a href="LICENSE">CC BY-NC-ND 4.0</a> 라이선스 · 개인 오픈소스 퀀트 프로젝트는 본업과 무관합니다.</sub>
</p>
