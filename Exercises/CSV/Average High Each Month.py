# mean high của Facebook các tháng trong năm 2013
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


dtFrame = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/archive/Facebook.csv")
# convert dataframe to date time
dtFrame["Date"] = pd.to_datetime(dtFrame["Date"])

# lấy khoảng thời gian
start_date = datetime(2013,1,1)
end_date = datetime(2013,12,31)

# gắn vào 1 dataframe
wanted_range = (dtFrame["Date"] >= start_date) & (dtFrame["Date"] <= end_date)
dtFrame_2013 = dtFrame[wanted_range].copy()


# Thêm cột mới 'Month' với tên tháng (January, February,...)
dtFrame_2013["Month"] = dtFrame_2013['Date'].dt.month_name()

monthly_highs = dtFrame_2013.groupby("Month")["High"].sum()  # Tính tổng
trading_days_count = dtFrame_2013.groupby("Month")["High"].count()  # Tính số ngày giao dịch
print(trading_days_count)

# Tính giá trị trung bình bằng cách chia tổng cho số ngày giao dịch
mean_highs = monthly_highs / trading_days_count
months_order = ['January', 'February', 'March',
                'April', 'May', 'June',
                'July', 'August', 'September',
                'October', 'November', 'December']
mean_highs = mean_highs.reindex(months_order)


print(mean_highs)
print(dtFrame)

mean_highs.plot.bar(y="High")
plt.xticks(rotation=45)
plt.show()
# In kết quả

#kết quả bị sai vì có nhưng ngày trong tháng ko giao dịch