import numpy as np
import pandas as pd


from numpy.random import randn
np.random.seed(101)

# Data frame serves as a data container object
df = pd.DataFrame(randn(5, 4), ["a", "b", "c", "d", "e"], [
                  "w", "x", "y", "z"])
print(f"Data frame \n{df}")

# Display one column
one_column = df["w"]
print(f"One column: \n{one_column}")

# Type
print(f"Tye of df['w']: \n{type(one_column)}")
print(f"Type of df: \n{type(df)}")

# Display two data use the column index as list
two_column_data = df[["w", "z"]]
print(f"Two data column index: \n{two_column_data}")

# New column and arithmetic ops
df["new"] = df["w"] + df["y"]
print(f"New column where df['w'] + df['y']: \n{df}")

# Drop
# print(df.drop("new"))
# //^^^ PRODUCES ERROR ^^^
df_new_drop = df.drop("new", axis=1)
print(f"Dropped 'new' column from Data frame: \n{df_new_drop}")

# Try drop["e"]
df_e_drop = df.drop("e")
print(f"Dropped 'e' series: \n{df_e_drop}")

# Try drop["e", axis=0]
df_e_ax0_drop = df.drop("e", axis=0)
print(f"Dropped ('e', axis = 0) series: \n{df_e_ax0_drop}")

# Shape
print(f"Data fram shape: \n{df.shape}")

# Series array row display
print(f"Series array row display: \n{df.loc['a']}")

# Index location of the series row display
print(f"Series indexed display: \n{df.iloc[1]}")

# df.drop("new", axis=1, inplace=True
df_drop_inplace = df.drop("new", axis=1, inplace=True)
print(f"Dropped: \n{df_drop_inplace}")

# df > 0 Useful for getting values
# Print Dataframe with true values and false based on bool 0 > 1
print(f"Data frame where  1 >  is true:\n{df > 0}")

# Print Dataframe with true values and false as NaN
boldf = df > 0
print(f"Data frame with NAN: \n{df[boldf]}")

# Data frames 12
print(f"df['w'] > 0: \n{df['w'] > 0}")

print(f"df[df['w'] > 0]: \n{df[df['w'] > 0]}")

print(f"(df[df['w'] > 0) & (df['y'] > 1)]: \n{(df['w'] > 0) & (df['y'] > 1)}")

# reset index
print(f"Reset index: \n{df.reset_index()}")

# Data frames 13
outside = ["G1", "G1", "G1", "G2", "G2", "G2"]
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df_2 = pd.DataFrame(randn(6, 2), hier_index, ["A", "B"])
print(f"Tuple to MultiIndex DF:\n{df_2}")

# df_2.loc["G1"].loc[1]
print(f"df_2.loc['G1'].loc[1]:\n{df_2.loc['G1'].loc[1]}")

# df_2.index.names['groups','nums']
# print(
#     f"df_2.index.names['groups','nums'] \n{df_2.index.names['groups','nums']}")
# //^^^ PRODUCES ERROR ^^^

# df_2.loc['G1'].loc[1]['B']
print(f"df_2.loc['G1'].loc[1]['B']:\n{df_2.loc['G1'].loc[1]['B']}")

# df_2.xs('G1')
print(f"df_2.xs('G1'):\n{df_2.xs('G1')}")

# df_2.xs(1,level='nums')
# print(f"df_2.xs(1,level='nums'):\n{df_2.xs(1,level='nums')}")
# //^^^ PRODUCES ERROR ^^^

# Missing Data
m_data = {
    "A": [1, 2, np.nan],
    "B": [5, np.nan, np.nan],
    "C": [1, 2, 3]
}
df_m = pd.DataFrame(m_data)
print(f"Missing data DF:\n{df_m}")

# df_m.dropna()
print(f"df_m.dropna():\n{df_m.dropna()}")

# df_m.dropna(axis=1)
print(f"df_m.dropna(axis=1):\n{df_m.dropna(axis=1)}")

# df_m.dropna(tresh=2)
# print(f"df_m.dropna(tresh=2):\n{df_m.dropna(tresh=2)}")
# //^^^ PRODUCES ERROR ^^^

# df_m.fillna(value='Fill Value')
print(f"df_m.fillna(value='Fill Value'):\n{df_m.fillna(value='Fill Value')}")

data = {
    "Company": ["Goog", "Goog", "MSFT", "MSFT", "FB", "FB"],
    "Person": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Sarah"],
    "Sales": [200, 120, 340, 124, 243, 350]
}
df_data = pd.DataFrame(data)
print(f"DF Data:\n{df_data}")

# Group by
by_company = df_data.groupby("Company")
print(f"Group by company:\n{by_company}")
