import numpy as np
import pandas as pd
import json

# Đọc dữ liệu từ file JSON
with open('F:/3.5 Years/First Year/Python/Pandas/Datasets/JSON/Bank-Owned_ATM_Locations_in_New_York_State.json', 'r') as file:
    data = json.load(file)

# Chuyển đổi thành DataFrame
df = pd.DataFrame(data)

# Chuyển cột 'City' thành chữ hoa
df['City'] = df['City'].str.upper()
df['Ratings'] = np.round(np.random.uniform(1.0,5,size=len(df)),2)
# Ghi lại vào file JSON với format mong muốn
with open('F:/3.5 Years/First Year/Python/Pandas/Datasets/JSON/Bank-Owned_ATM_Locations_in_New_York_State_and_ratings.json', 'w') as file:
    json.dump(df.to_dict(orient='records'), file, indent=4)
