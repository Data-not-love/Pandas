import pandas as pd
import matplotlib.pyplot as plt


air_quality = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.csv")
print (air_quality[["Cabin"]])
# Mean = AVERAGE
print (air_quality.columns)
print (air_quality["Fare"].mean())


# Mode = MOST SHOWN IN A SET OF VALUE
print (air_quality["Survived"].mode())
print (air_quality["Sex"].mode())
print (air_quality["Pclass"].mode())
print (air_quality["Embarked"].mode())
print (air_quality["Cabin"].mode())


# Median = giá trị nằm giữa 1 tập dữ liệu được sắp xếp
print ("Median")
print (air_quality["Fare"].median())
print (air_quality["Age"].median())


# mô tả
describe_csv = air_quality[["Age","Fare","Ticket"]].describe()
print(describe_csv)