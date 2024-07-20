import pandas as pd

# CSVファイルを読み込む
file_path = "/Users/yusuketakahashi/dataAnalysis/data.csv"  # ファイルパスを適切に設定
data = pd.read_csv(file_path)

# 2~9列目を抽出する
selected_data = data.iloc[:, 1:9]

# 相関係数行列を計算する
correlation_matrix = selected_data.corr()

# 相関係数行列をCSVファイルに出力する
correlation_matrix.to_csv("correlation_matrix.csv", index=False)
