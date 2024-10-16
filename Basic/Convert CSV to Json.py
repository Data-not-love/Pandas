import csv
import json

import pandas as pd


def csv_to_json ( csv_path, json_path):
    with open(csv_path, mode='r', encoding='utf-8') as csv_file:
        csv_read = csv.DictReader(csv_file)
        rows = list (csv_read)

    with open(json_path, mode='w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, indent=4, ensure_ascii=False)



csv_file = "F:/3.5 Years/First Year/Python/Pandas/Create Plot/air_quality.csv"  # Đường dẫn tới file CSV
json_file = "F:/3.5 Years/First Year/Python/Pandas/Create Plot/air_quality_output.json"  # Đường dẫn lưu file JSON
date_time_json_file = "F:/3.5 Years/First Year/Python/Pandas/Create Plot/date_time_output.json"  # Đường dẫn lưu file JSON


convert_datetime = pd.read_csv(csv_file,parse_dates=['datetime'])

convert_datetime['datetime'] = convert_datetime['datetime'].apply(lambda x: x.isoformat() if pd.notnull(x) else None)
convert_datetime_json = convert_datetime.to_json(date_time_json_file,orient='records',indent=4)



csv_to_json(csv_file, json_file)

