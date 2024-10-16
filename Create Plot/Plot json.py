import pandas as pd
import matplotlib.pyplot as plt
import json


analyzed_json = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Create Plot/air_quality.json") # dataframe
data_frame_to_json = analyzed_json.to_dict(orient="records") # chuyen ve dictionary
json_format = json.dumps(data_frame_to_json, indent=4)
print (json_format)