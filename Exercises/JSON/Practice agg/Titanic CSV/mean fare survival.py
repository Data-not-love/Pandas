# Giá vé trung bình của những người sống sót là bao nhiêu?
import pandas as pd
dt_frame = pd.read_json("/Basic/titanic.json")

r = dt_frame[dt_frame["Survived"] == 1].groupby("Survived").agg(
    mean_fare = pd.NamedAgg(column= "Fare", aggfunc="mean")
)
print(r)
print(dt_frame.columns)
