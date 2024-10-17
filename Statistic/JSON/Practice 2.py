import pandas as pd
# Đối với mỗi nhóm Pclass và giới tính, sum tìm số lượng hành khách có giá vé > mean giá vé trung bình của nhóm đó.

titanic = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.json")
titanic.groupby(["Pclass","Sex"]).agg(

)
print ( "Not done yet")