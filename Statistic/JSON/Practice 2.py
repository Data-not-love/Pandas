import pandas as pd
# Đối với mỗi nhóm Pclass và giới tính, sum tìm số lượng hành khách có giá vé > mean giá vé trung bình của nhóm đó.
# tìm mean môi nhóm

titanic = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.json")
def function (dtframe):
    mean_fare = dtframe["Fare"].mean()
    return (dtframe["Fare"] > mean_fare).sum()
    print(mean_fare)


print(titanic.groupby(["Pclass","Sex"]).apply(function,include_groups=False))

print("Still don't understand")