import pandas as pd
import matplotlib.pyplot as plt
import json
import os

json_path = "F:/3.5 Years/First Year/Python/Pandas/Datasets/JSON/Stock/"

json_files = []
json_files = [json_file for json_file in os.listdir(json_path) if json_file.endswith('.json')]

def load_dt_frame_and_print_in_json(json_file_path):
    full_path = os.path.join(json_path, json_file_path)
    dtframe = pd.read_json(full_path)
    data_frame_to_json = dtframe.to_dict(orient="records")
    json.dumps(data_frame_to_json, default=str, indent=4)
    return dtframe

# trục X
x_company_list = ["Amazon","Apple","Facebook","Google","Netflix"]


company_dataFrames = []
for json_file in json_files:
    load_dt_frame = load_dt_frame_and_print_in_json(json_file)
    company_dataFrames.append(load_dt_frame)



def calculate_mean_volume (data_frame):
    return data_frame["Volume"].min()

# trục Y
list_mean_result = []

for company_name in company_dataFrames:
    company_mean = calculate_mean_volume(company_name)
    list_mean_result.append(company_mean)
print(list_mean_result)

# cột
bars = plt.bar(x= x_company_list,height = list_mean_result)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:,.0f}',
            ha='center', va='bottom')
plt.title('Average Stock Volume of Companies')
plt.grid(True)
plt.show()