import numpy as np
import pandas as pd
import math

# you can use this table as an example
distr_table = pd.DataFrame(
    {"X": [0, 0, 1, 1], "Y": [1, 2, 1, 2], "pr": [0.3, 0.25, 0.15, 0.3]}
)


class CheckIndependence:
    def __init__(self):
        self.version = 1

    def check_independence(self, df: pd.DataFrame) -> dict:
        # write your solution here
        res = {}

        res["are_independent"] = self._are_independent(df)

        res["cov"] = self._cov(df)
        res["corr"] = res["cov"] / self._corr(df)

        return res

    def _corr(self, df: pd.DataFrame) -> float:
        # calcaute p
        x = df.groupby("X", as_index=False).pr.sum()
        y = df.groupby("Y", as_index=False).pr.sum()
        xy_tab = pd.merge(x, y, how="cross")

        # calculate mu
        xy_tab["mu_x"] = xy_tab["X"] * xy_tab["pr_x"]
        xy_tab["mu_y"] = xy_tab["Y"] * xy_tab["pr_y"]

        sig_x = (xy_tab["pr_x"] * ((xy_tab["X"] - xy_tab["mu_x"]) ** 2)).sum() ** 0.5
        sig_y = (xy_tab["pr_y"] * ((xy_tab["Y"] - xy_tab["mu_y"]) ** 2)).sum() ** 0.5

        return sig_x * sig_y

    def _cov(self, df: pd.DataFrame) -> float:

        # calcaute p
        x = df.groupby("X", as_index=False).pr.sum()
        y = df.groupby("Y", as_index=False).pr.sum()
        xy_tab = pd.merge(x, y, how="cross")

        # calculate mu
        xy_tab["mu_x"] = xy_tab["X"] * xy_tab["pr_x"]
        xy_tab["mu_y"] = xy_tab["Y"] * xy_tab["pr_y"]
        # print(xy_tab)
        # covariance equation
        res = (
            df["pr"] * (xy_tab["X"] - xy_tab["mu_x"]) * (xy_tab["Y"] - xy_tab["mu_y"])
        ).sum()

        return res

    def _are_independent(self, df: pd.DataFrame) -> bool:

        # x,y unique element
        X_uniq = df["X"].unique()
        Y_uniq = df["Y"].unique()

        # calculate x,y cor prob
        x = df.groupby("X", as_index=False).pr.sum()
        y = df.groupby("Y", as_index=False).pr.sum()
        xy_tab = pd.merge(x, y, how="cross")
        xy_tab["ind_pr"] = xy_tab["pr_x"] * xy_tab["pr_y"]

        xy_tab = xy_tab[["X", "Y", "ind_pr"]].merge(df, on=["X", "Y"])

        return xy_tab["ind_pr"].equals(xy_tab["pr"])
