import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Dữ liệu mẫu
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Men': [10.45, 15.4, 7.6, 10.8],
    'Woman': [5.9, 10.7, 12.3, 8.1]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Đặt 'Category' là chỉ số
df.set_index('Category', inplace=True)

# Vẽ biểu đồ cột đôi

x = np.arange(len(df.index))
width = 0.2
plt.figure(figsize=(10, 6))
bars_men = plt.bar(x - width/2, df['Men'], width, label='Men')
bars_women = plt.bar(x + width/2, df['Woman'], width, label='Woman')

def fix_bar_ui(bars):
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:,.2f}',
                ha='center', va='bottom')

fix_bar_ui(bars_men)
fix_bar_ui(bars_women)
# Thêm tiêu đề và nhãn
plt.title('Double Bar About Point Chart Example')
plt.xlabel('Category')
plt.ylabel('Values')
plt.xticks(x, df.index)   # Set the x-ticks to the category names
plt.grid(True, alpha =0.4)
# Hiển thị biểu đồ
plt.show()
