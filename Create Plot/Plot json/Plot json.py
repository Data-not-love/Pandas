import pandas as pd
from datetime import datetime
import json
# dùng datetime để xử lý các thuộc tính datetime

analyzed_json = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Create Plot/air_quality.json") # dataframe
data_frame_to_json = analyzed_json.to_dict(orient="records")  # chuyen ve dictionary
json_format = json.dumps(data_frame_to_json, default=str, indent=4)
print (json_format)


