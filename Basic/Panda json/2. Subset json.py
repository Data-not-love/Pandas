import pandas as pd
import json

data_json = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/output.json")
data_json_limited = data_json.head(5)
data_frame_data_json = data_json_limited.to_dict()
print_json = json.dumps(data_frame_data_json, indent = 4)
print(print_json)
print (data_json.columns)



name = data_json["Name"] # data frame with one attribute
limited_info = name.head(6)
name_to_json = limited_info.to_dict()
print_name_in_json = json.dumps(name_to_json, indent = 4)
print (print_name_in_json)


# Survived

# ko the dung head vs tail cho json cause json is not a dataframe
death_or_alive = data_json["Survived"] # data frame with one attribute
limited_info_for_survival = death_or_alive.tail(7)
death_or_alive_to_json = limited_info_for_survival.to_dict()
print_death_or_alive_in_json = json.dumps(death_or_alive_to_json, indent=4)
print (print_death_or_alive_in_json)



information = data_json[["Survived", "Name","Sex","Age"]] # data frame with 4 attribute
limited_information = information.tail(3)
# in json 1 barn ghi json rieeng biet
information_to_json = limited_information.to_dict(orient='records')
print_information_to_json = json.dumps(information_to_json, indent=4)
print(print_information_to_json)

print(type(information))

print ("Not done")