<h1 align="center">Younghwan Chae, Ph.D. · 채영환</h1>

<p align="center">
  <b>기계공학 박사</b> &nbsp;—&nbsp; <b><i>수치 최적화</i></b> &nbsp;·&nbsp; <b>두산로보틱스</b> ML · 인지 엔지니어<br/>
<b>학위 때부터 붙잡고 있는 건 결국 최적화 하나다.</b> 수치 최적화와 대리모델, 상태추정으로 시작해<br/>지금은 3D 인지와 센서 퓨전, 양산 시스템에 그걸 쓴다.
</p>

<p align="center"><b>한국어</b> · <a href="README.md">English</a></p>
<p align="center">
  <a href="https://www.linkedin.com/in/younghwan-chae/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:chyohw97@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/></a>
  <a href="https://github.com/younghwan91/resume/releases/latest/download/resume_en.pdf"><img src="https://img.shields.io/badge/Résumé-B7472A?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Résumé (PDF)"/></a>
</p>

---

<h3><img src="https://img.shields.io/badge/%F0%9F%94%AD%20%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4-059669?style=for-the-badge&labelColor=1E293B" height="26" alt="오픈소스"/></h3>

세 스택이 같은 뼈대를 쓴다. **수집하고, 저장하고, 그 위에서만 검증한다.**
두 주식 시장은 Airflow 하나를 나눠 쓰고, 단독으로 도는 서비스들은 파이프라인 바깥에 있다.

```mermaid
flowchart TB
    subgraph KR ["🇰🇷 한국 주식"]
        direction LR
        K["kiwoom-client"] --> AF["quant-airflow<br/>DART · KRX · 네이버 · 토스"] --> DB[("TimescaleDB<br/>상장폐지 포함")] --> Q["kr-quant"]
        NW["krx-news-client"] --> AF
        F["krx-fundamentals-client"] --> AF
        DB -- "news_judgments<br/>LLM 판단" --> SC["scalp-it"]
        DB -- "시세, 읽기전용" --> KSIG["krx-signal-engine<br/>리스크 게이트"]
        K --> KSIG
    end

    subgraph US ["🇺🇸 미국 주식"]
        direction LR
        SH["Sharadar"] --> AFU["quant-airflow<br/>일괄 스냅샷 재생성"] --> DD[("DuckDB<br/>시점 정합")] --> O["portfolio-research"]
        SH --> MS["macro-sector-agent<br/>자체 PIT DuckDB"]
        YF["yfinance"] --> AT["automated-stock-trading-systems"]
    end

    subgraph CX ["🪙 암호화폐"]
        direction LR
        EX["거래소 API"] --> CR["quantbox-engine"]
    end

    subgraph SVC ["단독 서비스 · 도구"]
        direction TB
        FC["fin-checkup"]
    end

    %% 세로 정렬용 — `~~~` 는 그 자체로 보이지 않는 링크다(linkStyle 불필요).
    KR ~~~ US ~~~ CX ~~~ SVC

    classDef source fill:#2563EB,stroke:#1E40AF,color:#FFFFFF
    classDef move   fill:#B45309,stroke:#78350F,color:#FFFFFF
    classDef out    fill:#059669,stroke:#065F46,color:#FFFFFF

    class K,SH,YF,EX,F,NW,FC source
    class AF,AFU,DB,DD move
    class Q,O,AT,CR,SC,MS,KSIG out

    style KR  fill:#0F172A08,stroke:#64748B
    style US  fill:#0F172A08,stroke:#64748B
    style CX  fill:#0F172A08,stroke:#64748B
    style SVC fill:#0F172A08,stroke:#64748B,stroke-dasharray:4 3
```

<sub>파랑은 데이터 원천과 단독 서비스, 앰버는 수집·저장, 초록은 리서치·엔진이다. 점선은 파이프라인 바깥을 뜻한다.</sub>

| 프로젝트 | 무엇인가 |
|---|---|
| **[kiwoom-client](https://github.com/younghwan91/kiwoom-client)**<br/><img src="https://img.shields.io/badge/DATA%20SOURCE-2563EB?style=flat-square&labelColor=1E293B" alt="DATA SOURCE"/> | 키움증권 REST API 를 파이썬으로 감싼 라이브러리. 국내주식 엔드포인트를 빠짐없이 덮고 실시간 WebSocket 도 받는다. sync 와 async 를 모두 지원하고 토큰은 알아서 갱신한다. 예전 OpenAPI+ 처럼 32bit 윈도우에 묶이지 않아 리눅스 서버에서 그대로 돈다. REST 엔드포인트 182개와 `condition_search` 를 통째로 노출하는 **MCP 서버**도 들어 있어 AI 에이전트가 바로 도구로 쓸 수 있다 — 실주문은 옵트인일 때만 · **`pip install kiwoom-client`** <a href="https://pypi.org/project/kiwoom-client/"><img src="https://img.shields.io/pypi/dm/kiwoom-client?style=flat-square&label=PyPI&color=2563EB&labelColor=1E293B" alt="PyPI downloads"/></a> |
| **[quant-airflow](https://github.com/younghwan91/quant-airflow)**<br/><img src="https://img.shields.io/badge/PIPELINE-7C3AED?style=flat-square&labelColor=1E293B" alt="PIPELINE"/> | 두 주식 스택에 데이터를 대는 파이프라인 — DAG 16개. 한국 쪽은 시세·수급·실적·컨센서스·상장주식수·뉴스공시(krx-fundamentals-client·krx-news-client 경유)를 DART·키움·KRX·네이버·토스에서 모아 TimescaleDB 에 쌓는다. **상장폐지 종목까지 되살려 담기 때문에** 이 데이터로 만든 백테스트는 생존편향에 빠지지 않는다. 그 뉴스·공시 스트림을 LLM이 구조화 판단(이벤트 유형·감성·재탕 여부)으로 바꿔 scalp-it의 장중 필터링에 공급한다. 미국 쪽은 Sharadar 스냅샷을 매일 통째로 받아 DuckDB 스토어를 새로 만든 뒤 한 번에 갈아끼운다 |
| **[krx-fundamentals-client](https://github.com/younghwan91/krx-fundamentals-client)**<br/><img src="https://img.shields.io/badge/DATA%20SOURCE-2563EB?style=flat-square&labelColor=1E293B" alt="DATA SOURCE"/> | 국내 기업 펀더멘탈 Python 클라이언트 라이브러리. 재무제표(최대 100종목씩 배치 조회)와 투자지표, 배당, 종목 스크리닝을 DART·KRX·네이버에서 모아 정규화한다. 상시 서버 없이 호출 시점에 소스에 직접 요청한다 · quant-airflow 의 실적·주식수·컨센서스 DAG 가 이걸 쓴다 |
| **[krx-news-client](https://github.com/younghwan91/krx-news-client)**<br/><img src="https://img.shields.io/badge/DATA%20SOURCE-2563EB?style=flat-square&labelColor=1E293B" alt="DATA SOURCE"/> | 한국 주식 뉴스와 공시를 모아 주는 Python 클라이언트 라이브러리 — DART 공시 + 토스증권 뉴스. 매체마다 같은 사건을 조금씩 다르게 쓰는데, 그걸 한 스키마로 눕혀서 내준다 · quant-airflow 의 `daily_news` DAG 가 이걸 쓴다 · **`pip install krx-news-client`** <a href="https://pypi.org/project/krx-news-client/"><img src="https://img.shields.io/pypi/dm/krx-news-client?style=flat-square&label=PyPI&color=2563EB&labelColor=1E293B" alt="PyPI downloads"/></a> |
| **[fin-checkup](https://github.com/younghwan91/fin-checkup)**<br/><img src="https://img.shields.io/badge/TOOL-0891B2?style=flat-square&labelColor=1E293B" alt="TOOL"/> | 관심 종목에 유상증자·전환사채·감사의견·상장폐지 같은 위험 공시가 뜨면 텔레그램으로 알린다. 재무 17개 지표는 작년 값, 업종 중앙값, 동종업계 백분위와 나란히 놓아 신호등으로 보여준다. DART 와 SEC 양쪽을 본다. **재무 수치와 사실만 전하고 종목 추천은 하지 않는다** |
| **[kr-quant](https://github.com/younghwan91/kr-quant)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | 코스피·코스닥 알파를 심사한다. walk-forward, 랜덤 음성대조, purged CV, Deflated Sharpe, 생존편향 보정 유니버스를 **CI 가 전부 검사하므로 빠뜨릴 수가 없다**. **여기서 나오는 건 대개 기각이고, 그게 이 저장소의 산출물이다.** 아무 신호도 없는 난수가 “6폴드 중 5폴드 양수”를 46% 확률로 통과하니, 판별 기준은 폴드 개수가 아니라 자기 자신의 무작위 버전을 이기느냐다. 일일 섹터 자금흐름을 재는 축도 같이 있다 |
| **[portfolio-research](https://github.com/younghwan91/portfolio-research)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | 미국주식 팩터 엔진. 시점이 어긋나지 않고 생존편향을 보정한 데이터 위에서만 walk-forward 를 돌리고, 그 결과를 **Deflated Sharpe 와 PBO** 로 거른다. ETF 전술배분도 같이 검증한다. **통과한 것만 싣지는 않는다.** 사전등록한 TAA 9건은 전부 PBO 관문을 못 넘었고, 표제로 쓰던 숫자 하나는 스스로 철회했다 · [writeup](https://younghwan91.github.io/portfolio-research/) |
| **[macro-sector-agent](https://github.com/younghwan91/macro-sector-agent)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | 하향식으로 미국 산업 테마를 찾는 리서치 파이프라인 — 자체 Sharadar 기반 시점정합 DuckDB 위에서 돈다. “지금 뭘 사야 하나”가 아니라 “**지금 어느 산업이 잊혔나**”를 먼저 묻는다. 표준 섹터 분류로는 안 보이는 해상도로 시장을 쪼갠다. 사이클 저점인지 그냥 죽어가는 산업인지는 LLM 판별기가 증거를 놓고 따지되, **파이프라인의 좁은 허리에만 두고** 위아래는 전부 결정론으로 짰다. **기계는 종목을 고르지 않고 빼기만 한다** — 전략 파라미터는 저장소에 없다 |
| **[quantbox-engine](https://github.com/younghwan91/quantbox-engine)**<br/><img src="https://img.shields.io/badge/CRYPTO%20ENGINE-EA580C?style=flat-square&labelColor=1E293B" alt="CRYPTO ENGINE"/> | 암호화폐 선물 백테스트·실행 엔진. 전략이 받는 배열에 미래 봉이 애초에 안 들어가고, 같은 전략 객체가 백테스트와 실거래를 그대로 탄다. 청산 주문은 거래소에 미리 걸어 두므로 봇이 죽어도 남는다 |
| **[automated-stock-trading-systems](https://github.com/younghwan91/automated-stock-trading-systems)**<br/><img src="https://img.shields.io/badge/RESEARCH-059669?style=flat-square&labelColor=1E293B" alt="RESEARCH"/> | Bensdorp 의 비상관 트레이딩 시스템 7개를 교육용으로 다시 구현한 백테스터. 일곱을 함께 돌리면 상관이 낮아진다는 주장을 그대로 확인해 본다 |

<h3><img src="https://img.shields.io/badge/%F0%9F%94%92%20%EB%B9%84%EA%B3%B5%EA%B0%9C-64748B?style=for-the-badge&labelColor=1E293B" height="26" alt="비공개"/></h3>

전략과 파라미터는 열지 않는다. 어떻게 굴러가는지, 어떤 규율을 지키는지만 적었다. **궁금하시면 따로 설명해 드린다.**

| 프로젝트 | 무엇인가 |
|---|---|
| **scalp-it**<br/><img src="https://img.shields.io/badge/PRIVATE-64748B?style=flat-square&labelColor=1E293B" alt="PRIVATE"/> | 국내 단타 전략을 검증하는 프레임워크와 장중 실시간 틱·호가 수집기. 틱은 나중에 받아올 방법이 없어서 그날 놓치면 영원히 없다. **사전등록하고 딱 한 번만 잰다.** 기각된 걸 살리려고 파라미터를 바꾸지 않는다 |
| **quantbox**<br/><img src="https://img.shields.io/badge/PRIVATE-64748B?style=flat-square&labelColor=1E293B" alt="PRIVATE"/> | 바이낸스 USDT-M 선물 브레이크아웃/모멘텀 시스템 — VR 압축 스퀴즈 + MA 클러스터 스퀴즈, 실거래 운용 중. 공개된 `quantbox-engine` 은 여기서 전략만 걷어낸 것이다 |
| **momentum**<br/><img src="https://img.shields.io/badge/PRIVATE-64748B?style=flat-square&labelColor=1E293B" alt="PRIVATE"/> | 미국주식 스크리너. Minervini 추세 템플릿과 VCP 패턴을 DuckDB 캐시 위에 올려 CLI 로 돌린다 |
| **krx-signal-engine**<br/><img src="https://img.shields.io/badge/PRIVATE-64748B?style=flat-square&labelColor=1E293B" alt="PRIVATE"/> | 국내주식(코스피·코스닥) 트레이딩 시스템. DART 공시 리스크 게이트가 ML·감성 신호와 별개로 진입을 막고 중대 공시에서는 강제 청산까지 한다. `quant-airflow` 를 읽기전용으로 조회하고 키움 브로커 어댑터로 주문을 낸다. 미국 시장 뉴스-감성 실험이던 `gpt-quant-v2` 를 국내주식용으로 다시 짰고, 아직 짓는 중이다 — 비용 모델과 리스크 게이트는 실물이지만 백테스트 대상 전략은 아직 자리표시자 스텁이다 |
| **trading_code**<br/><img src="https://img.shields.io/badge/PRIVATE-64748B?style=flat-square&labelColor=1E293B" alt="PRIVATE"/> | 암호화폐 페어 트레이딩 프레임워크의 첫 판. `quantbox` 가 여기서 나왔다 (아카이브) |
| **resume-private**<br/><img src="https://img.shields.io/badge/PRIVATE-64748B?style=flat-square&labelColor=1E293B" alt="PRIVATE"/> | 이력서 비공개 원본 (LaTeX) |

<h3><img src="https://img.shields.io/badge/%F0%9F%96%A5%EF%B8%8F%20%EC%9A%B4%EC%98%81-0F766E?style=for-the-badge&labelColor=1E293B" height="26" alt="운영"/></h3>

여기 적힌 것들은 레포로만 있는 게 아니라 지금도 돌고 있다. **레포는 같이 쓰지만 하는 일이 다른 두 호스트**로 나뉜다. 선을 긋는 규칙은 한 줄이다 — **다시 못 하는 일은 `trader` 에 남고, 다시 돌릴 수 있는 일은 `simnode` 로 간다.** 틱과 호가는 소급 수집이 안 되니 장중 한 시간을 놓치면 영원히 없지만, 실패한 배치는 내일 다시 돌리면 그만이다.

```mermaid
flowchart LR
    subgraph T ["🖥️ trader — 라이브, 24/7"]
        direction TB
        SC["scalp-it<br/>틱·호가 실시간 수집"]
        QB["quantbox"]
        KSE["krx-signal-engine"]
        RP[("TimescaleDB<br/>읽기전용 리플리카")]
    end

    subgraph S ["🖥️ simnode — 재현 가능, 24/7"]
        direction TB
        AF["quant-airflow<br/>스케줄러 · 웹서버"]
        PR[("TimescaleDB<br/>PRIMARY")]
        RS["kr-quant · portfolio-research<br/>macro-sector-agent · momentum<br/>장 마감 후 분석 배치"]
    end

    SC -- "LAN 너머로 틱 기록<br/>재연결 + 디스크 스풀" --> PR
    AF --> PR
    PR -- "스트리밍 복제" --> RP
    PR --> RS

    classDef live fill:#B45309,stroke:#78350F,color:#FFFFFF
    classDef repro fill:#059669,stroke:#065F46,color:#FFFFFF
    classDef store fill:#2563EB,stroke:#1E40AF,color:#FFFFFF

    class SC,QB,KSE live
    class AF,RS repro
    class RP,PR store

    style T fill:#0F172A08,stroke:#64748B
    style S fill:#0F172A08,stroke:#64748B
```

| | **`trader`** — 라이브 머신 | **`simnode`** — 리서치 머신 |
|---|---|---|
| **역할** | 되돌릴 수 없고 시계에 묶인 일 — 장중은 한 번뿐이다 | 다시 돌릴 수 있는 일 — 오케스트레이션·배치·리서치 |
| **도는 것** | `scalp-it` 실시간 틱·호가 수집 · `quantbox` · `krx-signal-engine` · `kiwoom-client` 개발 — 브로커 세션은 키 하나당 하나라 그 세션이 여기 있다 | Airflow 스케줄러·웹서버(16개 DAG) · TimescaleDB **PRIMARY** · `kr-quant`·`portfolio-research`·`macro-sector-agent`·`momentum` · 마감 후 집계 배치 전부 |
| **공유 레포** | `quant-airflow` 와 `kr-quant` 는 **`git sparse-checkout`** 으로만 있다 — 리플리카 compose, 백업 스크립트, 스키마, `.env` 뿐 | 정본 전체 클론 |
| **TimescaleDB** | 읽기전용 스트리밍 리플리카 | PRIMARY — 쓰기는 전부 여기로 |

- **같은 레포가 양쪽에 있다고 양쪽 다 정본인 건 아니다.** 설정 수정은 `simnode` 의 전체 클론에서 하고 push 한다. `trader` 는 pull 만 한다 — sparse checkout 이라 거꾸로 하기가 어렵다.
- **어느 쪽이 PRIMARY 인지는 코드가 아니라 상태다.** `pg_is_in_recovery()` 가 답하고, 그 답은 이미 한 번 뒤집혔다. 처음엔 LAN 순단에 수집기가 죽지 않도록 `trader` 가 PRIMARY 였는데, 수집기에 재연결과 디스크 스풀이 들어가 순단을 스스로 버티는 게 운영에서 확인된 날 `simnode` 로 승격했다. 강등된 쪽은 리플리카로 재구성했다 — compose 파일 이름까지 그대로 둔 채.
- **배치를 옮겨도 시각은 안 옮겼다.** 크론 트리거는 호스트가 아니라 DB 에서 데이터가 확정되는 시점에 맞춰져 있어서, 분리 전후의 스케줄이 똑같이 읽힌다.
- 반대로 **꺼야 했던 것** 하나 — 내려간 DB 컨테이너를 되살리는 헬스 가드다. 그대로 뒀으면 강등된 옛 PRIMARY 를 깨워 split-brain 을 만들었을 것이다. 스크립트 파일은 `trader` 가 다시 PRIMARY 를 맡을 날을 위해 디스크에 남겨뒀다.

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
