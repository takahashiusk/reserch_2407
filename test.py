import numpy as np
import pandas as pd
import statsmodels.api as sm

fp="/Users/yusuketakahashi/dataAnalysis/data.csv"
data=pd.read_csv(fp)

#print(data)

# "rate of achievement" を目的変数として、その他の左側の項目を説明変数とする
X = data.iloc[:, 1:8]  # 最後の列以外を説明変数とする
y = data["rate of achievement"]  # "rate of achievement" を目的変数とする

# 定数項（Intercept）を追加する
X = sm.add_constant(X)

# 重回帰分析を行う
model = sm.OLS(y, X).fit()

# 分析結果を表示する
#print(model.summary())

# 分析結果をCSVファイルに出力する
with open("analysis_result2.csv", "w") as file:
    file.write(model.summary().as_csv())
 
print("OK")