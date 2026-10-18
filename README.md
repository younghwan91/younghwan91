<h1 align="center">Younghwan Chae, Ph.D. · 채영환</h1>

<p align="center">
  <b>PhD in Mechanical Engineering</b> &nbsp;—&nbsp; <b><i>Mathematical Optimization</i></b> &nbsp;·&nbsp; ML &amp; Perception Engineer <b>@ Doosan Robotics</b><br/>
  <b>Mathematical optimization is the through-line</b> — numerical optimization, surrogate modeling &amp; state estimation, carried from theory into 3D perception, sensor fusion, and production systems. The quant repos below run on the same discipline: strategy search is an optimization problem, and every trial is paid for.
</p>

<p align="center"><a href="README.ko.md">한국어</a> · <b>English</b></p>
<p align="center">
  <a href="https://www.linkedin.com/in/younghwan-chae/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:chyohw97@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/></a>
  <a href="https://github.com/younghwan91/resume/releases/latest/download/resume_en.pdf"><img src="https://img.shields.io/badge/Résumé-B7472A?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Résumé (PDF)"/></a>
</p>

---

<h3><img src="https://img.shields.io/badge/%F0%9F%94%AD%20OPEN--SOURCE-059669?style=for-the-badge&labelColor=1E293B" height="26" alt="Open-source"/></h3>

Three stacks, one shape — **collect → store → research**. Korean equities get the most of it: client libraries feed one Airflow pipeline into TimescaleDB, a shared core fixes the market rules, and the research and trading repos read from there. The search itself is treated as optimization with a bill attached: grid sweeps, Optuna TPE and a CMA-ES evolutionary engine write every config to a run ledger, Deflated Sharpe and PBO charge for the number of trials, and the out-of-sample window opens once.

```mermaid
%%{init: {"flowchart": {"useMaxWidth": false, "nodeSpacing": 20, "rankSpacing": 25}, "themeVariables": {"fontSize": "12px"}}}%%
flowchart TB
    subgraph KR ["🇰🇷 Korean equities"]
        direction LR
        SRC["kiwoom-client<br/>krx-news-client<br/>krx-fundamentals-client"] --> AF["quant-airflow"] --> DB[("TimescaleDB<br/>delisted included")]
        DB --> SW["swing-it"]
        DB --> DT["daytrade-it"]
        DB --> SC["scalp-it"]
        KC["krx-quant-core<br/>shared market rules"] --> SW & DT & SC
    end

    subgraph US ["🇺🇸 US equities"]
        direction LR
        SH["Sharadar<br/>frozen at 09-10"] --> DD[("DuckDB<br/>point-in-time")] --> PR["portfolio-research<br/>macro-sector-agent"]
    end

    subgraph CX ["🪙 Crypto"]
        direction LR
        EX["Exchange APIs"] --> CR["binance-quant-engine"] --> CI["crypto-quant-insights"]
    end

    FC["fin-checkup<br/>DART · SEC EDGAR"]

    KR ~~~ US ~~~ CX ~~~ FC

    classDef source fill:#2563EB,stroke:#1E40AF,color:#FFFFFF
    classDef move   fill:#B45309,stroke:#78350F,color:#FFFFFF
    classDef out    fill:#059669,stroke:#065F46,color:#FFFFFF

    class SRC,SH,EX,FC source
    class AF,DB,DD move
    class SW,DT,SC,KC,PR,CR,CI out

    style KR fill:#0F172A08,stroke:#64748B
    style US fill:#0F172A08,stroke:#64748B
    style CX fill:#0F172A08,stroke:#64748B
```

<sub>Blue — data sources &amp; standalone tools · amber — collection &amp; storage · green — research &amp; engines. `scalp-it` and `daytrade-it` are private.</sub>

| Project | What it is |
|---|---|
| **[kiwoom-client](https://github.com/younghwan91/kiwoom-client)**<br/><img src="https://img.shields.io/badge/DATA%20SOURCE-2563EB?style=flat-square&labelColor=1E293B" alt="DATA SOURCE"/> | Kiwoom Securities REST API wrapper — every domestic-equity endpoint, real-time WebSocket, sync + async, auto token refresh. Ships an **MCP server** so AI agents call the same API as tools, real orders opt-in only · **`pip install kiwoom-client`** <a href="https://pypi.org/project/kiwoom-client/"><img src="https://img.shields.io/pypi/dm/kiwoom-client?style=flat-square&label=PyPI&color=2563EB&labelColor=1E293B" alt="PyPI downloads"/></a> |
| **[krx-news-client](https://github.com/younghwan91/krx-news-client)**<br/><img src="https://img.shields.io/badge/DATA%20SOURCE-2563EB?style=flat-square&labelColor=1E293B" alt="DATA SOURCE"/> | Korean market news and disclosures — DART filings and Toss Securities — as one schema, article bodies and per-company history included · **`pip install krx-news-client`** <a href="https://pypi.org/project/krx-news-client/"><img src="https://img.shields.io/pypi/dm/krx-news-client?style=flat-square&label=PyPI&color=2563EB&labelColor=1E293B" alt="PyPI downloads"/></a> |
| **[krx-fundamentals-client](https://github.com/younghwan91/krx-fundamentals-client)**<br/><img src="https://img.shields.io/badge/DATA%20SOURCE-2563EB?style=flat-square&labelColor=1E293B" alt="DATA SOURCE"/> | Korean corporate fundamentals — statements, valuation, dividends, screening — normalized from DART, KRX and Naver. No standing server |
| **[quant-airflow](https://github.com/younghwan91/quant-airflow)**<br/><img src="https://img.shields.io/badge/PIPELINE-7C3AED?style=flat-square&labelColor=1E293B" alt="PIPELINE"/> | The one pipeline behind both equity stacks: Korean prices, supply/demand, earnings, consensus, news and disclosures into TimescaleDB, with **delisted stocks backfilled** so downstream backtests aren't survivorship-biased. The US Sharadar rebuild into DuckDB is **paused** since the subscription lapsed |
| **[krx-quant-core](https://github.com/younghwan91/krx-quant-core)**<br/><img src="https://img.shields.io/badge/SHARED%20CORE-0F766E?style=flat-square&labelColor=1E293B" alt="SHARED CORE"/> | Where the Korean-equity systems agree on market mechanics — tick sizes, asymmetric price limits, a **dated** transaction-tax schedule, order guards, DART disclosure classes, a kill switch — plus the validation statistics and a research layer (grid sweeps, Optuna TPE, BIPOP CMA-ES) whose run ledger records every trial and **hard-locks the out-of-sample window**. No strategies; all three consumers pin the same version |
| **[fin-checkup](https://github.com/younghwan91/fin-checkup)**<br/><img src="https://img.shields.io/badge/TOOL-0891B2?style=flat-square&labelColor=1E293B" alt="TOOL"/> | Risk-disclosure alerts (rights offerings, CB issues, audit opinions, delistings) routed to Telegram, plus a traffic-light financial checkup over **DART &amp; SEC EDGAR**. **Facts and measurements only — never a recommendation** |
| **[swing-it](https://github.com/younghwan91/swing-it)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | KOSPI/KOSDAQ swing research on two axes: an **observation** screen of where money went by sector, and a **judgment** track where alpha hypotheses face walk-forward, random null controls, purged CV and Deflated Sharpe **enforced as CI guardrails**. **The rejections are the product** |
| **[portfolio-research](https://github.com/younghwan91/portfolio-research)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | US equity factor engine — strategy parameters walk-forward optimized on point-in-time, survivorship-bias-free data, with **Deflated Sharpe &amp; PBO** charging for the search; tactical ETF allocation goes through the same gate · [writeup](https://younghwan91.github.io/portfolio-research/) |
| **[macro-sector-agent](https://github.com/younghwan91/macro-sector-agent)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | Top-down US sector-cycle research that asks **which industry has been forgotten**, not what to buy. An LLM judge argues from evidence at one narrow waist only; **the machine never picks — it only excludes** |
| **[binance-quant-engine](https://github.com/younghwan91/binance-quant-engine)**<br/><img src="https://img.shields.io/badge/CRYPTO%20ENGINE-EA580C?style=flat-square&labelColor=1E293B" alt="CRYPTO ENGINE"/> | Strategy-agnostic Binance USDT-M futures backtest &amp; execution engine — zero lookahead, backtest↔live parity, exits placed as exchange-side algo orders, optional MCP server |
| **[crypto-quant-insights](https://github.com/younghwan91/crypto-quant-insights)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | Chart-backed research notes from validating a live futures system — crash stress tests, win rate vs. reward-to-risk, in- vs. out-of-sample divergence, Kelly leverage vs. what's actually run, backtest vs. live fills. The strategy stays private; the findings don't |
| **[automated-stock-trading-systems](https://github.com/younghwan91/automated-stock-trading-systems)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | Backtester for Bensdorp's seven non-correlated trading systems (educational reimplementation) |

<h3><img src="https://img.shields.io/badge/%F0%9F%94%92%20PRIVATE-64748B?style=for-the-badge&labelColor=1E293B" height="26" alt="Private"/></h3>

Strategies and parameters stay closed. Only structure and discipline are written down. **Happy to walk through any of these on request.**

| Project | What it is |
|---|---|
| **scalp-it**<br/><img src="https://img.shields.io/badge/PRIVATE-64748B?style=flat-square&labelColor=1E293B" alt="PRIVATE"/> | Korean intraday framework — live tick/orderbook collection, a **pre-registered** validation program (hashed pre-registrations, hard-locked out-of-sample window, measured once) and an order execution loop that now runs **dry-run only** |
| **daytrade-it**<br/><img src="https://img.shields.io/badge/PRIVATE-64748B?style=flat-square&labelColor=1E293B" alt="PRIVATE"/> | Korean-equity news day-trading system — a daemon polls Toss news, Claude extracts **facts only** (subject, novelty, direction) and code does the scoring, behind a DART hard-severity gate that refuses entries when its cache is missing or stale. Runs in paper mode now; the replay engine, ledger and write-ups stay |
| **quantbox**<br/><img src="https://img.shields.io/badge/PRIVATE-64748B?style=flat-square&labelColor=1E293B" alt="PRIVATE"/> | Binance USDT-M futures breakout/momentum system, traded live and currently paused. `binance-quant-engine` is the public extract with the strategies removed |
| **crypto-pair-trading**<br/><img src="https://img.shields.io/badge/PRIVATE-64748B?style=flat-square&labelColor=1E293B" alt="PRIVATE"/> | First iteration of the crypto pair-trading framework — predecessor of `quantbox` |
| **resume-private**<br/><img src="https://img.shields.io/badge/PRIVATE-64748B?style=flat-square&labelColor=1E293B" alt="PRIVATE"/> | Private résumé source (LaTeX) |

<h3><img src="https://img.shields.io/badge/%F0%9F%9B%A0%EF%B8%8F%20TECH-7C3AED?style=for-the-badge&labelColor=1E293B" height="26" alt="Tech"/></h3>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="CUDA"/>
  <img src="https://img.shields.io/badge/TensorRT-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="TensorRT"/>
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="pandas"/>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/TimescaleDB-FDB515?style=flat-square&logo=timescale&logoColor=black" alt="TimescaleDB"/>
  <img src="https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white" alt="Airflow"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/>
</p>
