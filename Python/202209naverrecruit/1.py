from math import sqrt
import pandas as pd

# you can use this table as an example
df = pd.DataFrame({"X": [0, 0, 1, 1], "Y": [1, 2, 1, 2], "pr": [0.3, 0.25, 0.15, 0.3]})

# x_0, x_1 = distr_table.groupby("X").pr.sum()
# y_1, y_2 = distr_table.groupby("Y").pr.sum()

# x_u = distr_table.X.unique()
# y_u = distr_table.Y.unique()
# for index, row in distr_table.iterrows():
#     print(row['X'], row['Y'], row['pr'])

# cmp = pd.merge(distr_table.groupby('X', as_index=False)['pr'].sum(), distr_table.groupby('Y', as_index=False)['pr'].sum(), how='cross')
# cmp['indep_pr'] = cmp['pr_x'] * cmp['pr_y']
# print(cmp)

# x = df.groupby("X", as_index=False).pr.sum()
# y = df.groupby("Y", as_index=False).pr.sum()
# xy_tab = pd.merge(x, y, how="cross")
# xy_tab["mu_x"] = xy_tab["X"] * xy_tab["pr_x"]
# xy_tab["mu_y"] = xy_tab["Y"] * xy_tab["pr_y"]
# print(df["pr"])
# print((xy_tab["X"] - xy_tab["mu_x"]))
# print((xy_tab["Y"] - xy_tab["mu_y"]))
# print(df["pr"] * (xy_tab["X"] - xy_tab["mu_x"]) * (xy_tab["Y"] - xy_tab["mu_y"]))

# print(
#     (df["pr"] * (xy_tab["X"] - xy_tab["mu_x"]) * (xy_tab["Y"] - xy_tab["mu_y"])).sum()
# )
# calcaute p
x = df.groupby("X", as_index=False).pr.sum()
y = df.groupby("Y", as_index=False).pr.sum()
xy_tab = pd.merge(x, y, how="cross")

# calculate mu
xy_tab["mu_x"] = xy_tab["X"] * xy_tab["pr_x"]
xy_tab["mu_y"] = xy_tab["Y"] * xy_tab["pr_y"]

# print(xy_tab)
# print((xy_tab["pr_x"] * (xy_tab["X"] - xy_tab["mu_x"]) ** 2).sum() **0.5)
# print(sqrt((xy_tab["pr_x"] * (xy_tab["X"] - xy_tab["mu_x"]) ** 2).sum()))

print(df[["X", "Y"]].cov())
# calcaute p
x = df.groupby("X", as_index=False).pr.sum()
y = df.groupby("Y", as_index=False).pr.sum()
xy_tab = pd.merge(x, y, how="cross")

# calculate mu
xy_tab["mu_x"] = xy_tab["X"] * xy_tab["pr_x"]
xy_tab["mu_y"] = xy_tab["Y"] * xy_tab["pr_y"]

# covariance equation
res = df["pr"] * (xy_tab["X"] - xy_tab["mu_x"]) * (xy_tab["Y"] - xy_tab["mu_y"])
print()
