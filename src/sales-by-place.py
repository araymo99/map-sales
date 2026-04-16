

# load data/sale-address-2024.csv
# print the counts of sales by city
import pandas as pd
df = pd.read_csv("data/sale-address-2024.csv")

#only keep sales in Fluvanna County
df = df[df["CityCounty"] == "Fluvanna County"]


# in one line, print the city, the zipcode, and the number of sales in that city, sorted by number of sales
print(df.groupby(["City", "Zipcode"]).size().reset_index(name="Sales Count").sort_values("Sales Count", ascending=False))