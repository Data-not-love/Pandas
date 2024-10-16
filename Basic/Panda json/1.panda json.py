import pandas as pd
import json
analyzed_json = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/output.json")

move_data_frame_to_json = analyzed_json.to_dict(orient="records")
pretty_print = json.dumps(move_data_frame_to_json, indent=4)
print("Real-time price data:", pretty_print)


print ( analyzed_json.dtypes)

print (analyzed_json.columns)