import pandas as pd


air_quality = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Create Plot/air_quality.csv")

#NO2 concentration of the station in London in mg/m
air_quality["paris_mg_per_cubic"] = air_quality["station_paris"] * 1.882
print (air_quality.head(5))
print (air_quality.tail(3))