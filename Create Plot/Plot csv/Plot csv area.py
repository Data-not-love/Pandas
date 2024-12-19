import matplotlib.pyplot as plt
import pandas as pd

air_qlty = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Create Plot/air_quality.csv")

axs = air_qlty.plot.area(figsize=(24, 5), subplots=True)
#plt.show()

# subplot for aera

fig,axs = plt.subplots(figsize=(12, 4))

air_qlty.plot.area(ax=axs)

axs.set_ylabel("NO$_2$ concentration")

axs.set_xlabel("Date")

plt.grid(True, alpha = 0.4)
plt.show()
