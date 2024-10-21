import pandas as pd

titanic = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.json")
# mean tuổi
print(titanic[["Sex", "Age"]].groupby("Sex").mean())

# đếm
condition = titanic["Sex"].value_counts()
print(condition)

print(titanic[["Sex","Survived"]].groupby("Survived").count())

print(titanic[["Pclass","Fare"]].groupby("Pclass").mean())

condition_pclass = titanic.groupby("Pclass").agg(
    count_male = pd.NamedAgg(column="Sex", aggfunc=lambda x:(x=="male").sum())
)
print(condition_pclass)

print("-------------------------------------------------")
# tìm số lượng female còn sống của từng class
condition_female_survided = titanic[titanic["Sex"] == "female"].groupby("Pclass").agg(
    count_survived_female = pd.NamedAgg(column="Survived",aggfunc=lambda x:(x == 1).sum())
)
print(condition_female_survided)
print("-------------------------------------------------")

# tìm sô lượng người nam, nữ sống sót mà chi Fare > 40$

condition_survived_fare_40 = titanic[titanic["Survived"] == 1].groupby("Sex").agg(
    count_fare = pd.NamedAgg(column="Fare", aggfunc=lambda x : (x > 40).sum())
)
print(condition_survived_fare_40)

# tìm số lượng người còn sống sót > 30 tuổi đi toa S cua moi lop
condition_ticket = titanic[((titanic["Survived"] == 1) & (titanic["Age"] > 30))].groupby("Pclass").agg(
    count_A_5_21171 = pd.NamedAgg(column="Embarked", aggfunc=lambda x :(x == "S").sum())
)
print(condition_ticket)




# KO THỂ ĐƯA ĐIỀU KIỆN TRỰC TIẾP vào groupby()
# lọc dữ liệu trước groupby() hoặc áp dụng điều kiện trong hàm tổng hợp agg() hoặc apply().