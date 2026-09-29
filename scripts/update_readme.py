"""각 사람 폴더(lv* 하위)를 스캔해 README의 진행 현황 표를 갱신한다."""
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START, END = "<!-- STATUS:START -->", "<!-- STATUS:END -->"


def added_date(path: Path) -> str:
    out = subprocess.run(
        ["git", "log", "--diff-filter=A", "--format=%as", "--", str(path)],
        cwd=ROOT, capture_output=True, text=True,
    ).stdout.split()
    return out[-1] if out else "-"


people = sorted(
    d.name for d in ROOT.iterdir()
    if d.is_dir() and not d.name.startswith(".") and any(d.glob("lv*"))
)

table = defaultdict(lambda: defaultdict(list))  # date -> person -> [problem no]
totals = {p: 0 for p in people}
for p in people:
    for f in sorted((ROOT / p).glob("lv*/*")):
        if f.name.startswith("."):
            continue
        num = re.match(r"(\d+)", f.name)
        table[added_date(f)][p].append(num.group(1) if num else f.stem)
        totals[p] += 1

lines = ["| 날짜 | " + " | ".join(people) + " |", "|---|" + "---|" * len(people)]
for date in sorted(table, reverse=True):
    lines.append(f"| {date} | " + " | ".join(", ".join(table[date].get(p, [])) or "-" for p in people) + " |")
lines.append("| **총합** | " + " | ".join(f"**{totals[p]}**" for p in people) + " |")

readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
block = f"{START}\n" + "\n".join(lines) + f"\n{END}"
readme.write_text(re.sub(f"{START}.*?{END}", block, text, flags=re.S), encoding="utf-8")
