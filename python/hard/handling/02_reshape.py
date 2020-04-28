# -*- coding: utf-8 -*-
"""
DataFrame의 모양 변경
"""

import pandas as pd

buy = pd.read_csv("buy_data.csv", encoding="utf-8")
buy.info()
buy.shape

type(buy)
buy

# 1. row -> column
buy_long = buy.stack()
buy_long.shape
buy_long[0]

# 2. column -> row
buy_wide = buy_long.unstack()
buy_wide

# 3. transpose
wide_t = buy_wide.T
wide_t

# 4. 중복 행 제거
buy_df = buy.drop_duplicates()
buy_df.shape
