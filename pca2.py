import pandas as pd
from sklearn.decomposition import PCA

# CSVファイルを読み込む
file_path = "/Users/yusuketakahashi/dataAnalysis/data.csv"  # ファイルパスを適切に設定
data = pd.read_csv(file_path)

# 2~9列目のデータを抽出する
selected_data = data.iloc[:, 1:9]

# 主成分分析を実行する
pca = PCA()
pca.fit(selected_data)

# 固有値を取得する
eigenvalues = pca.explained_variance_

# 寄与率を計算する
variance_ratio = pca.explained_variance_ratio_

# 累積寄与率を計算する
cumulative_variance_ratio = variance_ratio.cumsum()

# 結果をDataFrameにまとめる
result_df = pd.DataFrame({
    'Eigenvalue': eigenvalues,
    'Variance Ratio': variance_ratio,
    'Cumulative Variance Ratio': cumulative_variance_ratio
})

# 寄与率の大きい順に並び替える
result_df = result_df.sort_values(by='Variance Ratio', ascending=False)

# 結果をCSVファイルに出力する
result_df.to_csv("pca2_results.csv", index=False)
