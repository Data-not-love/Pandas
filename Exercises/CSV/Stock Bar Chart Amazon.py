import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# hiện giá open từ lúc niêm yết đến hiện tại
dataFrame = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/archive/Amazon.csv")

dataFrame.plot.bar(x="Date",y="Open")
plt.xticks(np.arange(0, len(dataFrame), step=100),rotation=75)

plt.show()