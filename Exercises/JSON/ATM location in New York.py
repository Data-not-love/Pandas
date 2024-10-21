import pandas as pd

dt_frame = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Datasets/JSON/Bank-Owned_ATM_Locations_in_New_York_State.json")

print (dt_frame.columns)
ATM_in_brooklyn = len(dt_frame[dt_frame["City"] == "BROOKLYN"])
print(ATM_in_brooklyn)

Number_of_Alma = len(dt_frame[dt_frame["Name of Institution"] == "ALMA BANK"])
print(Number_of_Alma)



#agg : designed to operate on grouped DataFrames or Series objects.If you are not grouping the data beforehand, this could be causing the error
number_ATM_in_brooklyn = dt_frame.agg(
    # nhớ đặt tên hàm NamedAgg
    Brooklyn_ATMs = pd.NamedAgg(column="City",aggfunc=lambda x: (x=='BROOKLYN').sum()),
    Saratoga_ATMs = pd.NamedAgg(column="City",aggfunc=lambda x: (x=='SARATOGA SPRINGS').sum()),
    Rochester_ATMs = pd.NamedAgg(column="City",aggfunc=lambda x: (x=='ROCHESTER').sum())
)
print(number_ATM_in_brooklyn)

# đếm atm theo county
number_of_ATM = dt_frame.groupby("County").agg(
    ATMs = pd.NamedAgg(column="County",aggfunc='count')
)
print(number_of_ATM)

print("----------------------------------------------------------------------")
number_of_ATM_1 = dt_frame.groupby("County")["Name of Institution"].count()
print(number_of_ATM_1)

#in ra các city
all_city = dt_frame["City"].unique()
print(all_city)

number_of_all_city = len(dt_frame["City"].unique())
print(number_of_all_city)

# tìm các Institutions , số lượng instituion ở Westchester
dt_frame_weschester = dt_frame[dt_frame["County"] == "Westchester"]
all_instituions_in_weschester = dt_frame_weschester.groupby("Name of Institution").agg(
    name_of_institution = pd.NamedAgg(column="Name of Institution",aggfunc="count")
)
print(all_instituions_in_weschester)

print ("---------------------------------------------------------------------------")
df_1 = dt_frame[dt_frame["County"] == 'Westchester']
all_instituions_in_weschester_111 = df_1.groupby('Name of Institution').agg(
    number=('Name of Institution', 'size')
)
print(all_instituions_in_weschester_111)

print ("---------------------------------------------------------------------------")


results = dt_frame[dt_frame["County"] == 'Westchester'].groupby('Name of Institution').count()
print(results)