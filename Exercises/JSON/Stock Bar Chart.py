import pandas as pd
import matplotlib.pyplot as plt
import json

dataFrame = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Datasets/JSON/Stock/Amazon.json")
covert_json = dataFrame.to_dict(orient="records")
pretty_print_console = json.dumps(covert_json, indent=4)
print(pretty_print_console)

dataFrame.plot.bar(x="Date",y="Close")
plt.show()