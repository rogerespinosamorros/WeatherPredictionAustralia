import os
import pandas as pd

# Base path for data files
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
INV_PATH = os.path.join(BASE_DIR, "data", "station.metadata.location.inv")
DAT_PATH = os.path.join(BASE_DIR, "data", "monthly.temperature.dat")


# Load AU station data (stations)
stations = {}
with open(INV_PATH) as f:
    for line in f:
        station_id = line[0:11]
        country = line[38:40]
        if country == "AU":
            stations[station_id] = {
                "latitude": float(line[12:20]),
                "longitude": float(line[21:30]),
                "name": line[41:].strip()
            }
print(f"Found {len(stations)} station in Australia")

# Parse dat. file for AU station temps
rows = []
with open(DAT_PATH) as f:
    for line in f:
        station_id = line[0:11]
        year = int(line[11:15])
        if station_id not in stations:
            continue
        for month in range(12):
            val = line[19 + month * 8 : 24 + month * 8].strip()
            if val == "" or val == "-9999":
                continue
            try:
                temp_celsius = int(val) / 100
                rows.append({
                    "station": station_id,
                    "year": year,
                    "month": month + 1,
                    "temp": temp_celsius
                })
            except ValueError:
                continue

df = pd.DataFrame(rows)

# Filter station-years with at least 10 months of data
counts = df.groupby(["station", "year"])["month"].count().reset_index(name="count")
valid = counts[counts["count"]>= 10]
df = df.merge(valid[["station", "year"]], on=["station", "year"])

# Compute per station annual mean temperature
annual_per_station = df.groupby(["station", "year"])["temp"].mean().reset_index()

# Compute national annual mean temperature
annual_national = annual_per_station.groupby("year")["temp"].mean().reset_index()
annual_national.columns = ["Year", "Australia Mean Temp (°C)"]

# Save output
output_path = os.path.join(BASE_DIR, "data", "australia_annual_mean_temp_clean.csv")
annual_national.to_csv(output_path, index=False)
print(f"Saved cleaned dataset to: {output_path}")
