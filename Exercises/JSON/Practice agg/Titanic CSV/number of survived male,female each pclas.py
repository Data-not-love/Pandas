import pandas as pd



dt_frame = pd.read_json("/Basic/titanic.json")
print(len(dt_frame))
results = dt_frame.groupby(["Pclass","Sex"]).agg(
    male_and_female = pd.NamedAgg(column="Survived",aggfunc=lambda x:(x==1).sum())
)

print(results)

# số người sống sót và tử vong mỗi class


results_2 = dt_frame.groupby(["Pclass","Sex"]).agg(
    Survived = pd.NamedAgg(column="Survived", aggfunc=lambda x:(x==1).sum()),
    Dead = pd.NamedAgg(column="Survived", aggfunc=lambda x:(x==0).sum())
)


print(results_2)
