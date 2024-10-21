import pandas as pd



dt_frame = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.json")

results = dt_frame.groupby(["Pclass","Sex"]).agg(
    male_and_female = pd.NamedAgg(column="Survived",aggfunc=lambda x:(x==1).sum())
)

print(results)