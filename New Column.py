import pandas as pd

# 1. load data
df = pd.read_csv("mcd_menu_clean.csv")

# 2. function sub-category
def sub_category(name):
    name = name.lower()
    if "muffin" in name:
        return "Muffin"
    elif "wrap" in name:
        return "Wrap"
    elif "nasi" in name or "bubur" in name:
        return "Rice"
    elif "hotcakes" in name:
        return "Hotcakes"
    elif "hashbrown" in name:
        return "Side"
    else:
        return "Others"

# 3. apply function
df["sub_category"] = df["product_name"].apply(sub_category)

# 4. check result
print(df["sub_category"].value_counts())

# 5. Plotting
import matplotlib.pyplot as plt

df["sub_category"].value_counts().plot(kind="bar")
plt.title("Distribusi Sub-Kategori Menu Sarapan Pagi McDonald's Indonesia")
plt.xlabel("Sub-Kategori")
plt.ylabel("Jumlah Menu")
plt.tight_layout()
plt.show()
