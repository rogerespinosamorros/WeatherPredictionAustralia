import os
import pandas as pd

# Station directories and city names
stations = {
    "adelaideStation": "Adelaide",
    "brisbaneStation": "Brisbane",
    "canberraStation": "Canberra",
    "goldCoastStation": "Gold Coast",
    "melbourneStation": "Melbourne",
    "newcastleStation": "Newcastle",
    "perthStation": "Perth",
    "sidneyStation": "Sydney",  
    "sunshineCoastStation": "Sunshine Coast",
    "wollongongStation": "Wollongong"
}

root = "data/urbanHeatIsland"
summary = []

for folder, city in stations.items():
    file_path = os.path.join(root, folder, f"{folder}.csv")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue

    df = pd.read_csv(file_path)
    if "Date" in df.columns:
        df["Year"] = pd.to_datetime(df["Date"], errors="coerce").dt.year
        max_temp_col = [col for col in df.columns if "Maximum temperature" in col][0]
    else:
        df["Year"] = df["Year"]
        max_temp_col = [col for col in df.columns if "Maximum temperature" in col][0]
        
    # Drop rows with missing temperatures
    df = df.dropna(subset=[max_temp_col])
    df = df[df[max_temp_col] != '']
    df[max_temp_col] = pd.to_numeric(df[max_temp_col], errors="coerce")

    # Years above 1960+
    df = df[df["Year"] >= 1960]

    # Calculate stats
    for year, group in df.groupby("Year"):
        summary.append({
            "Year": int(year),
            "City": city,
            "Mean_Max_Temp": round(group[max_temp_col].mean(), 2),
            "Days_Above_35C": int((group[max_temp_col] > 35).sum())
        })

# Final DataFrame
summary_df = pd.DataFrame(summary).sort_values(["City", "Year"])
summary_df.to_csv("data/urbanHeatIsland/urban_heat_island_annual_summary.csv", index=False)
print("✅ Saved: data/urbanHeatIsland/urban_heat_island_annual_summary.csv")