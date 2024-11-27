import pandas as pd

dt_frame_1 = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/Motor Vehicle Thefts CSV/stolen_vehicles.csv")
print (dt_frame_1.columns)

print ("-----------------------------------------------------------------------------------------")
dt_frame_2 = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/Motor Vehicle Thefts CSV/locations.csv")
print (dt_frame_2.columns)

print ("-----------------------------------------------------------------------------------------")

merged_df = pd.merge(dt_frame_1,dt_frame_2, how = 'inner', on ="location_id")
print (merged_df)

print ("-----------------------------------------------------------------------------------------")
# in số lượng xe bị trộm từng region
r1 = merged_df.groupby("region").agg(
    amount = pd.NamedAgg(column = "vehicle_id",aggfunc = "count")
        )
print (r1)
print("------------------------------------------------------------------------------------------")

# in số lượng loại xe bị cướp tưng region
r2 = merged_df.groupby(["region","vehicle_type"]).agg(
    amount = pd.NamedAgg(column = "vehicle_id",aggfunc = "count")
        )
print (r2)
print ("-----------------------------------------------------------------------------------------")
# in số lượng loại xe bị cướp trên 30 chiếc từng region
r3 = merged_df.groupby(["region","vehicle_type"]).agg(
    amount = pd.NamedAgg(column = "vehicle_id",aggfunc = "count" )
)

r3_filtered = r3[r3["amount"]>30]
print (r3_filtered)

print ("-----------------------------------------------------------------------------------------")

# in số lượng loại xe bị cướp trên 10 và dưới 40  chiếc xe
r4 = merged_df.groupby(["region","vehicle_type"]).agg(
    amount = pd.NamedAgg(column = "vehicle_id", aggfunc="count")
)


print (r4[(r4["amount"] >= 10) & (r4["amount"] <= 40)])

# in vùng và số lượng loại xe luxury
print ("-----------------------------------------------------------------------------------------")
dt_frame_3 = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/Motor Vehicle Thefts CSV/make_details.csv")
print (dt_frame_3.columns)


merged_df_2 = pd.merge(merged_df,dt_frame_3, how = "inner",on ="make_id")
print (merged_df_2)

result = merged_df_2.groupby(["region","make_type"]).agg(
    amount = pd.NamedAgg(column = "vehicle_id", aggfunc = "count")

)
print (result)
print ("----------------------------------------------------------------------------------------")
r5 = merged_df_2[merged_df_2["make_type"]=="Luxury"].groupby(["region","vehicle_type"]).agg(
    amount = pd.NamedAgg(column = "vehicle_id", aggfunc = "count")
)
print (r5)

print ("----------------------------------------------------------------------------------------")


mean = dt_frame_1["vehicle_id"].count() / dt_frame_2["location_id"].count()
print (mean)

print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# tìm các region có số lượng xe > mean

r6 = merged_df.groupby("region").agg(
    amount = pd.NamedAgg(column = "vehicle_id" , aggfunc = lambda x: x.count () > mean)
)
print (r6)

result_11 = merged_df_2.groupby(["region","make_type"]).agg(
    amount = pd.NamedAgg(column = "vehicle_id", aggfunc ="count")
)
print(result_11)

print ("----------------------------------------------------------------------------------------")

# số lượng xe bị ăn cắp từng năm
merged_df_2["date_stolen"] = pd.to_datetime(merged_df_2["date_stolen"], format = '%m/%d/%y')
merged_df_2["year"] = merged_df_2["date_stolen"].dt.year
merged_df_2["month"] = merged_df_2["date_stolen"].dt.month
r7 = merged_df_2.groupby(["region","year","month"]).agg(
    amount = pd.NamedAgg (column = "vehicle_id", aggfunc ="count")
)
print (r7)
