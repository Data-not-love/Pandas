# tìm số lượng người còn sống sót > 30 tuổi các toa
import pandas as pd
dt_frame = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.json")
print(dt_frame.columns)


results = dt_frame[dt_frame["Survived"] == 1].groupby("Embarked").agg(
    Above_30 = pd.NamedAgg(column="Age", aggfunc=lambda x:(x > 30).sum())
)

print(results)

print(len(dt_frame))