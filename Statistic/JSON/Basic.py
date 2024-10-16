import pandas as pd

titanic = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.json")

print(titanic[["Sex", "Age"]].groupby("Sex").mean())
print(titanic[["Survived","Sex"]].groupby("Sex").count())
print(titanic[["Pclass","Fare"]].groupby("Pclass").mean())
print(titanic[["Pclass","Fare"]].groupby("Pclass").count())