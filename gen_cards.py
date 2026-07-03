#!/usr/bin/env python3
"""Generate the static stat/language SVG cards in assets/.

Static SVGs replace github-readme-stats (its shared Vercel instance 503s
under rate limits). Refresh the numbers, then re-run:

    python3 gen_cards.py

Data sources:
- STATS: gh api graphql contributionsCollection (last 12 months)
- LANGS: byte counts across public repos (ats-optimizer crawl-github)
"""
from pathlib import Path

STATS = {
    "contributions": 1230,
    "commits": 169,
    "prs": 97,
    "issues": 27,
    "reviews": 10,
    "as_of": "Jul 2026",
}

# bytes by language, public repos, notebooks/markup/config excluded
LANGS = [
    ("Python", 2_436_494),
    ("Dart", 369_880),
    ("Kotlin", 70_495),
    ("C++", 37_703),
    ("JavaScript", 27_970),
    ("C", 23_043),
]

THEMES = {
    "light": {
        "ink": "#1f2328", "ink2": "#656d76", "accent": "#4f46e5",
        "border": "#d1d9e0", "track": "#eaeef2",
    },
    "dark": {
        "ink": "#e6edf3", "ink2": "#8d96a0", "accent": "#818cf8",
        "border": "#30363d", "track": "#21262d",
    },
}
FONT = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"


def stats_card(t):
    w, h = 464, 200
    tiles = [
        ("Commits", STATS["commits"]),
        ("Pull requests", STATS["prs"]),
        ("Issues", STATS["issues"]),
        ("Reviews", STATS["reviews"]),
    ]
    tile_w = (w - 48) / 4
    tile_svg = ""
    for i, (label, val) in enumerate(tiles):
        x = 24 + i * tile_w
        tile_svg += (
            f'<text x="{x:.0f}" y="150" font-size="20" font-weight="600" '
            f'fill="{t["ink"]}" font-family="{FONT}">{val}</text>'
            f'<text x="{x:.0f}" y="170" font-size="11" fill="{t["ink2"]}" '
            f'font-family="{FONT}">{label}</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="GitHub activity, last 12 months: {STATS['contributions']} contributions">
  <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="8" fill="none" stroke="{t['border']}"/>
  <text x="24" y="38" font-size="13" font-weight="600" fill="{t['ink2']}" font-family="{FONT}">GITHUB ACTIVITY — LAST 12 MONTHS</text>
  <text x="24" y="86" font-size="40" font-weight="700" fill="{t['ink']}" font-family="{FONT}">{STATS['contributions']:,}</text>
  <text x="24" y="106" font-size="12" fill="{t['ink2']}" font-family="{FONT}">contributions · as of {STATS['as_of']}</text>
  <rect x="24" y="118" width="60" height="3" rx="1.5" fill="{t['accent']}"/>
  {tile_svg}
</svg>'''


def langs_card(t):
    w, h = 336, 200
    total = sum(b for _, b in LANGS)
    bar_max = w - 48 - 44  # right gutter for % labels
    rows = ""
    y = 56
    for name, b in LANGS:
        frac = b / total
        bw = max(6, bar_max * frac)
        rows += (
            f'<text x="24" y="{y}" font-size="11" font-weight="600" fill="{t["ink"]}" font-family="{FONT}">{name}</text>'
            f'<rect x="24" y="{y+5}" width="{bar_max}" height="8" rx="4" fill="{t["track"]}"/>'
            f'<rect x="24" y="{y+5}" width="{bw:.1f}" height="8" rx="4" fill="{t["accent"]}"/>'
            f'<text x="{w-24}" y="{y+13}" font-size="11" fill="{t["ink2"]}" font-family="{FONT}" text-anchor="end">{frac*100:.1f}%</text>'
        )
        y += 24
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Top code languages by bytes">
  <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="8" fill="none" stroke="{t['border']}"/>
  <text x="24" y="38" font-size="13" font-weight="600" fill="{t['ink2']}" font-family="{FONT}">TOP LANGUAGES — CODE</text>
  {rows}
</svg>'''


def main():
    out = Path(__file__).parent / "assets"
    out.mkdir(exist_ok=True)
    for mode, t in THEMES.items():
        (out / f"stats-{mode}.svg").write_text(stats_card(t))
        (out / f"langs-{mode}.svg").write_text(langs_card(t))
    print("wrote 4 SVGs to", out)


if __name__ == "__main__":
    main()
