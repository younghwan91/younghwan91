"""프로필 README 히어로 콜라주 — 각 레포의 docs/images/hero-{light,dark}.png 네 장을 2×2 로 합친다.

실행 (이 레포 루트에서):
    uv run --with matplotlib --with pillow python scripts/make_hero_collage.py [--repos-dir ~/git]
→ docs/images/hero-light.png, docs/images/hero-dark.png
각 레포의 그림은 그 레포 scripts/make_hero.py 가 만든다. 여기서는 합치기만 한다.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from hero_style import P, render_both  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
from PIL import Image  # noqa: E402

# (레포, 칸 제목) — 순서 = 읽는 순서. 시장 구조 사실 → 도구 → 엔진.
TILES = [
    ("macro-sector-agent", "Which US industry has been forgotten?"),
    ("quant-airflow", "31% of stocks that ever traded are delisted — and stay in the data"),
    ("krx-quant-core", "KRX price limits are not symmetric"),
    ("swing-it", "Pure noise passes \u201c5 of 6 folds\u201d about half the time"),
]
ASPECT = 2.05
COLS, ROWS = 2, 2


def _load(repos: pathlib.Path, repo: str, mode: str, surface: str) -> Image.Image:
    img = Image.open(repos / repo / "docs" / "images" / f"hero-{mode}.png").convert("RGB")
    w, h = img.size
    tw, th = (w, round(w / ASPECT)) if w / h > ASPECT else (round(h * ASPECT), h)
    canvas = Image.new("RGB", (tw, th), surface)
    canvas.paste(img, ((tw - w) // 2, (th - h) // 2))
    return canvas


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos-dir", default="~/git")
    args = ap.parse_args()
    repos = pathlib.Path(args.repos_dir).expanduser()

    def draw(fig, axes, p):
        mode = "light" if p is P["light"] else "dark"
        fig.subplots_adjust(left=0.01, right=0.99, top=0.955, bottom=0.01, wspace=0.025, hspace=0.11)
        for ax, (repo, title) in zip(axes.flat, TILES):
            ax.imshow(_load(repos, repo, mode, p["surface"]))
            ax.set_title(f"{repo}  ·  {title}", fontsize=12, color=p["ink2"], loc="left", pad=4)
            ax.axis("off")
            for s in ax.spines.values():
                s.set_visible(False)
            ax.add_patch(plt.Rectangle((0, 0), 1, 1, transform=ax.transAxes, fill=False,
                                       edgecolor=p["grid"], linewidth=1))

    tile_w = 14 / COLS
    fig_h = ROWS * tile_w / ASPECT + 0.9  # 타일 높이 + 제목 줄
    render_both(draw, out_dir="docs/images", name="hero", figsize=(14, fig_h), nrows=ROWS, ncols=COLS)


if __name__ == "__main__":
    main()
