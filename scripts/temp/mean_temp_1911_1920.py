import numpy as np
import os
import pandas as pd


folder = "../../data/temp/decades"
results = []

# Loop over all txt files in the folder
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        decade = filename.replace("mean", "").replace(".txt", "")
        values = []
        with open(os.path.join(folder, filename), "r") as f:
            lines = f.readlines()
        data_lines = lines[6:] # ASCII files
        for line in data_lines:
            for val in line.split():
                v = float(val)
                if v != 99999.90:
                    values.append(v)
        mean_temp = np.mean(values)
        results.append({"Decade": decade, "Mean_Temperature": mean_temp})

# Save to CSV
mean_temp_df = pd.DataFrame(results)
mean_temp_df.to_csv("../../data/temp/aus_mean_temp.csv", index=False)
print(mean_temp_df)