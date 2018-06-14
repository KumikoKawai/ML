#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, metrics, preprocessing, model_selection
from mlxtend.plotting import plot_decision_regions
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
args = sys.argv

#解説 2：Reading dataset of gaze pattern--------------------------------
#use x(col 6), y(col 7),misunderstand(10)
df_gaze=pd.read_excel(args[1], usecols=[6, 7, 10])
df_gaze.columns = ['x', 'y', 'mis']
pd.DataFrame(df_gaze)  #この行を実行するとデータが見れる

x=df_gaze["x"]
y=df_gaze["y"]
z=df_gaze["mis"]
plt.scatter(x,y, c=z)
plt.show()

#解説 4：データの整形-------------------------------------------------------
X=df_gaze[["x","y"]]

###---Sample---###
"""
df_wine_all=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
#品種(0列、1～3)と色（10列）とプロリンの量(13列)を使用する
df_wine=df_wine_all[[0,10,13]]
df_wine.columns = [u'class', u'color', u'proline']
pd.DataFrame(df_wine)  #この行を実行するとデータが見れる

#解説 3：プロットしてみる------------------------------------------------------

x=df_wine["color"]
y=df_wine["proline"]
z=df_wine["class"]-1
plt.scatter(x,y, c=z)
plt.show()

#解説 4：データの整形-------------------------------------------------------
X=df_wine[["color","proline"]]
"""
###---Sample end---###

sc=preprocessing.StandardScaler()
sc.fit(X)
X_std=sc.transform(X)

#解説 5：機械学習で分類する---------------------------------------------------
clf_result=linear_model.SGDClassifier(loss="hinge", max_iter=1000) #loss="hinge", loss="log"


#解説 6：K分割交差検証（cross validation）で性能を評価する---------------------
scores=model_selection.cross_val_score(clf_result, X_std, z, cv=10)
print("平均正解率 = ", scores.mean())
print("正解率の標準偏差 = ", scores.std())

#解説 7：トレーニングデータとテストデータに分けて実行してみる------------------
X_train, X_test, train_label, test_label=model_selection.train_test_split(X_std,z, test_size=0.1, random_state=0)
clf_result.fit(X_train, train_label)
#正答率を求める
pre=clf_result.predict(X_test)
ac_score=metrics.accuracy_score(test_label,pre)
print("正答率 = ",ac_score)
#plotする
X_train_plot=np.vstack(X_train)
train_label_plot=np.hstack(train_label)
X_test_plot=np.vstack(X_test)
test_label_plot=np.hstack(test_label)
plot_decision_regions(X_train_plot, train_label_plot, clf=clf_result, res=0.01) #学習データをプロット
plt.show()
plot_decision_regions(X_test_plot, test_label_plot, clf=clf_result, res=0.01, legend=2) #テストデータをプロット
plt.show()

#解説 8：任意のデータに対する識別結果を見てみる------------------
predicted_label=clf_result.predict([[1,-1]])
print("このテストデータのラベル = ", predicted_label)

#解説 9：識別平面の式を手に入れる--------------------------------
print(clf_result.intercept_)
print(clf_result.coef_ )  #coef[0]*x+coef[1]*y+intercept=0
