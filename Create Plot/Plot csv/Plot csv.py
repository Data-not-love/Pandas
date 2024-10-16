import matplotlib.pyplot as plt
import pandas as pd


# ko khí của 3 trạm

air_qlty = pd.read_csv ("F:/3.5 Years/First Year/Python/Pandas/Create Plot/air_quality.csv", index_col=0, parse_dates=True)
print(air_qlty.tail(5))

air_qlty.plot()
plt.show()


