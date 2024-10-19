import pandas as pd

# Đọc tệp CSV
csv_file_path = 'F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/archive/Facebook.csv'  # Thay thế bằng đường dẫn đến tệp CSV của bạn
df = pd.read_csv(csv_file_path)

# Chuyển đổi và lưu thành tệp Excel
excel_file_path = 'F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/archive/Facebook.xlsx'  # Đường dẫn lưu tệp Excel
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f'Tệp Excel đã được lưu tại: {excel_file_path}')
