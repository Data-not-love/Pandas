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

# Giá vé trung bình và trung vị của hành khách theo từng hạng ghế
ticket = titanic.groupby("Pclass").agg(
    mean = pd.NamedAgg(column="Fare",aggfunc="mean"),
    median = pd.NamedAgg(column="Fare",aggfunc="median"))
print (ticket)

ticket_2 = titanic.groupby("Pclass")["Fare"].agg(["mean", "median"])
print(ticket_2)
# Tuổi trung bình và trung vị của các hành khách theo giới tính là bao nhiêu?
Age = titanic.groupby("Sex").agg(
    mean=pd.NamedAgg(column="Age", aggfunc="mean"),
    median=pd.NamedAgg(column="Age", aggfunc="median")
)
print (Age)

print ( titanic.groupby("Sex")["Age"].agg(["mean", "median"])
)

#Tuổi trung bình của những người sống sót là bao nhiêu?
survivor = titanic[titanic["Survived"] == 1]
result_survivor = titanic.groupby("Survived").agg(
    mean=pd.NamedAgg(column="Age", aggfunc="mean"),
)
print (result_survivor)

print(titanic[titanic["Survived"] == 1]["Age"].mean())
#  Giá vé trung bình của những người sống sót là bao nhiêu?
print(titanic[titanic["Survived"] == 1]["Fare"].mean())

# Hạng ghế nào có tỷ lệ sống sót cao nhất?
print (titanic.groupby("Pclass")["Survived"].mean())

highest_survival_rate = titanic.groupby("Pclass").agg(
    rate = pd.NamedAgg(column="Survived", aggfunc=lambda x:(x == 1).mean())
)
print(highest_survival_rate)

# Có bao nhiêu hành khách không có thông tin về tuổi?
NaN_age = titanic["Age"].isna().sum()
print(NaN_age)

# Có bao nhiêu hành khách không có thông tin về giá vé?
NaN_fare = titanic["Fare"].isna().sum()
print(NaN_fare)


# Tỷ lệ phần trăm những người sống sót theo giới tính là bao nhiêu?
survival_rate = titanic.groupby("Sex").agg(
    rate = pd.NamedAgg(column="Survived",aggfunc=lambda x:(x==1).mean()*100)
)
print(survival_rate)
print (titanic.groupby("Sex")["Survived"].mean()*100)


# Tỉ lệ sống sót theo cả giới tính và hạng ghế (Pclass) là bao nhiêu?
rate = titanic.groupby(["Sex","Pclass"]).agg(
    rate = pd.NamedAgg(column="Survived",aggfunc=lambda x:(x==1).mean())
)
print(rate)

print (titanic.groupby(["Sex", "Pclass"])["Survived"].mean()
)

# Trong mỗi hạng ghế, hành khách nam hay nữ có tỷ lệ sống sót cao hơn?