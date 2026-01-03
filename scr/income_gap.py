import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
from pathlib import Path
from shapely.geometry import Point

BASE_DIR = Path(__file__).resolve().parent.parent
ZIP_PATH = BASE_DIR / "data" / "peru_regions.zip"
OUT_PATH = BASE_DIR / "heatmaps"

gdf  = gpd.read_file(f"zip://{ZIP_PATH}")
data = pd.read_csv(BASE_DIR / "data" / "income_gap.csv", sep=";")

gdf  = gdf.merge(data, left_on="NOMBDEP", right_on="NOMBDEP", how="left")

bins   = [4.2, 25.7, 28.7, 35.6, 45.2]
labels = ["[4.2-25.7)", "[25.7-28.7)", "[28.7-35.6)", "[35.6-45.2]"]
colors = ["#EFF3FF", "#BDD7E7", "#6BAED6", "#2171B5"]
cmap   = mcolors.ListedColormap(colors)
norm   = mcolors.BoundaryNorm(bins, cmap.N)

legend_patches = [
    mpatches.Patch(
        facecolor=colors[i],
        label=labels[i],
        edgecolor="black",
        linewidth=0.5
    )
    for i in range(len(labels))
]

legend_patches = legend_patches[::-1]

fig, ax = plt.subplots(figsize=(10, 10))

gdf.plot(
    column    = "IncomeGap",
    cmap      = cmap,
    norm      = norm,
    linewidth = 0.8,
    edgecolor = "black",
    ax        = ax
)

ax.set_axis_off()

ax.legend(
    handles=legend_patches,
    title="Income Gap (%)",
    loc="lower left",
    frameon=False,
    fontsize=10,
    title_fontsize=12
)

gdf["label_point"] = gdf.geometry.representative_point()
gdf.loc[gdf["NOMBDEP"] == "CALLAO", "label_point"] = Point(-78, -11.94856)

ax.scatter(
    gdf["label_point"].x,
    gdf["label_point"].y,
    s=750,
    facecolor="white",
    edgecolor="black",
    linewidth=1,
    zorder=3
)

for x, y, val in zip(
    gdf["label_point"].x,
    gdf["label_point"].y,
    gdf["IncomeGap"]
):
    ax.text(
        x, y,
        f"{val:.1f}",
        ha="center",
        va="center",
        fontsize=10,
        color="black",
        zorder=4
    )

out_path = OUT_PATH / "income_gap.png"
plt.savefig(out_path, dpi=300, bbox_inches="tight")
print("Saved map to", out_path)