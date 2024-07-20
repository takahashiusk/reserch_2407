import pandas as pd
from sklearn.decomposition import PCA

# CSVファイルを読み込む
file_path = "/Users/yusuketakahashi/dataAnalysis/data.csv"  # ファイルパスを適切に設定
data = pd.read_csv(file_path)

# 2~9列目のデータを抽出する
selected_data = data.iloc[:, 1:9]
print(selected_data)

# 2~9列目の一行目の項目名を取得する
column_names = list(data.columns[1:9])

# 主成分分析を実行する
pca = PCA()
pca.fit(selected_data)

#主成分の固有ベクトル
loadings = pd.DataFrame(pca.components_.T)
print(loadings) 

# 固有値を取得する
eigenvalues = pca.explained_variance_

# 寄与率を計算する
variance_ratio = pca.explained_variance_ratio_

# 累積寄与率を計算する
cumulative_variance_ratio = variance_ratio.cumsum()

# 主成分名を取得する
component_names = [f'{column_names[i]}' for i in range(selected_data.shape[1])]

# 結果をDataFrameにまとめる
result_df = pd.DataFrame({
    'Component': component_names,
    'Eigenvalue': eigenvalues,
    'Variance Ratio': variance_ratio,
    'Cumulative Variance Ratio': cumulative_variance_ratio
})

# 寄与率の大きい順に並び替える
result_df = result_df.sort_values(by='Variance Ratio', ascending=False)

# 結果をCSVファイルに出力する
result_df.to_csv("pca_results.csv", index=False)
