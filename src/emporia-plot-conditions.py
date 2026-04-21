import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# Download Virginia county shapefile directly from Census
counties = gpd.read_file(
    "data/tl_2025_us_county.zip"
)
# Filter to Virginia (FIPS code 51)
target_counties = ["Emporia"]
va_counties = counties[(counties["STATEFP"] == "51") & (counties["NAME"].isin(target_counties))]

# read in the geocoded Emporia conditions data
df = pd.read_csv("outputs/emporia_conditions_coords.csv")

# plot them with different colors
condition_colors = {
    "AVERAGE": "blue",
    "AV/FAIR": "lightblue",
    "FAIR": "yellow",
    "FAIR/POOR": "orange",
    "AV/GD": "lightgreen",
    "POOR": "red",
    "GOOD": "green",
    "NaN": "gray"
}
df["color"] = df["extrcond"].map(condition_colors).fillna("gray")

#print the number of dots in each condition category
print(df["extrcond"].value_counts())


fig, ax = plt.subplots(figsize=(15, 15))
va_counties.boundary.plot(ax=ax, color="black", linewidth=0.5)
#fill the counties with a light color
va_counties.plot(ax=ax, color="lightgray", alpha=0.5)
# make the dots smaller
df.plot.scatter(x="lng", y="lat", c="color", ax=ax, legend=True, s=10)
#add a key for the colors
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in condition_colors.values()]
labels = condition_colors.keys()
ax.legend(handles, labels, title="Condition", loc="upper right")
ax.set_title("Emporia Residential Conditions")
ax.set_axis_off()
plt.tight_layout()

plt.show(block=True)