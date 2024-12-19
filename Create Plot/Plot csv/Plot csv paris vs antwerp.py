import matplotlib.pyplot as plt
import pandas as pd

air_qlty = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Create Plot/air_quality.csv")
air_qlty.plot.scatter(x="station_paris", y="station_antwerp", alpha =0.5)
plt.grid(True, alpha = 0.5)
plt.show()
