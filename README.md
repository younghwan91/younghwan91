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
- 📈 On the side, I build a full open-source **quant stack** — market-data APIs, a collection pipeline, and research &amp; backtesting engines
- 🛰️ **Every sensor, every modality** — RGB/stereo/structured-light cameras, 4D imaging radar, LiDAR, IMU/GPS, point clouds &amp; RF signals, 3D scans, video, and financial time-series; few data types I haven't shipped with

<h3><img src="https://img.shields.io/badge/%F0%9F%94%AD%20OPEN--SOURCE-059669?style=for-the-badge&labelColor=1E293B" height="26" alt="Open-source"/></h3>

Market-data APIs feed a collection pipeline into TimescaleDB that the research layer reads — plus a standalone crypto engine fed straight from exchange APIs.

```mermaid
flowchart TD
    K["🔌 kiwoom-rest-api"] --> AF
    F["🔌 krx-fundamentals-api"] --> AF
    NW["🔌 krx-news-rest-api"] --> AF
    AF["🗄️ kr-quant-airflow"] --> DB[("TimescaleDB")]
    DB --> Q["🧪 kr-quant"]
    DB --> O["🧪 opt_portfolio"]
    DB --> AT["🧪 automated-stock-<br/>trading-systems"]
    EX["🔌 Exchange APIs"] --> CR["₿ quantbox-engine<br/>backtest ↔ live"]

    classDef src    fill:#2563EB,stroke:#1E40AF,stroke-width:1px,color:#FFFFFF
    classDef pipe   fill:#7C3AED,stroke:#5B21B6,stroke-width:1px,color:#FFFFFF
    classDef store  fill:#B45309,stroke:#78350F,stroke-width:1px,color:#FFFFFF
    classDef res    fill:#059669,stroke:#065F46,stroke-width:1px,color:#FFFFFF
    classDef crypto fill:#EA580C,stroke:#9A3412,stroke-width:1px,color:#FFFFFF

    class K,F,NW,EX src
    class AF pipe
    class DB store
    class Q,O,AT res
    class CR crypto

    linkStyle default stroke:#94A3B8,stroke-width:1.5px
```

| Project | What it is |
|---|---|
| **[kiwoom-rest-api](https://github.com/younghwan91/kiwoom-rest-api)**<br/><img src="https://img.shields.io/badge/DATA%20SOURCE-2563EB?style=flat-square&labelColor=1E293B" alt="DATA SOURCE"/> | Kiwoom Securities REST API wrapper — 207 endpoints + real-time WebSocket |
| **[quantbox-engine](https://github.com/younghwan91/quantbox-engine)**<br/><img src="https://img.shields.io/badge/CRYPTO%20ENGINE-EA580C?style=flat-square&labelColor=1E293B" alt="CRYPTO ENGINE"/> | Crypto futures backtest &amp; execution engine — zero lookahead, backtest↔live parity |
| **[kr-quant-airflow](https://github.com/younghwan91/kr-quant-airflow)**<br/><img src="https://img.shields.io/badge/PIPELINE-7C3AED?style=flat-square&labelColor=1E293B" alt="PIPELINE"/> | Airflow pipeline collecting Korean market data into TimescaleDB |
| **[krx-fundamentals-api](https://github.com/younghwan91/krx-fundamentals-api)**<br/><img src="https://img.shields.io/badge/DATA%20SOURCE-2563EB?style=flat-square&labelColor=1E293B" alt="DATA SOURCE"/> | Korean corporate fundamentals API (DART + KRX + Naver) |
| **[krx-news-rest-api](https://github.com/younghwan91/krx-news-rest-api)**<br/><img src="https://img.shields.io/badge/DATA%20SOURCE-2563EB?style=flat-square&labelColor=1E293B" alt="DATA SOURCE"/> | Korean market news &amp; disclosure collection API (FastAPI + Redis) |
| **[kr-quant](https://github.com/younghwan91/kr-quant)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | KOSPI/KOSDAQ alpha research — walk-forward, trade-level distributions &amp; random null controls enforced as guardrails |
| **[opt_portfolio](https://github.com/younghwan91/opt_portfolio)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | VAA-based tactical asset allocation |
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
