<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/brand/wordmark-dark.svg">
  <img alt="younghwan91" src="docs/images/brand/wordmark-light.svg" height="52">
</picture>

# younghwan91

**한국 주식 오픈소스 퀀트 인프라와 수치 최적화 시스템을 만듭니다.**

기계공학 박사(*수치 최적화*) · 낮에는 **두산로보틱스** ML · 인지 엔지니어로 일합니다.

**한국어** · [English](README.md) | [Homepage](https://younghwan91.github.io/) · [LinkedIn](https://www.linkedin.com/in/younghwan-chae/) · [Email](mailto:chyohw97@gmail.com) · [이력서 (PDF)](https://github.com/younghwan91/resume/releases/latest/download/resume_ko.pdf)

</div>

## 여기서 시작하세요

- [**kiwoom-client**](https://github.com/younghwan91/kiwoom-client) — 키움 REST API 를 파이썬과 AI 에이전트(MCP)로 씁니다. 윈도 OCX 없이 맥·리눅스에서도 돕니다. `pip install kiwoom-client`
- [**fin-checkup**](https://github.com/younghwan91/fin-checkup) — 상장사 재무제표를 신호등으로 읽어 줍니다. 지표 17개마다 계산식과 기준값이 붙습니다. [브라우저에서 바로 보기](https://younghwan91.github.io/fin-checkup/)
- [**kiwoom-order-guard**](https://github.com/younghwan91/kiwoom-order-guard) — AI 에이전트가 내는 키움 주문의 내용(금액·수량·시장가 매수·반복 전송)을 보내기 전에 검사하는 Claude Code 훅입니다.

## 한국 주식 라이브러리

| 저장소 | 설명 |
|--------|------|
| [**sector-flow**](https://github.com/younghwan91/sector-flow) | 오늘 어느 투자 주체가 어느 섹터를 넘기고 넘겨받았는지 한 장의 지도로 봅니다 |
| [**krx-news-client**](https://github.com/younghwan91/krx-news-client) | DART 공시와 토스증권 뉴스를 한 스키마로 받습니다 |
| [**krx-fundamentals-client**](https://github.com/younghwan91/krx-fundamentals-client) | DART·KRX·네이버의 기업 펀더멘털을 Pydantic 모델로 돌려줍니다 |
| [**krx-quant-core**](https://github.com/younghwan91/krx-quant-core) | 시장 규칙·비용·주문 가드·검증 통계를 한 군데서 맞추는 공통 코어입니다 |

## 그 밖의 저장소

- **데이터 파이프라인:** [quant-airflow](https://github.com/younghwan91/quant-airflow) — 상장폐지 종목까지 담는 Airflow + TimescaleDB 한국 주식 시세·재무 적재
- **리서치 (한국):** [swing-it](https://github.com/younghwan91/swing-it) · [daytrade-it](https://github.com/younghwan91/daytrade-it) · [scalp-it](https://github.com/younghwan91/scalp-it)
- **리서치 (미국 · 크립토):** [portfolio-research](https://github.com/younghwan91/portfolio-research) · [macro-sector-agent](https://github.com/younghwan91/macro-sector-agent) · [quantbox](https://github.com/younghwan91/quantbox) · [crypto-quant-insights](https://github.com/younghwan91/crypto-quant-insights)
- **공부 · 도구:** [automated-stock-trading-systems](https://github.com/younghwan91/automated-stock-trading-systems) · [resume](https://github.com/younghwan91/resume)

## 아키텍처 개요

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/architecture-ko-dark.svg">
    <img alt="아키텍처 개요: 한국·미국·크립토 데이터 소스가 적재·저장을 거쳐 리서치·전략 저장소로 흐릅니다" src="docs/images/architecture-ko-light.svg" width="638">
  </picture>
</p>


## 기술 스택

- **언어:** Python, C/C++, SQL, LaTeX
- **ML · 최적화:** PyTorch, 수치 최적화, 센서 퓨전, 4D 레이더 · 컴퓨터 비전
- **데이터 · 인프라:** PostgreSQL / TimescaleDB, DuckDB, Apache Airflow, Docker, Linux

## 라이선스

[CC BY-NC-ND 4.0](LICENSE) 라이선스를 따르며, 개인 오픈소스 퀀트 프로젝트는 본업과 무관합니다.
