import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# tỷ lệ open với close
dataFrame = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/archive/Google.csv")
dataFrame["Open/Close"] = dataFrame["Open"] / dataFrame["Close"]

dataFrame['Date'] = pd.to_datetime(dataFrame['Date'])
start_date = datetime(2019,1,15)
end_date = datetime(2019,2,3)

wanted_range = (dataFrame["Date"] >= start_date) & (dataFrame['Date'] <= end_date)
dataFrame_filter_range = dataFrame[wanted_range]

dataFrame_filter_range.plot.bar(x = "Date", y = "Open/Close")
plt.xticks(rotation=75)
plt.ylabel("Ratio")
plt.xlabel("Date")
plt.title("Open / Close ratio of GOOGLE stock")
plt.grid(True, alpha = 0.3)
print(len(dataFrame))
plt.show()