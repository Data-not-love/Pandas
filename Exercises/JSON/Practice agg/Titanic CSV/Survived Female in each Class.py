import pandas as pd
# tìm số lượng female còn sống của từng class
dt_frame = pd.read_json("/Basic/titanic.json")

print(dt_frame.columns)


results = dt_frame[dt_frame["Survived"] == 1].groupby("Pclass").agg(
    Survived_female = pd.NamedAgg(column="Sex",aggfunc=lambda x:(x=='female').sum())
)

print(results)

