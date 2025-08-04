import calendar
from pathlib import Path

meses = list(calendar.month_name[1:])

for i, mes in enumerate(meses):
    Path(f"2025/{i+1}. {mes}").mkdir(parents=True, exist_ok=True)