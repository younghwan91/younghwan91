<h1 align="center">Younghwan Chae</h1>

<p align="center">
  <b>PhD in Mechanical Engineering</b> <i>(Mathematical Optimization)</i> &nbsp;·&nbsp; ML &amp; Perception Engineer <b>@ Doosan Robotics</b><br/>
  3D perception &amp; sensor fusion for robotics and autonomous systems — grounded in optimization, shipped to production.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/younghwan-chae/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:chyohw97@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/></a>
  <a href="https://github.com/younghwan91/resume/releases/latest/download/resume_en.pdf"><img src="https://img.shields.io/badge/Résumé-B7472A?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Résumé (PDF)"/></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/younghwan91/younghwan91/main/assets/optimization.svg" width="560" alt="Gaussian-process surrogate (mean ± σ) with Bayesian optimization converging to the global optimum"/>
</p>

<p align="center">
  <b>Mathematical Optimization</b> · 3D Perception &amp; Sensor Fusion · Camera · Radar · LiDAR · MLOps · Quantitative Research
</p>

---

### 🧠 Background

- 🎓 **PhD in Mechanical Engineering**, specialized in **mathematical optimization** — numerical optimization, surrogate modeling, state estimation (all degrees *Cum Laude*)
- 🤖 **ML &amp; Perception Engineer @ Doosan Robotics** (prev. bitsensing) — 3D perception, sensor fusion &amp; robotics AI across **camera · radar · LiDAR**
- 🏭 Shipped camera/radar/LiDAR **multi-sensor perception to mass production** — 200+ deployments across 8 countries, −51% fusion error · **10 patents · 6 peer-reviewed papers**
- 📈 On the side, I build a full open-source **quant stack** — market-data APIs, a collection pipeline, and backtesting engines

### 🔭 Open-source

Market-data APIs feed a collection pipeline into TimescaleDB that the research layer reads — plus a standalone, live-parity crypto engine.

```mermaid
flowchart LR
    subgraph APIs["🔌 Market-data APIs"]
        direction TB
        K[kiwoom-rest-api]
        F[krx-fundamentals-api]
        N[krx-news-rest-api]
    end
    P["🗄️ kr-quant-airflow<br/>→ TimescaleDB"]
    subgraph RES["🧪 Research"]
        direction TB
        O[opt_portfolio]
        S[automated-stock-trading-systems]
    end
    C["₿ quantbox-engine<br/>crypto futures · backtest ↔ live"]
    APIs --> P --> RES
```

| Project | What it is |
|---|---|
| **[kiwoom-rest-api](https://github.com/younghwan91/kiwoom-rest-api)** | Kiwoom Securities REST API wrapper — 207 endpoints + real-time WebSocket |
| **[quantbox-engine](https://github.com/younghwan91/quantbox-engine)** | Crypto futures backtest &amp; execution engine — zero lookahead, backtest↔live parity |
| **[kr-quant-airflow](https://github.com/younghwan91/kr-quant-airflow)** | Airflow pipeline collecting Korean market data into TimescaleDB |
| **[krx-fundamentals-api](https://github.com/younghwan91/krx-fundamentals-api)** | Korean corporate fundamentals API (DART + KRX + Naver) |
| **[opt_portfolio](https://github.com/younghwan91/opt_portfolio)** | VAA-based tactical asset allocation |
| **[automated-stock-trading-systems](https://github.com/younghwan91/automated-stock-trading-systems)** | Backtester for Bensdorp's 7 non-correlated systems |

🔒 **Also private** — equity screeners (Wyckoff accumulation · Minervini + VCP), a statistical-arbitrage crypto engine, and live trading systems. *Available on request.*

### 🛠️ Tech

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
