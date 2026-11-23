<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/brand/wordmark-dark.svg">
  <img alt="younghwan91" src="docs/images/brand/wordmark-light.svg" height="52">
</picture>

# younghwan91

**Open-source quant infrastructure &amp; numerical optimization systems.**

Ph.D. in Mechanical Engineering (*mathematical optimization*) · ML &amp; perception engineer **@ Doosan Robotics** by day.

[한국어](README.ko.md) · **English** | [Homepage](https://younghwan91.github.io/) · [LinkedIn](https://www.linkedin.com/in/younghwan-chae/) · [Email](mailto:chyohw97@gmail.com) · [Résumé (PDF)](https://github.com/younghwan91/resume/releases/latest/download/resume_en.pdf)

</div>

## Architecture Overview

```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "nodeSpacing": 8, "rankSpacing": 16, "padding": 4}, "themeVariables": {"fontSize": "10px"}}}%%
flowchart LR
    K1["🇰🇷 kiwoom · news · fundamentals clients"] --> K2[("quant-airflow<br/>TimescaleDB")] --> K3["swing-it · sector-flow<br/>daytrade-it · scalp-it"]
    KC["krx-quant-core"] --> K3
    U1["🇺🇸 Sharadar"] --> U2[("DuckDB")] --> U3["portfolio-research<br/>macro-sector-agent"]
    C1["🪙 Exchange APIs"] --> C2["quantbox"] --> C3["crypto-quant-insights"]

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

## Featured Open Source Work

| Repository | Domain | Description |
|------------|--------|-------------|
| [**fin-checkup**](https://github.com/younghwan91/fin-checkup) | Personal Finance | Financial checkup &amp; portfolio diagnostics CLI/toolkit |
| [**kiwoom-client**](https://github.com/younghwan91/kiwoom-client) | Korean Equities | Python client for Kiwoom Securities REST/WebSocket market &amp; order APIs |
| [**sector-flow**](https://github.com/younghwan91/sector-flow) | Korean Equities | Sector rotation &amp; institutional flow analysis across KRX markets |
| [**krx-quant-core**](https://github.com/younghwan91/krx-quant-core) | Korean Equities | Shared quantitative core library for KRX data, signals, and backtesting |
| [**quant-airflow**](https://github.com/younghwan91/quant-airflow) | Data Pipeline | Airflow + TimescaleDB orchestration for Korean equity market &amp; fundamental data |
| [**swing-it**](https://github.com/younghwan91/swing-it) | Alpha Validation | KOSPI/KOSDAQ alpha validation with random null controls, purged CV &amp; Deflated Sharpe |
| [**portfolio-research**](https://github.com/younghwan91/portfolio-research) | US Equities | US equity factor engine &amp; tactical asset allocation gated by walk-forward validation |

<details>
<summary>Full ecosystem (clients, research &amp; tooling)</summary>

- **Korea:** [krx-news-client](https://github.com/younghwan91/krx-news-client) · [krx-fundamentals-client](https://github.com/younghwan91/krx-fundamentals-client) · [daytrade-it](https://github.com/younghwan91/daytrade-it) · [scalp-it](https://github.com/younghwan91/scalp-it) · [kiwoom-order-guard](https://github.com/younghwan91/kiwoom-order-guard)
- **US &amp; Crypto:** [macro-sector-agent](https://github.com/younghwan91/macro-sector-agent) · [quantbox](https://github.com/younghwan91/quantbox) · [crypto-quant-insights](https://github.com/younghwan91/crypto-quant-insights)
- **Research &amp; Tools:** [automated-stock-trading-systems](https://github.com/younghwan91/automated-stock-trading-systems) · [resume](https://github.com/younghwan91/resume)

</details>

## Tech Stack

- **Languages:** Python, C/C++, SQL, LaTeX
- **ML &amp; Optimization:** PyTorch, numerical optimization, sensor fusion, 4D radar &amp; computer vision
- **Data &amp; Infra:** PostgreSQL / TimescaleDB, DuckDB, Apache Airflow, Docker, Linux

## License

[CC BY-NC-ND 4.0](LICENSE) · Independent open-source quant work is unrelated to my day job.
