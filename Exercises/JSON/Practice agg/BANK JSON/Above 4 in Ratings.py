import pandas as pd

dt_frame = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Datasets/JSON/Bank-Owned_ATM_Locations_in_New_York_State_and_ratings.json")
# tìm số lượng institution có hơn 4.0 rating ở GENEVA
above_4 = dt_frame[(dt_frame["City"] == "GENEVA") & (dt_frame["Ratings"] >= 4.0)].groupby("Name of Institution").agg(
    Number_of_Institutions_above_4 = pd.NamedAgg(column="Name of Institution",aggfunc="count")
)
print(above_4)
