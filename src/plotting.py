import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

df = pd.read_csv("data/sales_with_coords.csv").dropna(subset=["lat", "lng"])

# Download Virginia county shapefile directly from Census
counties = gpd.read_file(
    "data/tl_2025_us_county.zip"
)

# Filter to Virginia (FIPS code 51)
target_counties = ["Albemarle", "Charlottesville", "Louisa", "Fluvanna", "Nelson", "Greene"]
#target_counties = ["Fluvanna"]
va_counties = counties[(counties["STATEFP"] == "51") & (counties["NAME"].isin(target_counties))]


fig, ax = plt.subplots(figsize=(12, 8))

# Plot county outlines
va_counties.plot(ax=ax, color="whitesmoke", edgecolor="gray", linewidth=0.5)
#make Fluvanna county a different color
va_counties[va_counties["NAME"] == "Fluvanna"].plot(ax=ax, color="lightblue", edgecolor="gray", linewidth=0.5)

# Plot sales dots on top
ax.scatter(df["lng"], df["lat"], s=10, color="blue", alpha=0.6, zorder=5)

ax.set_title("TJPDC Home Sales in 2024")
ax.set_axis_off()
plt.tight_layout()
plt.savefig("outputs/sales_map.png", dpi=150)
plt.show()