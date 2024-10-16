# Giá vé trung bình và trung vị của hành khách theo từng hạng ghế
import pandas as pd

titanic = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.json")

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
rate_2 = titanic.groupby(["Pclass","Sex"]).agg(
    mean = pd.NamedAgg(column="Survived",aggfunc="mean"),
)
print(rate_2)

print(titanic.groupby(["Pclass", "Sex"])["Survived"].mean())

# Trong mỗi Pclass, sum sô lượng hành khách có tuổi > 35 và số lượng người sống sót là bao nhiêu?
ok = titanic.groupby("Pclass").agg(
    sum_above_35 = pd.NamedAgg(column="Age",aggfunc=lambda x :(x > 35).sum()),
    sum_survival = pd.NamedAgg(column="Survived",aggfunc=lambda x:(x==1).sum())
)

print (ok )

def age_survival_analysis(df):
    return pd.Series({
        "above_35_count": (df["Age"] > 35).sum(),
        "survived_count": df["Survived"].sum()
    })

result = titanic.groupby("Pclass").apply(age_survival_analysis,include_groups=False)
print(result)
