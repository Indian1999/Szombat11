import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # pip install seaborn
import os # Az elérési útvonalak kezelésére használjuk

MAIN_PATH = os.path.abspath(__file__)
# Megadja, hogy mi az elérési útvonala annak a scriptnek ami éppen fut
DIR_PATH = os.path.dirname(MAIN_PATH)
TIPS_PATH = os.path.join(DIR_PATH, "tips.csv")
GRAFS_PATH = os.path.join(DIR_PATH, "grafikonok")

data = pd.read_csv(TIPS_PATH)
print(data)
print(data.dtypes)
print(data.describe())

def days_bar_chart(file_path = None, show_fig = True):
    plt.bar(data["day"], data["tip"])
    plt.title("Tip amount on days")
    plt.xlabel("Day")
    plt.ylabel("Tip amount")
    if file_path: # Valaminek None értéke van, akkor az False, ha brámi más, True
        plt.savefig(file_path) # nem törli a plot tartalmát
    if show_fig:
        plt.show()  # show() az törli a plot tartalmát
    plt.close()
    
days_bar_chart(os.path.join(GRAFS_PATH, "days_tip_bar.png"), False)
