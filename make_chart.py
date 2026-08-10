"""Reproduce the Part 3 line plot from the MicroProject notebook and save it as a PNG.

The plotting code below is the code provided by the DISCOVERY course in Part 3.3 of
the notebook; this script only wraps it so the figure can be written to disk.

Usage: python make_chart.py
"""

import os

import matplotlib

matplotlib.use("Agg")

import pandas as pd

DATA_URL = "https://waf.cs.illinois.edu/discovery/cds-high-school-gpas.csv"
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "gpa-trends.png")

df = pd.read_csv(DATA_URL)

df_wisconsin = df[df.School == "University of Wisconsin-Madison"]
df_michigan = df[df.School == "University of Michigan"]
df_michiganState = df[df.School == "Michigan State"]

x_column = "Year (Fall)"
y_column = ">=3.75"

# --- Course-provided plotting code (Part 3.3 of the notebook) ---
ax = df_wisconsin.plot.line(x=x_column, y=y_column)
df_michigan.plot.line(x=x_column, y=y_column, ax=ax)
df_michiganState.plot.line(x=x_column, y=y_column, ax=ax)

ax.set_ylabel(f"% of Freshman Class with High School GPA {y_column}")
ax.set_title("Trends in High School GPAs among Incoming Freshman Classes")
ax.set_xticks(range(2004, 2024))
ax.set_xticklabels(labels=range(2004, 2024), rotation=90)
ax.legend(["Wisconsin", "Michigan", "Michigan State"])
# --- end course-provided code ---

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
ax.get_figure().savefig(OUTPUT, dpi=200, bbox_inches="tight")
print(f"Saved {OUTPUT}")
