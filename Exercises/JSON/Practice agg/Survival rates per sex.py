# Tỷ lệ phần trăm những người sống sót theo giới tính là bao nhiêu?
import pandas as pd
dt_frame = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.json")
print(dt_frame.columns)
total_survival = dt_frame[dt_frame["Survived"] == 1]

survival_rates = total_survival.groupby("Sex").agg(
    survival = pd.NamedAgg(column="Survived",aggfunc=lambda x:(x.sum())),
    survival_rates = pd.NamedAgg(column="Survived",aggfunc=lambda x:(x.sum()/len(total_survival)) *100)
)
print(survival_rates)


print(len(total_survival))
