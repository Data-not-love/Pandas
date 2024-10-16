import pandas as pd
import matplotlib.pyplot as plt


air_qlty = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Create Plot/air_quality.csv")

air_qlty.plot.bar(x="datetime",y="station_paris")
plt.show()