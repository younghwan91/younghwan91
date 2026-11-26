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

## Start Here

- [**kiwoom-client**](https://github.com/younghwan91/kiwoom-client) — Kiwoom Securities REST API for Python and AI agents (MCP), no Windows OCX, runs on macOS and Linux. `pip install kiwoom-client`
- [**fin-checkup**](https://github.com/younghwan91/fin-checkup) — Traffic-light check-up of a Korean listed company's financial statements: 17 metrics, each with its formula and thresholds. [Try it in the browser](https://younghwan91.github.io/fin-checkup/)
- [**kiwoom-order-guard**](https://github.com/younghwan91/kiwoom-order-guard) — Claude Code hook that checks what an AI agent's Kiwoom order actually says (amount, quantity, market buys, repeats) before it is sent.

## Korean Market Libraries

| Repository | Description |
|------------|-------------|
| [**sector-flow**](https://github.com/younghwan91/sector-flow) | One map of which investor groups sold and bought which sectors today |
| [**krx-news-client**](https://github.com/younghwan91/krx-news-client) | DART filings and Toss Securities news in one schema |
| [**krx-fundamentals-client**](https://github.com/younghwan91/krx-fundamentals-client) | Company fundamentals from DART, KRX and Naver as Pydantic models |
| [**krx-quant-core**](https://github.com/younghwan91/krx-quant-core) | Shared core for KRX market rules, costs, order guards and validation statistics |

## Everything Else

- **Data pipeline:** [quant-airflow](https://github.com/younghwan91/quant-airflow) — Airflow + TimescaleDB for Korean equity prices and fundamentals, delisted names included
- **Research (Korea):** [swing-it](https://github.com/younghwan91/swing-it) · [daytrade-it](https://github.com/younghwan91/daytrade-it) · [scalp-it](https://github.com/younghwan91/scalp-it)
- **Research (US &amp; crypto):** [portfolio-research](https://github.com/younghwan91/portfolio-research) · [macro-sector-agent](https://github.com/younghwan91/macro-sector-agent) · [quantbox](https://github.com/younghwan91/quantbox) · [crypto-quant-insights](https://github.com/younghwan91/crypto-quant-insights)
- **Study &amp; tools:** [automated-stock-trading-systems](https://github.com/younghwan91/automated-stock-trading-systems) · [resume](https://github.com/younghwan91/resume)

## Architecture Overview

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/architecture-en-dark.svg">
    <img alt="Architecture overview: KRX, US and crypto data sources flow through ingest and storage into research and strategy repositories" src="docs/images/architecture-en-light.svg" width="638">
  </picture>
</p>


## Tech Stack

- **Languages:** Python, C/C++, SQL, LaTeX
- **ML &amp; Optimization:** PyTorch, numerical optimization, sensor fusion, 4D radar &amp; computer vision
- **Data &amp; Infra:** PostgreSQL / TimescaleDB, DuckDB, Apache Airflow, Docker, Linux

## License

[CC BY-NC-ND 4.0](LICENSE) · Independent open-source quant work is unrelated to my day job.
