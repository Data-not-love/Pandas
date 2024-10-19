import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

dtFrame = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/archive/Netflix.csv")
print (len(dtFrame))

# convert datafarme qua datetime
dtFrame["Date"]= pd.to_datetime(dtFrame["Date"])

start_date = datetime(2004, 7,1)
end_date = datetime(2004,7,30)

range = (dtFrame["Date"] >= start_date) & (dtFrame["Date"] <= end_date)

dfRange = dtFrame[range]

dfRange.plot.bar(x="Date",y="High")
plt.xticks(rotation=75)
plt.grid(True)
plt.xlabel("Trading dates in July")
plt.ylabel("High Price ($)")
plt.show()