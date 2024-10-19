import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# tỷ lệ open với close
dataFrame = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/archive/Google.csv")
dataFrame["Open/Close"] = dataFrame["Open"] / dataFrame["Close"]
dataFrame.plot.bar(x = "Date", y ="Open/Close")
plt.xticks(np.arange(0, len(dataFrame), step=500),rotation=75)
print(len(dataFrame))
plt.show()