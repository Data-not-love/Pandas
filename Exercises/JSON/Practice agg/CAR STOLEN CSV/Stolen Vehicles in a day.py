import pandas as pd

dt_frame_stolen_vehicles = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/Motor+Vehicle+Thefts+CSV/stolen_vehicles.csv")
print(dt_frame_stolen_vehicles.columns)


# số phương tiện bị cướp trong 3/2/22
print(len(dt_frame_stolen_vehicles[dt_frame_stolen_vehicles["date_stolen"] == "3/2/22"]))

result = dt_frame_stolen_vehicles[dt_frame_stolen_vehicles["date_stolen"] == "3/2/22"].groupby("vehicle_type").agg(
    count = pd.NamedAgg(column="vehicle_type", aggfunc="count")
)

print(result)