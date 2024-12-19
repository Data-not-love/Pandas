import pandas as pd
import matplotlib.pyplot as plt

air_qlty = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Create Plot/air_quality.csv")

air_qlty["station_london"].plot()
plt.grid(True, alpha = 0.5)
plt.show()
