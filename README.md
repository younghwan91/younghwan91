<h1 align="center">Younghwan Chae, Ph.D. · 채영환</h1>

<p align="center">
  <b>Open-source quant infrastructure for Korean equities.</b><br/>
  PhD in mechanical engineering (<i>mathematical optimization</i>) · ML &amp; perception engineer <b>@ Doosan Robotics</b> by day.
</p>

<p align="center"><a href="README.ko.md">한국어</a> · <b>English</b></p>
<p align="center">
  <a href="https://www.linkedin.com/in/younghwan-chae/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:chyohw97@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/></a>
  <a href="https://github.com/younghwan91/resume/releases/latest/download/resume_en.pdf"><img src="https://img.shields.io/badge/Résumé-B7472A?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Résumé (PDF)"/></a>
</p>

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

- **Korea** — [kiwoom-client](https://github.com/younghwan91/kiwoom-client) · [krx-news-client](https://github.com/younghwan91/krx-news-client) · [krx-fundamentals-client](https://github.com/younghwan91/krx-fundamentals-client) · [quant-airflow](https://github.com/younghwan91/quant-airflow) · [krx-quant-core](https://github.com/younghwan91/krx-quant-core) · [swing-it](https://github.com/younghwan91/swing-it) · [sector-flow](https://github.com/younghwan91/sector-flow) · [daytrade-it](https://github.com/younghwan91/daytrade-it) · [scalp-it](https://github.com/younghwan91/scalp-it)
- **US** — [portfolio-research](https://github.com/younghwan91/portfolio-research) · [macro-sector-agent](https://github.com/younghwan91/macro-sector-agent)
- **Crypto** — [quantbox](https://github.com/younghwan91/quantbox) · [crypto-quant-insights](https://github.com/younghwan91/crypto-quant-insights)
- **Tools** — [fin-checkup](https://github.com/younghwan91/fin-checkup) · [automated-stock-trading-systems](https://github.com/younghwan91/automated-stock-trading-systems)
