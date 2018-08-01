#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm, metrics, preprocessing, model_selection #機械学習用のライブラリを利用
from mlxtend.plotting import plot_decision_regions #学習結果をプロットする外部ライブラリを利用
import sys
import ssl

from sklearn.feature_extraction.text import CountVectorizer
np.set_printoptions(threshold=np.inf)

#read gaze data file
args = sys.argv
df_gaze=pd.read_csv(args[1], header=None)
#df_gaze=pd.read_csv('/Users/kawaikumiko/Desktop/ML_data/signals.csv', header=None)
df_gaze.columns = [u'gaze', u'mis']

#vecrorize
vectorizer = CountVectorizer(ngram_range=(4,4), token_pattern=u'(?u)\\b\\w+\\b', lowercase=False)
X = vectorizer.fit_transform(df_gaze["gaze"])
z=df_gaze["mis"]

#解説 5：機械学習で分類する---------------------------------------------------
clf_result=svm.LinearSVC(loss='hinge', C=1.0,class_weight='balanced', random_state=0)#loss='squared_hinge' #loss="hinge", loss="log"
clf_result.fit(X[1:], z[1:])

# 6：K分割交差検証（cross validation）で性能を評価する---------------------
scores=model_selection.cross_val_score(clf_result, X[1:], z[1:], cv=10)
print("平均正解率 = ", scores.mean())
print("正解率の標準偏差 = ", scores.std())

# 7：トレーニングデータとテストデータに分けて実行してみる------------------
X_train, X_test, train_label, test_label=model_selection.train_test_split(X[1:],z[1:], test_size=0.1, random_state=0)
clf_result.fit(X_train, train_label)
#正答率を求める
pre=clf_result.predict(X_test)
#print(pre)
#print(test_label)
ac_score=metrics.accuracy_score(test_label,pre)
print("正答率 = ",ac_score)
print(metrics.confusion_matrix(test_label, pre))

# 8：任意のデータに対する識別結果を見てみる------------------
#先頭1件を識別
predicted_label=clf_result.predict(X[1])
print("このテストデータのラベル = ", predicted_label)

# 9：識別平面の式を手に入れる--------------------------------
#切片
#print(clf_result.intercept_)
#偏回帰係数
#print(clf_result.coef_ )  #coef[0]*x+coef[1]*y+intercept=0
