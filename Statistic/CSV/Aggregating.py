import pandas as pd

titanic_to_dataFrame = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.csv")
print(titanic_to_dataFrame[["Sex", "Age"]].groupby("Sex").mean())
