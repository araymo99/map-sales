# create a histogram of sale prices in 2024 in Nelson County, VA
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/TJPDC-sales.csv")
# only keep sales in Nelson County
df = df[df["CityCounty"] == "Nelson County"]
plt.figure(figsize=(10, 10))

# make the bins be $50,000 wide, starting from $0 up to the max sale price rounded up to the nearest $50,000
max_price = df["Sold Price"].max()
bins = range(0, int(max_price) + 5000, 5000)

plt.hist(df["Sold Price"], bins=bins, color="skyblue", edgecolor="skyblue")
plt.title("Distribution of Sale Prices in Nelson County (2024)")

# make the x-axis labels be in $500,000 increments, with a $ sign and K for thousands, and X.XM for millions
plt.xticks(range(0, int(max_price) + 500000, 500000), [f"${x//1000}K" if x < 1000000 else f"${x/1000000:.1f}M" for x in range(0, int(max_price) + 500000, 500000)])

# put a vertical line at the price $426250
plt.axvline(x=426250, color="red", linestyle="--", label="Median Price ($426K)")
plt.legend()

plt.xlabel("Sale Price")
plt.ylabel("Number of Sales")
plt.grid(axis="y", alpha=0.75)
plt.tight_layout()
plt.savefig("outputs/nelson_price_histogram.png", dpi=150)
plt.show()


#print the maximum sale price in the data
print(f"Maximum sale price in Nelson County (2024): ${max_price:,.2f}")
#print total number of sales
total_sales = df["Sold Price"].count()
print(f"Total sales in Nelson County (2024): {total_sales}")
#print the number of sales below $500k
sales_below_500k = df[df["Sold Price"] < 500000].shape[0]
print(f"Number of sales below $500k in Nelson County (2024): {sales_below_500k}")
#print the number of sales above 1 million
sales_above_1m = df[df["Sold Price"] > 1000000].shape[0]
print(f"Number of sales above $1M in Nelson County (2024): {sales_above_1m}")