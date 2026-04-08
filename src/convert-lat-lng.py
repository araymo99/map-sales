import pandas as pd
import censusgeocode as cg
import math

df = pd.read_csv("data/sale-address-2024.csv")

# Census batch API needs: unique ID, street, city, state, zip
# Build a properly formatted dataframe for it
census_input = pd.DataFrame({
    "id":     df.index,
    "street": df["Property Address"],
    "city":   df["City"],
    "state":  "VA",      
    "zip":    df["Zipcode"]
})


chunk_size = 1000
all_results = []


for i in range(0, len(census_input), chunk_size):
    chunk = census_input.iloc[i:i+chunk_size]
    
    # Save chunk to a temp CSV file, then pass the path
    chunk.to_csv("outputs/temp_chunk.csv", index=False, header=False)
    result = cg.addressbatch("outputs/temp_chunk.csv")
    
    all_results.extend(result)
    print(f"Processed {min(i+chunk_size, len(df))}/{len(df)}")

results_df = pd.DataFrame(all_results)
results_df = pd.DataFrame(all_results)
results_df.to_csv("outputs/raw_results.csv", index=False)  # add this
print(results_df.columns.tolist())                  # add this

# Merge lat/lng back onto your original data
df["lat"] = pd.to_numeric(results_df["lat"],  errors="coerce")
df["lng"] = pd.to_numeric(results_df["lon"], errors="coerce")

# See how many failed to geocode
failed = df["lat"].isna().sum()
print(f"Geocoded {len(df) - failed}/{len(df)} addresses. {failed} failed.")

df.to_csv("data/sales_with_coords.csv", index=False)