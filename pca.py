import pandas as pd
from sklearn.decomposition import PCA

# CSVファイルを読み込む
file_path = "/Users/yusuketakahashi/dataAnalysis/data.csv"  # ファイルパスを適切に設定
data = pd.read_csv(file_path)

# 2~9列目のデータを抽出する
selected_data = data.iloc[:, 1:9]

# 主成分分析を行う
pca = PCA()
print(dir(pca))
pca.fit(selected_data)

# 主成分分析の結果をDataFrameに変換する
pca_result = pd.DataFrame(pca.components_, columns=selected_data.columns)

# 結果をCSVファイルに出力する
#pca_result.to_csv("pca_result.csv", index=False)
