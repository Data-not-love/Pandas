# Tuổi trung bình và trung vị của các hành khách theo giới tính là bao nhiêu?
import pandas as pd
dt_frame = pd.read_json("/Basic/titanic.json")
results = dt_frame.groupby("Sex").agg(
    mean_age = pd.NamedAgg(column="Age", aggfunc="mean"),
    median_age = pd.NamedAgg(column="Age", aggfunc="median")
)
print(results)
print(dt_frame.columns)