import pandas as pd
# read_csv : đọc thành dataframe = bảng
analyzed_csv = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Basic/test.csv")

# in 9 hàng đầu tiên của dataframe
print (analyzed_csv.head(9))

# in 5 hàng cuối c
print (analyzed_csv.tail(5))

# in kiểu dữ liệu
print (analyzed_csv.dtypes)
print (analyzed_csv.info())
# read_* : đọc data , to_* : chứa data
# không cho ghi đè
#analyzed_csv.to_excel("titanic.xlsx", sheet_name="tourists", index=True)
# index = False :

# excel_file = pd.read_excel("titanic.xlsx", sheet_name="tourists")


print (analyzed_csv.columns)
ages = analyzed_csv[["Age","Survived"]]
print (ages.head(5))

print (type(ages))
print (ages.shape)
print ( "ok")