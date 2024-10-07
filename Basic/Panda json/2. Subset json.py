import pandas as pd
import json

data_json = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/output.json")
data_frame_data_json = data_json.to_dict()

print_json = json.dumps(data_frame_data_json, indent = 4)
print(print_json)

name = data_json["Name"]
name_to_json = name.to_dict()
print_name_in_json = json.dumps(name_to_json, indent = 4)
print (print_name_in_json)


print (data_json.columns)
# Survived

# ko the dung head vs tail cho json cause json is not a dataframe
death_or_alive = data_json["Survived"]
death_or_alive_to_json = death_or_alive.to_dict()
print_death_or_alive_in_json = json.dumps(death_or_alive_to_json, indent=4)
print (print_death_or_alive_in_json)

information = data_json[["Survived", "Name" ]]
# in json 1 barn ghi json rieeng biet
information_to_json = information.to_dict(orient='records')
print_information_to_json = json.dumps(information_to_json, indent=4)
print(print_information_to_json)