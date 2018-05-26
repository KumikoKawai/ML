#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

args = sys.argv

#xlsxファイルからデータ読み込み
#pd.set_option('display.max_rows', 100)
data = pd.read_excel(args[1], usecols=[0, 6, 7, 10])
data.columns=['num', 'x', 'y', 'dont']

#ok部分とng部分を新しいDataFrameに抽出
df_ok = data[data.dont == 0].iloc[:,0:3]
df_ng = data[data.dont == 1].iloc[:,0:3]
ok_parse = list()
ng_parse = list()

plt.scatter(df_ok.x, df_ok.y, c='#00cc00')
plt.scatter(df_ng.x, df_ng.y, c='#cc0000')

plt.grid()
plt.show()

prev = 0
i = 0

#okとngのDataFrameの要素を連続したindexごとに区切る
while prev + i < len(df_ng):
    print('---')
    for i in range(len(df_ng)):
        if prev + i < len(df_ng):
            if i == 0:
                print(df_ng.iloc[prev+i,:])
            elif i >= 1:
                if int(df_ng.iloc[prev+i,:].num) == int(df_ng.iloc[prev+i-1,:].num) +1:
                    print(df_ng.iloc[prev+i,:])
                else:
                    prev = prev + i
                    break
