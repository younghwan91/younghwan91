# younghwan91 — GitHub 프로필 README (PUBLIC)

`main` 푸시 = github.com/younghwan91 첫 화면에 즉시 공개. **(전역 '묻지 않고 진행' 규칙의 예외) 커밋·푸시는 반드시 사용자 확인 후에만 실행한다.**

## 두 판
- `README.md`(영어, 기본) · `README.ko.md`(한국어). 항상 둘 다 같은 커밋에서 고친다.
- 한국어판은 번역이 아니라 한국어로 다시 쓴 글이다 — 번역투·대시 반복을 피한다.

## 공개하지 않는 것 (사용자가 여러 번 걷어낸 것)
- **전략·성과 노출 금지**: 수익률, 엣지·비용 분석 결론, 실험 판정, "숫자가 말하는 것" 류 연구 요약.
  레포는 "무엇을 하는 시스템인가"까지만.
- **하드웨어 사양 금지** — 호스트는 이름만.
- 휴대폰 번호, 회사(현 직장) 내부 정보. 개인 gmail·LinkedIn·GitHub 링크는 공개 OK.

## 사실 출처 — 이 레포 git log 가 아니다
README 는 다른 레포들의 요약이다. 갱신할 때는 각 레포 상태를 직접 확인한다.
- 레포 존재·공개 여부: `gh repo list younghwan91 --limit 100 --json name,visibility,isArchived`
  — README 에 적힌 레포가 전부 아직 존재하는지 대조한다.
- 변경 내용: 로컬 클론 `~/git/<repo>` 의 `git log`, 없으면 `gh api repos/younghwan91/<repo>/commits`.
- 코드에 아직 없는 계획·예정 연결은 그리지 않는다. 각 레포 자기 README 가 하는 말과 어긋나지 않게.
- 레포 개명 시 옛 이름은 흔적 없이 지운다("formerly X" 도 남기지 않는다).

## 다이어그램 (archify — mermaid 쓰지 않는다)
README 플로우차트는 archify 로 만든 SVG 이미지다. 원본은 `docs/diagrams/architecture.{en,ko}.json`,
결과물은 `docs/images/architecture-{en,ko}-{light,dark}.svg`. 고칠 때는 JSON 두 판을 같이 고치고 다시 뽑는다.
```bash
export ARCHIFY_CHROME=~/.cache/ms-playwright/chromium-1255/chrome-linux64/chrome ARCHIFY_CHROME_NO_SANDBOX=1
A=~/.claude/skills/archify/bin/archify.mjs
for l in en ko; do
  node $A finalize dataflow docs/diagrams/architecture.$l.json docs/diagrams/architecture.$l.html --quality showcase --out-dir /tmp/archify-review-$l
  node scripts/export_diagram_svg.mjs docs/diagrams/architecture.$l.html docs/images/architecture-$l
done
```
- puppeteer chrome 은 `libatk` 부재로 안 뜬다. playwright chromium 을 쓰고, AppArmor 가 샌드박스를 막아 `--no-sandbox` 가 필요하다.
- 뽑은 SVG 는 chromium `--screenshot` 으로 PNG 를 떠서 눈으로 확인한다.
