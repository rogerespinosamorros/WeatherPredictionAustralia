import pandas as pd
import os

DATA_DIR = r"d:\PersonalProjects\WeatherPredictionAustralia\data"
SUBFOLDER = "floods&cyclones"
FILENAME = "Flood_Cyclones_Events.csv"

output_dir = os.path.join(DATA_DIR, SUBFOLDER)
os.makedirs(output_dir, exist_ok=True)

# Flood and cyclone data from 2001 to 2022, where "1" it's a major flood event
data = {
    "Year": list(range(2001, 2023)),
    "Major_Flood_Event": [
        0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
        1, 0, 0, 1, 0, 0, 1, 0, 0, 0,
        1, 1
    ],
    "Cyclone_Landfalls": [
        5, 4, 6, 4, 3, 2, 6, 5, 4, 3,
        4, 3, 5, 4, 3, 5, 4, 4, 3, 5,
        4, 5
    ]
}

df = pd.DataFrame(data)

output_path = os.path.join(output_dir, FILENAME)
df.to_csv(os.path.join(DATA_DIR, "floods&cyclones", "Flood_Cyclones_Events.csv"))
print(f"✅ File saved to {output_path}")