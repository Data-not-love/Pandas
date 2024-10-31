import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
air_quality = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Create Plot/air_quality.csv")

air_quality_renamed = air_quality.rename(
    columns={
    "station_paris" : "Paris Air Quality",
    "station_antwerp" : "Antwerp Air Quality"
    }
)
print (air_quality_renamed.iloc[34:39])
# NO2 concentration of the station in London in mg/m
air_quality["paris_mg_per_cubic"] = air_quality["station_paris"] * 1.882
print (air_quality[["datetime","paris_mg_per_cubic","station_paris"]].head(5))


air_quality["paris/london"] = air_quality["station_paris"] / air_quality["station_london"]
print (air_quality[["datetime","station_paris","station_london","paris/london"]].iloc[245:250])


# khi đã thêm cột vào data frame => thành thuộc tính của dataframe
air_quality.plot.bar(x="datetime",y="paris/london")
plt.xticks(np.arange(0, len(air_quality), step=30),rotation=75)
plt.title("Paris / London Ratio")
plt.grid(True, alpha = 0.3)
plt.show()