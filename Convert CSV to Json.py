import csv
import json

def csv_to_json ( csv_path, json_path):
    with open(csv_path, mode='r', encoding='utf-8') as csv_file:
        csv_read = csv.DictReader(csv_file)
        rows = list (csv_read)

    with open(json_path, mode='w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, indent=4, ensure_ascii=False)

csv_file = "F:/3.5 Years/First Year/Python/Pandas/Basic/test.csv" # Đường dẫn tới file CSV
json_file = "F:/3.5 Years/First Year/Python/Pandas/Basic/output.json" # Đường dẫn lưu file JSON

csv_to_json(csv_file, json_file)