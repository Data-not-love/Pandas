import pandas as pd
import matplotlib.pyplot as plt


dataframe = pd.read_csv("F:/3.5 Years/First Year/Python/Pandas/Datasets/CSV/archive/Netflix.csv")
print(len(dataframe))
dataframe["Date"] = pd.to_datetime(dataframe["Date"])
dataframe["Month"] = dataframe["Date"].dt.strftime('%B')
dataframe["Year"] = dataframe["Date"].dt.year
print(dataframe.columns)


october_data = dataframe[dataframe["Month"] == "October"]
Y_for_mean = october_data.groupby("Year")["Open"].mean()

# Group by "Year" to ensure each year only appears once
grouped_october = october_data.groupby("Year").first()  # Take the first entry for each year

# Create "October - Year" format for each unique year
X_for_year = []
for year in grouped_october.index:
    X_for_year.append(f"{year}")
print(X_for_year)


bars = plt.bar(x=X_for_year,height=Y_for_mean)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:,.3f}',# in ra 2 số sau thập phân
            ha='center', va='bottom')
plt.xticks(rotation = 45)
plt.grid(True,alpha = 0.3)
plt.title("Mean Open Price of NETFLIX in October Every Year")
plt.xlabel("Year")
plt.ylabel("Value per share ( $ )")
plt.show()