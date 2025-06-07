import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # pip install matplotlib.pyplot
import seaborn as sns
import plotly.express as px # pip install plotly.express
import os # Elérési útvanalak kezelésére (filepath)

dir_path = os.path.dirname(__file__)
with open(os.path.join(dir_path, "item_block_data.json"), "r", encoding="utf-8") as f:
    data = json.load(f)
    
print(type(data))

df = pd.DataFrame.from_dict(data, orient="index")
print(df) # kiírja az első 5 sorát a df-nek
print(df.columns)

def categorize_item(item):
    """Possible categories: Block, Tool, Armor, Food, Other"""
    if item["is_block"] == True:
        return "Block"
    elif "c:tools" in item["item_tags"]:
        return "Tool"
    elif "c:armors" in item["item_tags"]:
        return "Armor"
    elif "c:foods" in item["item_tags"]:
        return "Food"
    else:
        return "Other"
    
#print(categorize_item(data["diamond_pickaxe"]))
#print(categorize_item(data["acacia_planks"]))

df["category"] = df.apply(categorize_item, axis = 1)

df["subcategory"] = df["name"].apply(
    lambda x: x.split("_")[0] if "_" in x else "misc"
)

category_counts = df.groupby(["category"]).size().reset_index(name="count")
    
plt.pie(category_counts["count"], labels = category_counts["category"], shadow=False)
plt.title("Minecraft item category distribution")
plt.savefig(os.path.join(dir_path, "categories_pie_chart.png"))
plt.close()

category_counts = df.groupby(["category", "subcategory"]).size().reset_index(name="count")
fig = px.sunburst(
    category_counts,
    path = ["category", "subcategory"],
    values = "count",
    title = "Minecraft item categories"
)

fig.write_html(os.path.join(dir_path, "minecraft_item_categories.html"))

sns.violinplot(data=df, x = "category", y = "stack_limit")
plt.title("Max stack size per category")
plt.savefig(os.path.join(dir_path, "category_stack_sizes.png"))
plt.close()