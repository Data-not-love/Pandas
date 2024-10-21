import pandas as pd

dt_frame_stolen_vehicles = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/Motor+Vehicle+Thefts+CSV/stolen_vehicles.csv")
print(dt_frame_stolen_vehicles.columns)
dt_frame_location = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/Motor+Vehicle+Thefts+CSV/locations.csv")
print(dt_frame_location.columns)

merge_2_data_frame = pd.merge(dt_frame_stolen_vehicles,dt_frame_location[["region","location_id"]],on="location_id",how="outer")
print(merge_2_data_frame)

result = merge_2_data_frame.groupby("vehicle_type").agg(
    stolen_quantity = pd.NamedAgg(column="vehicle_type", aggfunc="count"),
    where_most_being_stolen = pd.NamedAgg(column="region",aggfunc=lambda x:x.value_counts().idxmax())
)
print(result)

