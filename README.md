<h1 align="center">Hi, I'm Younghwan Chae 👋</h1>

<p align="center">
  <b>PhD in Mechanical Engineering · Mathematical Optimization</b><br/>
  ML &amp; Perception Engineer building 3D perception &amp; sensor fusion for robotics —<br/>
  and, in my own time, a full quant stack for Korean &amp; crypto markets.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/younghwan-chae/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:chyohw97@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/></a>
  <a href="https://github.com/younghwan91"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
</p>

---

### 🧭 About me

- 🎓 **PhD, Mechanical Engineering** (University of Pretoria) — research in **mathematical optimization**: gradient-only line searches (GOALS), surrogate modeling, optimal sensor placement. All degrees *Cum Laude*.
- 🤖 **ML &amp; Perception Engineer @ Doosan Robotics** — 3D perception, sensor fusion, and MLOps for robotics &amp; autonomous systems (camera · radar · LiDAR).
- 📈 In my own time, I build **quant research tooling** for Korean equities and crypto — a full stack from raw market APIs to backtests, with a focus on **lookahead-safe data** and **reproducible backtests**.
- 📝 **10 patents** · **6 peer-reviewed publications** (IEEE Sensors, Springer Nature, Elsevier).

### 🗺️ How my projects fit together

My open-source repos form one **Korean-market quant stack** — raw market APIs feed a
collection pipeline into TimescaleDB, which the research layer reads — plus a separate
**crypto** track.

```mermaid
flowchart TB
    A["🔌 Market-data APIs<br/>kiwoom-rest-api · krx-fundamentals-api · krx-news-rest-api"]
    B["🗄️ Collection and Storage<br/>kr-quant-airflow to TimescaleDB"]
    C["🧪 Research and Strategy<br/>opt_portfolio · automated-stock-trading-systems · kr-quant (private)"]
    D["₿ Crypto track<br/>quantbox-engine — backtest and live parity"]

    A --> B --> C
```

### 🔭 Open-source projects

**🇰🇷 Korean-market quant stack**

| Layer | Project | What it is |
|---|---|---|
| 🔌 API | **[kiwoom-rest-api](https://github.com/younghwan91/kiwoom-rest-api)** ⭐7 | Python wrapper for the Kiwoom Securities REST API — 207 KR-stock endpoints + real-time WebSocket |
| 🔌 API | **[krx-fundamentals-api](https://github.com/younghwan91/krx-fundamentals-api)** | Corporate fundamentals REST API (DART + KRX + Naver) — financials, valuation, dividends, screening |
| 🔌 API | **[krx-news-rest-api](https://github.com/younghwan91/krx-news-rest-api)** | Market news &amp; disclosure collection REST API (FastAPI + Redis) |
| 🗄️ Pipeline | **[kr-quant-airflow](https://github.com/younghwan91/kr-quant-airflow)** | Airflow pipeline collecting prices/flows/earnings/consensus into TimescaleDB |
| 🧪 Research | **[opt_portfolio](https://github.com/younghwan91/opt_portfolio)** ⭐2 | VAA-based tactical asset-allocation / portfolio management |
| 🧪 Research | **[automated-stock-trading-systems](https://github.com/younghwan91/automated-stock-trading-systems)** | Backtester for the 7 non-correlated systems from Bensdorp's *Automated Stock Trading Systems* |

**₿ Crypto**

| Project | What it is |
|---|---|
| **[quantbox-engine](https://github.com/younghwan91/quantbox-engine)** | Strategy-agnostic crypto futures backtest &amp; execution engine — guaranteed zero lookahead, backtest↔live parity |

### 🛠️ Tech

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="CUDA"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="pandas"/>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/TimescaleDB-FDB515?style=flat-square&logo=timescale&logoColor=black" alt="TimescaleDB"/>
  <img src="https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white" alt="Airflow"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white" alt="Redis"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux"/>
</p>

### 📊 GitHub

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=younghwan91&show_icons=true&hide_border=true&count_private=true" height="165" alt="GitHub stats"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=younghwan91&layout=compact&hide_border=true&langs_count=8" height="165" alt="Top languages"/>
</p>
