import pandas as pd
import json

# LOAD JSON
data_json = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/output.json")


limited_records_json = data_json.head(3)
convert_json = limited_records_json.to_dict()
print_in_json = json.dumps(convert_json, indent= 4 )
print ( print_in_json)


print (data_json.columns)


information = data_json[(data_json["Sex"] == "male") &
                        (data_json["Age"] >= str(53)) &
                        (data_json["Pclass"] == 3) &
                        (data_json["Fare"] > 20)]

limited_information_json = information.head(5)
info_with_condition = limited_information_json.to_dict(orient='records')
print_information_in_json_4mat = json.dumps(info_with_condition, indent=5)
print (print_information_in_json_4mat)

print("Gioi han voi ham iloc")

# chọn điều kiện lọc kết quả
filter_conditions = data_json[(data_json["Embarked"] == "S") |
                              (data_json["Sex"] == 'female') &
                              (data_json["Age"] > str(30))]

# chọn thuộc tính để hiển thị
in4 = filter_conditions[["Name", "Embarked", "Sex", "Age"]]

# giới hạn từ hàng 200 -> 205 rồi so sánh đk
# có => in json
# ko => []
limited_in4 = in4.iloc[200:215]
convert_2_json = limited_in4.to_dict(orient='records')
print_in_json_4mat = json.dumps(convert_2_json, indent=5)
print(print_in_json_4mat)


filter_conditions_2 = data_json[(data_json["Sex"] == "female")]

info_2 = filter_conditions_2[["Name", "Fare",]]
limited_in4_2 = info_2.head(5)
convert_json_2 = limited_in4_2.to_dict(orient='records')
print_js = json.dumps(convert_json_2,indent=4)
print(print_js)