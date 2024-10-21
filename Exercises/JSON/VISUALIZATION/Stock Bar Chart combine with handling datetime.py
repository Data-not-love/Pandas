import pandas as pd
import matplotlib.pyplot as plt
import json
from datetime import datetime



dataFrame = pd.read_json("/Datasets/JSON/Stock/Amazon.json")
covert_json = dataFrame.to_dict(orient="records")
pretty_print_console = json.dumps(covert_json, default=str,indent=4)
print(pretty_print_console)

start_day = datetime(2020,8,1,00,00,00)
end_day = datetime(2020,8,14,00,00,00)


day_range = (dataFrame["Date"] >= start_day) & (dataFrame["Date"] <= end_day)
dtFrame_range = dataFrame[day_range].copy()


dtFrame_range.plot.bar(x="Date",y="Close")


plt.xticks(rotation=45)
plt.show()