# create a unversal condition code for all the different condition codes across the cities
# this will be used for the map and the analysis

import pandas as pd

# for each county, read in the geocoded conditions data, create a new column called universal_condition 
# combine into one single file with an additional column specifying the county


df = pd.read_csv("outputs/charles_city_conditions_coords.csv")

# add a new column called universal_condition and use the following mapping:

condition_mapping = {
    "AVERAGE": "AVERAGE",
    "GOOD": "GOOD",
    "FAIR": "FAIR",
    "MODULAR AVE": "AVERAGE",
    "NaN": "NONE",
    "POOR": "POOR",
    "EXCELLENT": "GOOD",
    "MODULAR GOOD": "GOOD",
    "MODULAR FAIR": "FAIR",
    "MODULAR POOR": "POOR",
    "SINGLEWIDE AVE": "AVERAGE",
    "SINGLEWIDE FAIR": "FAIR"
}
df["universal_condition"] = df["condition_"].map(condition_mapping).fillna("NaN")

# save the new dataframe to a new csv file
df.to_csv("outputs/charles_city_conditions_universal.csv", index=False)



df = pd.read_csv("outputs/dinwiddie_conditions_coords.csv")

# add a new column called universal_condition and use the following mapping:

condition_mapping = {
    "A": "AVERAGE",
    "G": "GOOD",
    "F": "FAIR",
    "NaN": "NONE",
    "P": "POOR",
    "E": "GOOD",
    "VG": "GOOD",
    "VP": "POOR",
    "UN": "NONE",
    "AV": "AVERAGE"
}
df["universal_condition"] = df["mcond"].map(condition_mapping).fillna("NaN")

# save the new dataframe to a new csv file
df.to_csv("outputs/dinwiddie_conditions_universal.csv", index=False)



df = pd.read_csv("outputs/emporia_conditions_coords.csv")

# add a new column called universal_condition and use the following mapping:

condition_mapping = {
    "AVERAGE": "AVERAGE",
    "AV/FAIR": "AVERAGE",
    "FAIR": "FAIR",
    "FAIR/POOR": "FAIR",
    "AV/GD": "GOOD",
    "POOR": "POOR",
    "GOOD": "GOOD",
    "NaN": "NONE"

}
df["universal_condition"] = df["extrcond"].map(condition_mapping).fillna("NaN")

# save the new dataframe to a new csv file
df.to_csv("outputs/emporia_conditions_universal.csv", index=False)


df = pd.read_csv("outputs/hopewell_conditions_coords.csv")

# add a new column called universal_condition and use the following mapping:

condition_mapping = {
    "AV": "AVERAGE",
    "G": "GOOD",
    "F": "FAIR",
    "NaN": "NONE",
    "P": "POOR",
    "VP": "POOR"

}
df["universal_condition"] = df["condcode"].map(condition_mapping).fillna("NaN")

# save the new dataframe to a new csv file
df.to_csv("outputs/hopewell_conditions_universal.csv", index=False)


df = pd.read_csv("outputs/petersburg_conditions_coords.csv")

# add a new column called universal_condition and use the following mapping:

condition_mapping = {
    3: "AVERAGE",
    4: "GOOD",
    2: "FAIR",
    "NaN": "NONE",
    1: "POOR",
    5: "GOOD"

}
df["universal_condition"] = df["quality"].map(condition_mapping).fillna("NaN")

# save the new dataframe to a new csv file
df.to_csv("outputs/petersburg_conditions_universal.csv", index=False)