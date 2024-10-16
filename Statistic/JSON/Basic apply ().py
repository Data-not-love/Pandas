# công dụng như agg()
import pandas as pd


titanic = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.json")
# agg
condition_pclass = titanic.groupby("Pclass").agg(
    count_male = pd.NamedAgg(column="Sex", aggfunc=lambda x:(x=="male").sum())
)
print(condition_pclass)
# apply version
def count_male (xample_dataFrame):
    return len(xample_dataFrame[xample_dataFrame["Sex"] == "male"])
# dùng include_groups=False đề ko hiện warning
# result = titanic.groupby("Pclass").apply(count_male_survivor,include_groups=False)
# chỉ rõ cột làm việc
result_1 = titanic.groupby("Pclass")[["Sex"]].apply(count_male)
print(result_1)

print("-----------------------------------------------------------------")
# tìm số lượng female còn sống của từng class
condition_female_survided = titanic[titanic["Sex"] == "female"].groupby("Pclass").agg(
    count_survived_female = pd.NamedAgg(column="Survived",aggfunc=lambda x:(x == 1).sum())
)
print(condition_female_survided)
# apply version
def count_female_survivor (ex_dataFrame):
    return len(ex_dataFrame[(ex_dataFrame["Sex"] == "female") & (ex_dataFrame["Survived"] == 1)])
result_2 = titanic.groupby("Pclass")[["Sex","Survived"]].apply(count_female_survivor)
print(result_2)


print("-----------------------------------------------------------------")
# tìm sô lượng người nam, nữ sống sót mà chi Fare > 40$

condition_survived_fare_40 = titanic[titanic["Survived"] == 1].groupby("Sex").agg(
    count_fare = pd.NamedAgg(column="Fare", aggfunc=lambda x : (x >= 40).sum())
)
print(condition_survived_fare_40)
# apply version
def count_fare (ex_dataFrame):
    return len(ex_dataFrame[(ex_dataFrame["Survived"] == 1) & (ex_dataFrame["Fare"] >= 40)])
result_3 = titanic.groupby("Sex")[["Survived","Fare"]].apply(count_fare)
print(result_3)


print("-----------------------------------------------------------------")
# tìm số lượng người còn sống sót > 30 tuổi đi toa S
condition_ticket = titanic[((titanic["Survived"] == 1) & (titanic["Age"] > 30))].groupby("Pclass").agg(
    count_A_5_21171 = pd.NamedAgg(column="Embarked", aggfunc=lambda x :(x == "S").sum())
)
print(condition_ticket)



# apply version
def count_survivor_above_30 (ex_dataFrame):
    return len(ex_dataFrame[(ex_dataFrame["Survived"] == 1) & (ex_dataFrame["Age"] > 30) & (ex_dataFrame["Embarked"] == "S")])
result_4 = titanic.groupby("Pclass")[["Survived","Age","Embarked"]].apply(count_survivor_above_30)
print(result_4)

print("-----------------------------------------------------------------")

# tìm mean fare và số lượng khách hàng > 35 tuổi group Pclass
above_35 = titanic[titanic["Age"] > 35]
result = titanic[titanic["Sex"] == "female"].groupby("Pclass").agg(
    count_mean_fare = pd.NamedAgg(column="Fare",aggfunc="mean"),
    count_age_above_35 = pd.NamedAgg(column="Age", aggfunc="count")
)
print(result)


#
# mode != mean != count
fare_above_40 = titanic[titanic["Fare"] > 40]
result_40 = titanic.groupby("Embarked").agg(
    mode_embarked=pd.NamedAgg(column="Sex", aggfunc=lambda x: x.mode()[0] if not x.mode().empty else None),  # Lấy giá trị mode đầu tiên (nếu có)
    above_40 = pd.NamedAgg(column="Fare",aggfunc="count")
)
print(result_40)

