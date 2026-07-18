<h1 align="center">Younghwan Chae</h1>

<p align="center">
  <b>Mathematical Optimization PhD</b> &nbsp;·&nbsp; Quantitative Research &amp; Applied ML<br/>
  Turning noisy, non-stationary market signals into alpha — optimization &amp; signal-processing rigor, backed by production trading infrastructure.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/younghwan-chae/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:chyohw97@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/></a>
  <a href="https://github.com/younghwan91/resume/releases/latest/download/resume_en.pdf"><img src="https://img.shields.io/badge/Résumé-B7472A?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Résumé (PDF)"/></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/younghwan91/younghwan91/main/assets/optimization.svg" width="600" alt="Gradient descent converging to the minimum of a loss curve"/>
</p>

<p align="center">
  <b>Mathematical Optimization</b> · Bayesian State Estimation · Signal Processing · Backtesting Infrastructure · Deep Learning
</p>

---

### 🗺️ Open-source quant stack — built end to end

Raw market-data APIs feed a collection pipeline into TimescaleDB that the research layer reads — plus a standalone, live-parity crypto engine.

```mermaid
flowchart LR
    A["🔌 Market-data APIs<br/>kiwoom-rest-api · krx-fundamentals-api · krx-news-rest-api"] --> B["🗄️ Pipeline<br/>kr-quant-airflow → TimescaleDB"] --> C["🧪 Research<br/>opt_portfolio · automated-stock-trading-systems"]
    D["₿ quantbox-engine<br/>crypto futures — backtest ↔ live"]
```

| Project | What it is |
|---|---|
| **[quantbox-engine](https://github.com/younghwan91/quantbox-engine)** | Crypto futures backtest &amp; execution engine — zero lookahead, backtest↔live parity |
| **[kiwoom-rest-api](https://github.com/younghwan91/kiwoom-rest-api)** | Kiwoom Securities REST API wrapper — 207 endpoints + real-time WebSocket |
| **[kr-quant-airflow](https://github.com/younghwan91/kr-quant-airflow)** | Airflow pipeline collecting Korean market data into TimescaleDB |
| **[krx-fundamentals-api](https://github.com/younghwan91/krx-fundamentals-api)** | Korean corporate fundamentals API (DART + KRX + Naver) |
| **[opt_portfolio](https://github.com/younghwan91/opt_portfolio)** | VAA-based tactical asset allocation |
| **[automated-stock-trading-systems](https://github.com/younghwan91/automated-stock-trading-systems)** | Backtester for Bensdorp's 7 non-correlated systems |

### 🧠 Background

- 🎯 **PhD in numerical optimization** — non-linear optimization, surrogate modeling &amp; Bayesian state estimation for noisy, non-stationary signals (all degrees *Cum Laude*)
- 🛰️ Applied ML at **production scale** @ Doosan Robotics / bitsensing — multi-sensor fusion &amp; radar signal processing shipped to mass production (**200+ deployments, 8 countries**) · **10 patents · 6 peer-reviewed papers**
- ⚙️ **Trading infrastructure** — live crypto execution engine, lookahead-safe backtesting with overfitting guards, high-frequency market-data pipelines

### 🛠️ Tech

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="pandas"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="CUDA"/>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/TimescaleDB-FDB515?style=flat-square&logo=timescale&logoColor=black" alt="TimescaleDB"/>
  <img src="https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white" alt="Airflow"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/>
</p>
