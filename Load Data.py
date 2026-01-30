import pandas as pd

df = pd.read_csv("mcd_menu_clean.csv")

df.info()

print(df["category"].value_counts())
