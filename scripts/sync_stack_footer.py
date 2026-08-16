#!/usr/bin/env python3
"""stack.yml 에서 각 레포 README 의 "관련 프로젝트" 푸터를 생성해 주입한다.

푸터를 8개 레포에 손으로 복사해 둔 결과 한 레포의 사실이 바뀌어도 나머지가
따라가지 못했다("207개 엔드포인트"가 실제 186 으로 바뀐 뒤에도 7개 레포에 남았다).
이 스크립트가 단일 소스에서 생성하므로 그 표류가 구조적으로 생기지 않는다.

사용법:
    python scripts/sync_stack_footer.py ~/Documents/git          # 주입
    python scripts/sync_stack_footer.py ~/Documents/git --check  # 표류 검사만 (CI 용)

인자는 레포 클론들이 나란히 들어있는 디렉터리다. 없는 레포는 건너뛴다.
표준 라이브러리만 쓴다(PyYAML 불필요 — stack.yml 의 부분집합만 파싱).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HEADING = re.compile(r"^##\s+(관련 프로젝트|Related projects)\b.*$", re.MULTILINE)
NEXT_HEADING = re.compile(r"^##\s+", re.MULTILINE)

# 언어는 파일명이 아니라 기존 푸터 헤딩으로 판정한다. opt_portfolio 처럼
# README.md 가 영문이고 README.ko.md 가 한국어인 레포가 있어서, 파일명 규칙은
# 믿을 수 없다. 헤딩 문구는 그 문서 자체의 언어이므로 항상 맞다.
LANG_BY_HEADING = {"관련 프로젝트": "ko", "Related projects": "en"}

TITLE = {
    "ko": "## 관련 프로젝트 — 오픈소스 퀀트 스택",
    "en": "## Related projects — open-source quant stack",
}
INTRO = {
    "ko": "한국·미국 주식과 암호화폐를 아우르는 오픈소스 스택입니다. 각 저장소는 독립적으로 쓸 수 있습니다.",
    "en": "Part of an open-source stack spanning Korean equities, US equities and crypto. Each repository stands on its own.",
}
COLUMNS = {
    "ko": ("축", "프로젝트", "설명"),
    "en": ("Market", "Project", "What it is"),
}


def parse_stack(path: Path) -> tuple[dict, list[dict]]:
    """stack.yml 에서 axes / repos 를 읽는다 (이 파일의 고정된 형태만 지원)."""
    axes: dict[str, dict] = {}
    repos: list[dict] = []
    section = None
    current: dict | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line == "axes:":
            section = "axes"
            continue
        if line == "repos:":
            section = "repos"
            continue

        if section == "axes":
            m = re.match(r"^\s{2}(\w+):\s*\{(.+)\}\s*$", line)
            if m:
                key, body = m.group(1), m.group(2)
                fields = dict(
                    (k.strip(), v.strip().strip('"'))
                    for k, v in (p.split(":", 1) for p in re.findall(r'\w+:\s*"[^"]*"', body))
                )
                axes[key] = fields
        elif section == "repos":
            m = re.match(r"^\s{2}-\s+name:\s*(\S+)\s*$", line)
            if m:
                current = {"name": m.group(1)}
                repos.append(current)
                continue
            m = re.match(r'^\s{4}(\w+):\s*"?(.*?)"?\s*$', line)
            if m and current is not None:
                current[m.group(1)] = m.group(2)

    return axes, repos


def render(axes: dict, repos: list[dict], lang: str, self_name: str) -> str:
    order = {"kr": 0, "us": 1, "cx": 2}
    rows = sorted(
        (r for r in repos if r["name"] != self_name),
        key=lambda r: (order.get(r["axis"], 9), repos.index(r)),
    )
    c = COLUMNS[lang]
    out = [TITLE[lang], "", INTRO[lang], "", f"| {c[0]} | {c[1]} | {c[2]} |", "|---|---|---|"]
    for r in rows:
        axis = axes[r["axis"]]
        mark = f"{axis['mark']} {axis[lang]}"
        link = f"**[{r['name']}](https://github.com/younghwan91/{r['name']})**"
        out.append(f"| {mark} | {link} | {r[lang]} |")
    return "\n".join(out) + "\n"


def replace_block(text: str, make_block) -> str | None:
    """기존 푸터 섹션(다음 ## 직전까지)을 갈아끼운다. 못 찾으면 None.

    make_block(lang) 는 해당 문서의 언어로 푸터를 만들어 돌려준다.
    """
    m = HEADING.search(text)
    if not m:
        return None
    lang = LANG_BY_HEADING.get(m.group(1))
    if lang is None:
        return None
    tail = NEXT_HEADING.search(text, m.end())
    end = tail.start() if tail else len(text)
    return text[: m.start()] + make_block(lang) + "\n" + text[end:]


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    base = Path(sys.argv[1]).expanduser()
    check_only = "--check" in sys.argv[2:]

    root = Path(__file__).resolve().parent.parent
    axes, repos = parse_stack(root / "stack.yml")

    drifted, written, missing = [], [], []
    for r in repos:
        repo_dir = base / r["name"]
        if not repo_dir.is_dir():
            missing.append(r["name"])
            continue
        for path in sorted(repo_dir.glob("README*.md")):
            text = path.read_text(encoding="utf-8")
            updated = replace_block(text, lambda lang: render(axes, repos, lang, r["name"]))
            if updated is None or updated == text:
                continue
            rel = f"{r['name']}/{path.name}"
            drifted.append(rel)
            if not check_only:
                path.write_text(updated, encoding="utf-8")
                written.append(rel)

    if missing:
        print(f"건너뜀(클론 없음): {', '.join(missing)}")
    if check_only:
        if drifted:
            print("푸터 표류:\n  " + "\n  ".join(drifted))
            return 1
        print("푸터 동기 상태 — 표류 없음")
        return 0
    print(f"갱신 {len(written)}개" + ("\n  " + "\n  ".join(written) if written else " (변경 없음)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
