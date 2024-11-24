import pandas as pd
import json

input_json = input("Must end with .csv and use complete path: ")

def reformat_path(file_path):
    re_format_input = ""
    for char in file_path:
        if char == "\\" :
            re_format_input += "/"
        else :
            re_format_input += char
        if len(file_path) == len(re_format_input):
            return re_format_input

reformat_json = reformat_path(input_json)
json_read = pd.read_json(reformat_json)
json_read = json_read.fillna("NaN")


output_csv = input("Use complete path and end with .csv: ")
reformat_output = reformat_path(output_csv)

# Save as CSV
json_read.to_csv(reformat_output, index=False, encoding='utf-8')
print("SUCCESSFULLY CONVERT THE FILE. PLEASE CHECK")
