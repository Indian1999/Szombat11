import pandas as pd # terminálba: pip install pandas
import matplotlib.pyplot as plt # pip install matplotlib.pyplot

data = pd.read_csv("NFLX.csv")
print(data)
print(type(data)) # <class 'pandas.core.frame.DataFrame'>

all_time_high = data["High"].max()
all_time_low = data["Low"].min()
close_average = data["Close"].mean()
open_median = data["Open"].median()
close_std = data["Close"].std() # Standard Deviation (szórás)

print(f"A valaha volt legnagyobb részvényérték: {round(all_time_high, 2)} $.")
print(f"A valaha volt legalacsonyabb részvényérték: {round(all_time_low, 2)} $.")
print(f"A záráskori részvényértékek átlaga: {round(close_average, 2)} $.")
print(f"A nyitáskori részvényértékek mediánja: {round(open_median, 2)} $.")
print(f"A záráskori részvényértékek szórása: {round(close_std, 2)} $.")

print(data.describe())
print(data.dtypes)

# Melyik napon volt a részvény értéke a legmagasabb?
max_row = data[ data["High"] == all_time_high ]
print(max_row)
print(type(max_row)) # <class 'pandas.core.frame.DataFrame'>
max_date = max_row.iloc[0, 0]
print(f"A rekord magas részvény állás {max_date} napon volt.")

# Mennyi volt a záráskori részvény állás azon a napon amikor a legkisebb értéken állt a részvény?

min_row = data[data["Low"] == all_time_low]
lowest_close = min_row.iloc[0, 4]
print(f"A záráskori érték a 'legrosszabb' napon: {lowest_close} $.")

# Mennyi volt a záráskori érték 2017-02-10-én?
data["Date"] = pd.to_datetime(data["Date"])
print(data.dtypes)
filtered_row = data[data["Date"] == "2017-02-10"]
close_price = filtered_row.iloc[0, 4]
print(f"A záráskori érték 2017 február 10-én: {close_price} $.")

# Szűrjük ki a 2019 novemberi adatokat
november_2019 = data[data["Date"] >= "2019-11-01"]
november_2019 = november_2019[november_2019["Date"] <= "2019-11-30"]
print(november_2019)
print(november_2019.describe())

# Hány napon volt a zárási érték az átlag 5%-os környezetében?

close_mean = data["Close"].mean()
average_days = data[data["Close"] >= close_mean * 0.95]
average_days = average_days[average_days["Close"] <= close_mean * 1.05]
print(average_days)
print(f"{len(average_days)} átlagos nap volt a tőzsdén.")

# Azon a napon amikor a legnagyobb volt a részvény forgalom (Volume), mennyi volt a netflix 
# részvények forgalma [ volume * átlag(High, Low)]


max_volume = data["Volume"].max()

max_volume_row = data[data["Volume"] == max_volume]
print(max_volume_row)
average_value = (max_volume_row.iloc[0, 2] + max_volume_row.iloc[0, 3]) / 2
print(f"Aznap amikor a legtöbb részvény kelt el, összesen {max_volume} db, a teljes forgalom értéke {max_volume * average_value} $ volt.")


# Ábrázoljuk egy grafikonon a részvények árának alakulását

plt.plot(data["Date"], data["Close"])
plt.title("Stock price over time")
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.close()

data.set_index("Date", inplace = True)
print(data)
monthly_average = data["Close"].resample("ME").mean()
monthly_average = monthly_average.reset_index()

print(monthly_average.dtypes)

monthly_average["Date"] = monthly_average["Date"].dt.to_period("M")
print(monthly_average)

print(monthly_average.dtypes)
