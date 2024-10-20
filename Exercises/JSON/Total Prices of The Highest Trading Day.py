# Total Price = Highest (Close) * That day Volume

import pandas as pd
import matplotlib.pyplot as plt
import json
import os


json_path = "F:/3.5 Years/First Year/Python/Pandas/Datasets/JSON/Stock/"

json_files = []
json_files = [json_file for json_file in os.listdir(json_path) if json_file.endswith('.json')]
x_companies = ["Amazon","Apple","Facebook","Google","Netflix"]

# load data frame function
def load_data_frame (json_file_path):
    full_path = os.path.join(json_path, json_file_path)
    dtframe = pd.read_json(full_path)
    data_frame_to_json = dtframe.to_dict(orient="records")
    json.dumps(data_frame_to_json, default=str, indent=4)

    return dtframe

# USING load dataframe
companies_dataframes = []
for json_file in json_files:
    load_data = load_data_frame(json_file)
    companies_dataframes.append(load_data)



def calculating_stock_price (dataFrame):
    # Find the row with the highest "Close" price
    highest_close_idx = dataFrame["Close"].idxmax()

    Highest_close = dataFrame.loc[highest_close_idx,"Close"]
    Volume = dataFrame.loc[highest_close_idx,"Volume"]

    return Highest_close * Volume


list_result = []
for companies_dataframe in companies_dataframes:
    result = calculating_stock_price(companies_dataframe)
    list_result.append(result)
print(list_result)


bars = plt.bar(x= x_companies,height = list_result)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:,.0f}',
            ha='center', va='bottom')


plt.grid(True)
plt.ylabel("Total price of highest trading day")
plt.show()