import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む（'your_file.csv'を実際のファイル名に置き換えてください）
df = pd.read_csv('gcf_data.csv')

# 2列目から最終列までを選択
data = df.iloc[:, 1:]

# カンマを削除して数値に変換
data = data.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',', ''), errors='coerce'))

# 相関係数行列を計算
correlation_matrix = data.corr()

# ヒートマップを作成
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title('相関係数行列')

# 画像を表示
plt.show()
