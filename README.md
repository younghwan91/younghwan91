<h1 align="center">Younghwan Chae, Ph.D. · 채영환</h1>

<p align="center">
  <b>PhD in Mechanical Engineering</b> &nbsp;—&nbsp; <b><i>Mathematical Optimization</i></b> &nbsp;·&nbsp; ML &amp; Perception Engineer <b>@ Doosan Robotics</b><br/>
  <b>Mathematical optimization is the through-line</b> — numerical optimization, surrogate modeling &amp; state estimation, carried from theory into 3D perception, sensor fusion, and production systems.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/younghwan-chae/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:chyohw97@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/></a>
  <a href="https://github.com/younghwan91/resume/releases/latest/download/resume_en.pdf"><img src="https://img.shields.io/badge/Résumé-B7472A?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Résumé (PDF)"/></a>
</p>

---

<h3><img src="https://img.shields.io/badge/%F0%9F%A7%A0%20BACKGROUND-2563EB?style=for-the-badge&labelColor=1E293B" height="26" alt="Background"/></h3>

- 🎓 **PhD in Mechanical Engineering** — all degrees *Cum Laude*
- 🤖 **ML &amp; Perception Engineer @ Doosan Robotics** (prev. bitsensing) — 3D perception, sensor fusion &amp; robotics AI across **camera · radar · LiDAR**
- 🏭 Shipped **multi-sensor perception to mass production** — 200+ deployments across 8 countries, −51% fusion error · **10 patents · 6 peer-reviewed papers**
- 📈 On the side, I build a full open-source **quant stack** across **Korean equities · US equities · crypto** — market-data APIs, a collection pipeline, and research &amp; backtesting engines, with point-in-time data and survivorship-bias handling throughout
- 🛰️ **Every sensor, every modality** — RGB/stereo/structured-light cameras, 4D imaging radar, LiDAR, IMU/GPS, point clouds &amp; RF signals, 3D scans, video, and financial time-series; few data types I haven't shipped with

<h3><img src="https://img.shields.io/badge/%F0%9F%94%AD%20OPEN--SOURCE-059669?style=for-the-badge&labelColor=1E293B" height="26" alt="Open-source"/></h3>

Three stacks that share a shape — **collect → store → research** — but only the Korean one needs all three stages. The two REST APIs are standalone services, not pipeline inputs.

```mermaid
flowchart TB
    subgraph KR ["🇰🇷 Korean equities"]
        direction LR
        K["kiwoom-rest-api"] --> AF["quant-airflow<br/>DART · KRX · Naver"] --> DB[("TimescaleDB<br/>delisted included")] --> Q["kr-quant"]
    end

    subgraph US ["🇺🇸 US equities"]
        direction LR
        SH["Sharadar"] --> O["opt_portfolio"]
        YF["yfinance"] --> AT["automated-stock-trading-systems"]
    end

    subgraph CX ["🪙 Crypto"]
        direction LR
        EX["Exchange APIs"] --> CR["quantbox-engine"]
    end

    subgraph SVC ["Standalone REST APIs"]
        direction TB
        F["krx-fundamentals-api"]
        NW["krx-news-rest-api"]
    end

    %% 세로 정렬용 — `~~~` 는 그 자체로 보이지 않는 링크다(linkStyle 불필요).
    KR ~~~ US ~~~ CX ~~~ SVC

    classDef source fill:#2563EB,stroke:#1E40AF,color:#FFFFFF
    classDef move   fill:#B45309,stroke:#78350F,color:#FFFFFF
    classDef out    fill:#059669,stroke:#065F46,color:#FFFFFF

    class K,SH,YF,EX,F,NW source
    class AF,DB move
    class Q,O,AT,CR out

    style KR  fill:#0F172A08,stroke:#64748B
    style US  fill:#0F172A08,stroke:#64748B
    style CX  fill:#0F172A08,stroke:#64748B
    style SVC fill:#0F172A08,stroke:#64748B,stroke-dasharray:4 3
```

<sub>Blue — data sources · amber — collection &amp; storage · green — research &amp; engines. Dashed — standalone services.</sub>

| Project | What it is |
|---|---|
| **[kiwoom-rest-api](https://github.com/younghwan91/kiwoom-rest-api)**<br/><img src="https://img.shields.io/badge/DATA%20SOURCE-2563EB?style=flat-square&labelColor=1E293B" alt="DATA SOURCE"/> | Kiwoom Securities REST API wrapper — 186 endpoints (182 REST + 4 condition-search) &amp; 19 real-time WebSocket feeds · sync + async, auto token refresh · **`pip install kiwoom-client`** <a href="https://pypi.org/project/kiwoom-client/"><img src="https://img.shields.io/pypi/dm/kiwoom-client?style=flat-square&label=PyPI&color=2563EB&labelColor=1E293B" alt="PyPI downloads"/></a> |
| **[quantbox-engine](https://github.com/younghwan91/quantbox-engine)**<br/><img src="https://img.shields.io/badge/CRYPTO%20ENGINE-EA580C?style=flat-square&labelColor=1E293B" alt="CRYPTO ENGINE"/> | Crypto futures backtest &amp; execution engine — zero lookahead, backtest↔live parity |
| **[quant-airflow](https://github.com/younghwan91/quant-airflow)**<br/><img src="https://img.shields.io/badge/PIPELINE-7C3AED?style=flat-square&labelColor=1E293B" alt="PIPELINE"/> | Airflow pipeline collecting Korean market data (prices, supply/demand, earnings, consensus, shares outstanding) into TimescaleDB — 11 DAGs over DART · Kiwoom · KRX · Naver, with **delisted-stock backfill** so downstream backtests aren't survivorship-biased |
| **[krx-fundamentals-api](https://github.com/younghwan91/krx-fundamentals-api)**<br/><img src="https://img.shields.io/badge/DATA%20SOURCE-2563EB?style=flat-square&labelColor=1E293B" alt="DATA SOURCE"/> | Korean corporate fundamentals API — financial statements, valuation metrics, dividends, major shareholders &amp; stock screening (DART + KRX + Naver) |
| **[krx-news-rest-api](https://github.com/younghwan91/krx-news-rest-api)**<br/><img src="https://img.shields.io/badge/DATA%20SOURCE-2563EB?style=flat-square&labelColor=1E293B" alt="DATA SOURCE"/> | Korean market news &amp; disclosure collection API (FastAPI + Redis) |
| **[kr-quant](https://github.com/younghwan91/kr-quant)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | KOSPI/KOSDAQ alpha research at the trade-distribution level — walk-forward, random null controls, purged CV, Deflated Sharpe &amp; survivorship-corrected universes, all **enforced as CI guardrails**. Findings so far: alpha splits into **convex** (tail-driven) vs **diffuse** types; PEAD is the validated diffuse one; and restoring delisted names *raised* its excess return — survivorship bias distorts the benchmark more than the strategy |
| **[opt_portfolio](https://github.com/younghwan91/opt_portfolio)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | US equity factor engine — **158 factors over 21,963 tickers (1997–2026)**, point-in-time &amp; survivorship-bias-free, walk-forward optimization gated by Deflated Sharpe · plus a VAA tactical asset allocation backtester |
| **[automated-stock-trading-systems](https://github.com/younghwan91/automated-stock-trading-systems)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | Backtester for Bensdorp's 7 non-correlated systems |

🔒 **Also private** — equity screeners (Wyckoff accumulation · Minervini + VCP), a statistical-arbitrage crypto engine, and live trading systems. *Available on request.*

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
