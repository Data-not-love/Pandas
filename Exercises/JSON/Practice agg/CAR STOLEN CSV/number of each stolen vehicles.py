import pandas as pd


dt_frame = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/Motor+Vehicle+Thefts+CSV/stolen_vehicles.csv")
print(len(dt_frame))
print(dt_frame.columns)

# sô lượng loại từng loại xe bị cướp

results = dt_frame.groupby("vehicle_type").agg(
    Number_of_vehicles = pd.NamedAgg(column="vehicle_type", aggfunc="count")
)

print(results)

results1 = dt_frame.groupby("vehicle_type").size().reset_index(name='Number_of_vehicles')

print(results1)