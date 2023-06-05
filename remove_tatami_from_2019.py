import random
import pandas as pd

df = pd.read_csv("product_orders_copy.csv")
df.loc[df["order_date"] < "2020", "product_id"] = 102

"""
df["order_date"] = pd.to_datetime(df["order_date"])
df = df[
    (df["order_date"] < pd.Timestamp("2021-01-01"))
    & (df["order_date"] > pd.Timestamp("2020-01-01"))
]
"""

df.loc[
    (pd.to_datetime(df["order_date"]) < pd.Timestamp("2021-01-01"))
    & (pd.to_datetime(df["order_date"]) > pd.Timestamp("2020-01-01")),
    "product_id",
] = random.choice([101, 102])
df.loc[
    (pd.to_datetime(df["order_date"]) < pd.Timestamp("2022-01-01"))
    & (pd.to_datetime(df["order_date"]) > pd.Timestamp("2021-01-01")),
    "product_id",
] = random.choice([100, 101, 102, 104, 105])

df.to_csv("product_orders.csv", index=False)
