import pandas as pd
import os

DATA_TEMP_DIR = r"d:\PersonalProjects\WeatherPredictionAustralia\data\temp"

df = pd.read_csv(os.path.join(DATA_TEMP_DIR, "good_max_min_temp_mean.csv"))
df["Mean_Temperature"] = (df["High_Mean_C"] + df["Low_Mean_C"]) / 2
df.to_csv(os.path.join(DATA_TEMP_DIR, "final_mean_temp.csv"), index=False)

print("Final mean temperature data saved to:", os.path.join(DATA_TEMP_DIR, "final_mean_temp.csv"))
