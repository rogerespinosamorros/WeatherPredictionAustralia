import pandas as pd

BASELINE = 22.6     # Average SST 1991-2020 (source from: http://www.bom.gov.au/cgi-bin/climate/change/timeseries.cgi?graph=sst&area=aus&season=0112&ave_yr=T&ave_period=9120 )

df = pd.read_csv("../../data/seaSurfaceTemperature/aus_SST_anomaly_1991_204.csv")
df["Absolute_SST"] = df["SST_Anomaly"] + BASELINE
df.to_csv("../../data/seaSurfaceTemperature/SST_absolute_1991_2024.csv", index=False)
print(df.head())