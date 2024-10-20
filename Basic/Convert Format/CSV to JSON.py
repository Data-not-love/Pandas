import pandas as pd
import json

input_csv = input("Must end with .csv and use complete path: ")

def reformat_path(file_path):
    re_format_input = ""
    for char in file_path:
        if char == "\\" :
            re_format_input += "/"
        else :
            re_format_input += char
        if len(file_path) == len(re_format_input):
            return re_format_input

reformat_csv = reformat_path(input_csv)
csv_read = pd.read_csv(reformat_csv)
csv_read = csv_read.fillna("NaN")


output_json = input("Use complete path: ")
reformat_output = reformat_path(output_json)
to_json = csv_read.to_dict(orient='records')
with open(reformat_output, 'w') as json_file:
    json.dump(to_json, json_file, indent=5,default=str)
print("SUCCESSFULLY CONVERT THE FILE. PLEASE CHECK")
