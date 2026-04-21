import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# Download Virginia county shapefile directly from Census
counties = gpd.read_file(
    "data/tl_2025_us_county.zip"
)
# Filter to Virginia (FIPS code 51)
target_counties = ["Charles City", "Dinwiddie","Emporia", "Hopewell", "Petersburg"]
va_counties = counties[(counties["STATEFP"] == "51") & (counties["NAME"].isin(target_counties))]

# read in the geocoded universal conditions data for each county and combine into one dataframe
charles_city = pd.read_csv("outputs/charles_city_conditions_universal.csv")
charles_city["county"] = "Charles City"

dinwiddie = pd.read_csv("outputs/dinwiddie_conditions_universal.csv")
dinwiddie["county"] = "Dinwiddie"

emporia = pd.read_csv("outputs/emporia_conditions_universal.csv")
emporia["county"] = "Emporia"


hopewell = pd.read_csv("outputs/hopewell_conditions_universal.csv")
hopewell["county"] = "Hopewell"

petersburg = pd.read_csv("outputs/petersburg_conditions_universal.csv")
petersburg["county"] = "Petersburg"

# combine all dataframes into one
df = pd.concat([charles_city, dinwiddie, emporia, hopewell, petersburg], ignore_index=True)

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lng, df.lat))


# specify colors for each condition category
# and simply dont put a dot for NONE

condition_colors = {

    "GOOD": "green",
    "AVERAGE": "yellow",
    "FAIR": "orange",
    "POOR": "red",
}



# drop NONE explicitly if you don’t want to plot it
gdf_plot = gdf[gdf["universal_condition"].isin(condition_colors.keys())].copy()

# map colors
gdf_plot["color"] = gdf_plot["universal_condition"].map(condition_colors)

# plot
fig, ax = plt.subplots(figsize=(10, 10))
va_counties.plot(ax=ax, color="whitesmoke", edgecolor="black")

gdf_plot.plot(
    ax=ax,
    color=gdf_plot["color"],
    markersize=5,
    alpha=0.6
)

plt.title("Residential Building Conditions in Crater PDC")
#plt.show()


# now plot emporia only, plot fair and poor only

emporia_gdf = gdf[gdf["county"] == "Emporia"].copy()
emporia_gdf = emporia_gdf[emporia_gdf["universal_condition"].isin(["FAIR", "POOR"])].copy()
emporia_gdf["color"] = emporia_gdf["universal_condition"].map(condition_colors)
fig, ax = plt.subplots(figsize=(10, 10))
va_counties[va_counties["NAME"] == "Emporia"].plot(ax=ax, color="whitesmoke", edgecolor="black")
emporia_gdf.plot(
    ax=ax,
    color=emporia_gdf["color"],
    markersize=60,
    alpha=0.7
)
plt.title("Fair and Poor Residential Building Conditions in Emporia")
#plt.show()

# now plot charles city only

charles_city_gdf = gdf[gdf["county"] == "Charles City"].copy()
charles_city_gdf = charles_city_gdf[charles_city_gdf["universal_condition"].isin(condition_colors.keys())].copy()
charles_city_gdf["color"] = charles_city_gdf["universal_condition"].map(condition_colors)
fig, ax = plt.subplots(figsize=(10, 10))
va_counties[va_counties["NAME"] == "Charles City"].plot(ax=ax, color="whitesmoke", edgecolor="black")
charles_city_gdf.plot(
    ax=ax,
    color=charles_city_gdf["color"],
    markersize=60,
    alpha=0.7
)
plt.title("Residential Building Conditions in Charles City")
#plt.show()

# now plot charles city only, plot fair and poor only

charles_city_gdf = gdf[gdf["county"] == "Charles City"].copy()
charles_city_gdf = charles_city_gdf[charles_city_gdf["universal_condition"].isin(["FAIR", "POOR"])].copy()
charles_city_gdf["color"] = charles_city_gdf["universal_condition"].map(condition_colors)
fig, ax = plt.subplots(figsize=(10, 10))
va_counties[va_counties["NAME"] == "Charles City"].plot(ax=ax, color="whitesmoke", edgecolor="black")
charles_city_gdf.plot(
    ax=ax,
    color=charles_city_gdf["color"],
    markersize=60,
    alpha=0.7
)
plt.title("Fair and Poor Residential Building Conditions in Charles City")
#plt.show()


# now plot dinwiddie only, plot fair and poor only

dinwiddie_gdf = gdf[gdf["county"] == "Dinwiddie"].copy()
dinwiddie_gdf = dinwiddie_gdf[dinwiddie_gdf["universal_condition"].isin(["FAIR", "POOR"])].copy()
dinwiddie_gdf["color"] = dinwiddie_gdf["universal_condition"].map(condition_colors)
fig, ax = plt.subplots(figsize=(10, 10))
va_counties[va_counties["NAME"] == "Dinwiddie"].plot(ax=ax, color="whitesmoke", edgecolor="black")
dinwiddie_gdf.plot(
    ax=ax,
    color=dinwiddie_gdf["color"],
    markersize=60,
    alpha=0.7
)
plt.title("Fair and Poor Residential Building Conditions in Dinwiddie")
#plt.show()

# now plot hopewell only, plot fair and poor only

hopewell_gdf = gdf[gdf["county"] == "Hopewell"].copy()
hopewell_gdf = hopewell_gdf[hopewell_gdf["universal_condition"].isin(["FAIR", "POOR"])].copy()
hopewell_gdf["color"] = hopewell_gdf["universal_condition"].map(condition_colors)
fig, ax = plt.subplots(figsize=(10, 10))
va_counties[va_counties["NAME"] == "Hopewell"].plot(ax=ax, color="whitesmoke", edgecolor="black")
hopewell_gdf.plot(
    ax=ax,
    color=hopewell_gdf["color"],
    markersize=60,
    alpha=0.7
)
plt.title("Fair and Poor Residential Building Conditions in Hopewell")
#plt.show()

# now plot petersburg only, plot fair and poor only

petersburg_gdf = gdf[gdf["county"] == "Petersburg"].copy()
petersburg_gdf = petersburg_gdf[petersburg_gdf["universal_condition"].isin(["FAIR", "POOR"])].copy()
petersburg_gdf["color"] = petersburg_gdf["universal_condition"].map(condition_colors)
fig, ax = plt.subplots(figsize=(10, 10))
va_counties[va_counties["NAME"] == "Petersburg"].plot(ax=ax, color="whitesmoke", edgecolor="black")
petersburg_gdf.plot(
    ax=ax,
    color=petersburg_gdf["color"],
    markersize=60,
    alpha=0.7
)
plt.title("Fair and Poor Residential Building Conditions in Petersburg")
plt.show()