# -*- coding: utf-8 -*-
"""
Description
"""

__version__ = '0.1'
__author__ = ''

import traceback
import logging

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class DataLoaderService:
    def __init__(self) -> None:
        super().__init__()
        self.xl = None

    def load_sheet_names(self):
        file_path = "./resources/raw_data/data.xls"
        self.xl = pd.ExcelFile(file_path)

    def pcg_mf_pop(self):
        df = self.xl.parse("pcgmale-female pop16")
        df = df.T
        df.reset_index(inplace=True)
        df.rename(columns={0: "pop"}, inplace=True)
        df.dropna(axis=0, inplace=True)
        return df

    def pcg_stats_16(self):
        df = self.xl.parse("pcgstats2016")
        df.dropna(axis=0, inplace=True)
        return df

    def pcg_mem_agents_16(self):
        df = self.xl.parse("pcgmem-agents16")
        df = df.T
        df.reset_index(inplace=True)
        df.rename(columns={0: "pop"}, inplace=True)
        df.dropna(axis=0, inplace=True)
        return df

    def agents_comp_16(self):
        df = self.xl.parse("agentscomp-16")
        df.dropna(axis=0, inplace=True)
        return df

    def comm_pcgmem_16(self):
        df = self.xl.parse("comm-pcgmem16")
        df = df.T
        df.reset_index(inplace=True)
        df.rename(columns={0: "pop"}, inplace=True)
        df.dropna(axis=0, inplace=True)
        return df

    def ppastors_16(self):
        df = self.xl.parse("ppastors2016")
        df.dropna(axis=0, inplace=True)
        return df

    def pcg_ghana_16(self):
        df = self.xl.parse("pcg-ghana16")
        df = df.T
        df.reset_index(inplace=True)
        df.rename(columns={0: "pop"}, inplace=True)
        df.dropna(axis=0, inplace=True)
        return df

    def chythatd16(self):
        df = self.xl.parse("chythadt16")
        df.dropna(axis=0, inplace=True)
        return df

    def pcg_growth_16_15(self):
        df = self.xl.parse("pcggrowth 16&15")
        df.dropna(axis=0, inplace=True)
        return df

    def adtnonadt_16(self):
        df = self.xl.parse("adtnonadt16")
        df.dropna(axis=0, inplace=True)
        return df

    def ann_trd_child_16(self):
        df = self.xl.parse("anntrdchild16")
        X = df["Year"]
        Y = df["Population"]
        reg = LinearRegression().fit(np.vstack(X), Y)
        df['bestfit'] = reg.predict(np.vstack(X))
        df.dropna(axis=0, inplace=True)
        return df

    def ann_trd_jy_16(self):
        df = self.xl.parse("anntrdjy16")
        X = df["Year"]
        Y = df["Population"]
        reg = LinearRegression().fit(np.vstack(X), Y)
        df['bestfit'] = reg.predict(np.vstack(X))
        df.dropna(axis=0, inplace=True)
        return df

    def ann_trd_ypg_16(self):
        df = self.xl.parse("anntrdypg16")
        X = df["Year"]
        Y = df["Population"]
        reg = LinearRegression().fit(np.vstack(X), Y)
        df['bestfit'] = reg.predict(np.vstack(X))
        df.dropna(axis=0, inplace=True)
        return df

    def ann_trd_yaf_16(self):
        df = self.xl.parse("anntrdyaf16")
        X = df["Year"]
        Y = df["Population"]
        reg = LinearRegression().fit(np.vstack(X), Y)
        df['bestfit'] = reg.predict(np.vstack(X))
        df.dropna(axis=0, inplace=True)
        return df

    def ann_trd_adlt_16(self):
        df = self.xl.parse("anntrdadlt16")
        X = df["Year"]
        Y = df["Population"]
        reg = LinearRegression().fit(np.vstack(X), Y)
        df['bestfit'] = reg.predict(np.vstack(X))
        df.dropna(axis=0, inplace=True)
        return df

    def ann_stats_01_16(self):
        df = self.xl.parse("annstats01-16")
        X = df["Year"]
        Y = df["Population"]
        reg = LinearRegression().fit(np.vstack(X), Y)
        df['bestfit'] = reg.predict(np.vstack(X))
        df.dropna(axis=0, inplace=True)
        return df

    def ann_trend_01_16(self):
        df = self.xl.parse("anntrend01-16")
        df.dropna(axis=0, inplace=True)
        return df

    def gen_growth_21(self):
        df = self.xl.parse("gen_growth_21")
        df.dropna(axis=0, inplace=True)
        return df

    def vision(self):
        df = self.xl.parse("vision_15")
        df['Growth Rate'] = df['Growth Rate'] * 100
        df.dropna(axis=0, inplace=True)
        return df

