import pandas as pd


dt_frame = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/Motor Vehicle Thefts CSV/stolen_vehicles.csv")
print(len(dt_frame))
print(dt_frame.columns)
print ("--------------------------------------------------------------------------------------------------")
# sô lượng loại từng loại xe bị cướp

results = dt_frame.groupby("vehicle_type").agg(
    Number_of_vehicles = pd.NamedAgg(column="vehicle_type", aggfunc="count")
)

print(results)
print ("--------------------------------------------------------------------------------------------------")
results1 = dt_frame.groupby("vehicle_type").size().reset_index(name='Number_of_vehicles')

print(results1)
print ("--------------------------------------------------------------------------------------------------")
dt_frame["date_stolen"] = pd.to_datetime(dt_frame["date_stolen"], format = '%m/%d/%y')
dt_frame["Year"] = dt_frame["date_stolen"].dt.year
dt_frame["Month"] = dt_frame["date_stolen"].dt.month
# số lượng loại xe bị cướp từng năm
result2 = dt_frame.groupby("Year").agg(
    number_of_vehicles_stolen_each_year = pd.NamedAgg(column="vehicle_id", aggfunc="count")
        )
print(result2)
print ("--------------------------------------------------------------------------------------------------")

# số lượng xe bị cướp từng tháng từng năm
result_3 = dt_frame.groupby(["Year","Month"]).agg(
    stolen_vehicles = pd.NamedAgg(column="vehicle_id",aggfunc ="count")
        )
print (result_3)
