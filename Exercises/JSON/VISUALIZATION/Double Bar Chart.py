import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu
dt_frame = pd.read_json("F:/3.5 Years/First Year/Python/Pandas/Basic/titanic.json")
print(dt_frame["Pclass"].unique())


results = dt_frame[dt_frame["Survived"] == 1].groupby("Pclass").agg(
    male = pd.NamedAgg(column="Sex",aggfunc=lambda x : (x=='male').sum()),
    female = pd.NamedAgg(column="Sex",aggfunc=lambda x : (x=='female').sum())
)
print(results)
# Vẽ biểu đồ
x = np.arange(len(dt_frame['Pclass'].unique()))

# Vẽ cột cho nam và nữ
bars_men = plt.bar(x - 0.3/2, results['male'].values, 0.3, label='Men')
bars_women = plt.bar(x + 0.3/2, results['female'].values, 0.3, label='Women')


def fix_bar_UI (bars) :
# Chỉnh sửa đồ thị
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:,.0f}',
                ha='center', va='bottom')

fix_bar_UI(bars_men)
fix_bar_UI(bars_women)

plt.title("Number of Survivors by Class and Gender")
plt.ylabel("Number of Survivors ( 1 Unit )")
plt.xlabel("Class")
plt.xticks(x,['Class 1', 'Class 2', 'Class 3'])
plt.legend(title='Genders')
plt.grid(True, alpha=0.3)
plt.show()