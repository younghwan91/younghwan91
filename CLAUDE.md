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

## 다른 레포의 "관련 프로젝트" 푸터
- `stack.yml` 이 단일 원천. 각 레포 README 푸터를 손으로 고치지 않는다. 설명에 숫자를 쓰지 않는다.
- 표류 검사: `python3 scripts/sync_stack_footer.py ~/git --check` (종료코드 1 = 표류 있음)
- 주입은 `--check` 없이 — **다른 레포 README 를 직접 고친다.** 다른 작업 트리를 건드리므로 실행 전 사용자 확인 필수.

## mermaid
로컬 렌더 검증 수단이 없다(2026-10-12: puppeteer chrome 이 `libatk` 부재로 안 뜸). 문법을 눈으로 확인하고,
푸시 후 github.com/younghwan91 에서 다이어그램이 뜨는지 사용자에게 확인을 부탁한다고 보고에 적는다.
