import pandas as pd

stolen_vehicles_dtframe = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/Motor Vehicle Thefts CSV/stolen_vehicles.csv")
print(stolen_vehicles_dtframe.columns)
details_dtframe = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/Motor Vehicle Thefts CSV/make_details.csv")
print(details_dtframe.columns)
location_dtframe = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/Motor Vehicle Thefts CSV/locations.csv")
print(location_dtframe.columns)
merge_dtframe = pd.merge(stolen_vehicles_dtframe,details_dtframe,on="make_id",how="outer")

second_merge = pd.merge(merge_dtframe,location_dtframe[["location_id","region"]],on="location_id",how="outer")

# số lượng xe hạng phổ thông, hạng sang đã bị cướp
result = second_merge.groupby("make_type").agg(
    quantity = pd.NamedAgg(column="make_type",aggfunc="count"),
    where_most_being_stolen = pd.NamedAgg(column="region", aggfunc=lambda x: x.value_counts().idxmax()),
    most_stolen_brand = pd.NamedAgg(column="make_name",aggfunc=lambda x: x.value_counts().idxmax()),
)

print(result)