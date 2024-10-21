# Giá vé trung bình và trung vị của hành khách theo Pclass
import pandas as pd

dt_frame = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.json")
print(dt_frame.columns)
results = dt_frame.groupby("Pclass").agg(
    mean = pd.NamedAgg(column="Fare", aggfunc="mean"),
    median = pd.NamedAgg(column="Fare", aggfunc="median")
)

print(results)