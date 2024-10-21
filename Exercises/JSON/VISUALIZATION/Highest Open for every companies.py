import pandas as pd
import matplotlib.pyplot as plt
import json
import os

json_path = "/Datasets/JSON/Stock/"

json_files = []
json_files = [json_file for json_file in os.listdir(json_path) if json_file.endswith('.json')]
x_companies = ["Amazon","Apple","Facebook","Google","Netflix"]
def load_dt_frame_and_print_in_json(json_file_path):
    full_path = os.path.join(json_path, json_file_path)
    dtframe = pd.read_json(full_path)
    data_frame_to_json = dtframe.to_dict(orient="records")
    json.dumps(data_frame_to_json, default=str, indent=4)
    return dtframe


# đọc data frame từ json
company_dataframes = []
for json_file in json_files:
    load_data = load_dt_frame_and_print_in_json(json_file)
    company_dataframes.append(load_data)
    print(company_dataframes)


def highest_open_each_company(dataframe):
    return dataframe["Open"].max()


max_open_price = []
for company_dataframe in company_dataframes:
    max_open = highest_open_each_company(company_dataframe)
    max_open_price.append(max_open)
    print(max_open)


bars = plt.bar(x=x_companies,height=max_open_price)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:,.0f}',
            ha='center', va='bottom')

    
plt.grid(True)
plt.xlabel("Company")
plt.ylabel("Highest Open Price ($)")
plt.title("Highest Open Price For Every Company")
plt.show()