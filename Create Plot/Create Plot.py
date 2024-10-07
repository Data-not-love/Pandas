import matplotlib.pyplot as plt
import pandas as pd
air_qlty = pd.read_csv ("F:/3.5 Years/First Year/Python/Pandas/Create Plot/air_quality.csv")
print (air_qlty)

#air_qlty.plot()
#plt.show()


air_qlty["station_london"].plot()

air_qlty.plot.scatter(x="station_london", y="station_paris", alpha=0.5)

air_qlty.plot.box ()

air_qlty.plot.area(figsize=(12, 4), subplots=True)
plt.show()