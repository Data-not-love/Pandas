# tìm sô lượng người nam, nữ sống sót mà chi Fare > 40$
import pandas as pd

dt_frame = pd.read_json("/Basic/titanic.json")
print(dt_frame.columns)

fare_above_40 = dt_frame[dt_frame["Survived"] == 1 ].groupby("Sex").agg(
    Fare_40 = pd.NamedAgg(column="Fare",aggfunc=lambda x:(x > 40).sum())
)

print(fare_above_40)