import pandas as pd
import json

input_csv = input("Must end with .csv and use complete path: ")

def reformat_path (str):
    re_format_input = ""
    for char in str:
        if char == "\\" :
            re_format_input += "/"
        else :
            re_format_input += char
        if len(str) == len(re_format_input):
            return re_format_input

reformat_csv = reformat_path(input_csv)
csv_read = pd.read_csv(reformat_csv)
csv_read = csv_read.fillna("NaN")

# ko thể làm việc với datetime của json
if 'datetime' in csv_read.columns:
    csv_read['datetime'] = pd.to_datetime(csv_read['datetime']).dt.strftime('%Y-%m-%dT%H:%M:%S')

output_json = input("Use complete path: ")
reformat_output = reformat_path(output_json)
to_json = csv_read.to_dict(orient='records')
with open(reformat_output, 'w') as json_file:
    json.dump(to_json, json_file, indent=5)
print("Can upgrade")