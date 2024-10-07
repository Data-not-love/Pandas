# lọc hàng và cột
import pandas as pd

csv = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Basic/test.csv")
condition = csv[((csv["Age"]> 35) & (csv["Survived"] ==1)) | (csv["Pclass"] == 3)]
print (condition.head (23))
print ( condition.shape)

condition_1 = csv[csv["Pclass"].isin([0,1])]
print ( condition_1)


condition_2 = csv[csv["Cabin"].notna() & (csv["Survived"] == 1) & (csv["Fare"] >= 100)]
print(condition_2)

print ( csv["Age"].max() ,csv["Age"].min() )
passenger_name = csv.loc[(csv["Survived"] == 1) & (csv["Age"] > 45) & (csv["Embarked"] == 'C'), ["Name","Fare"]]

print (passenger_name)