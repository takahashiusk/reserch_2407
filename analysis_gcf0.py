import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from matplotlib import font_manager

# 日本語フォントの設定
font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc'  # ここに日本語フォントのパスを指定してください
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# CSVファイルを読み込む
file_path = 'gcf_data.csv'  # ここにCSVファイルのパスを指定してください
output_dir = 'output_images'  # 画像を保存するディレクトリのパスを指定してください

# ディレクトリが存在しない場合は作成
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(file_path)

# 2列目以降の列名を取得
columns = df.columns[1:]

# 2列目以降の全ての列の組み合わせを取得
combinations_of_columns = list(combinations(columns, 2))

# 散布図を生成
for col1, col2 in combinations_of_columns:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=col1, y=col2)
    plt.title(f'{col1} と {col2} の散布図', fontproperties=font_prop)
    plt.xlabel(col1, fontproperties=font_prop)
    plt.ylabel(col2, fontproperties=font_prop)
    plt.grid(True)
    # 画像として保存
    plt.savefig(os.path.join(output_dir, f'scatter_{col1}_{col2}.png'))
    plt.close()

print(f"散布図はすべて {output_dir} に保存されました。")
