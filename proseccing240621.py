import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('output3.csv')

# 2列目のカンマをすべて削除する
df.iloc[:, 1] = df.iloc[:, 1].str.replace(',', '')

# 4列目の「目標金額：」を削除して数字部分のみを抽出する
df.iloc[:, 3] = df.iloc[:, 3].str.replace('目標金額：', '')

# 6列目の下二桁の数字のみを抽出し半角数字に置換する
df.iloc[:, 5] = df.iloc[:, 5].apply(lambda x: str(x)[-2:]).astype(str)

# 処理後のデータを新しいCSVファイルとして保存する
output_csv_path = 'processed_data.csv'
df.to_csv(output_csv_path, index=False, encoding='utf-8-sig')

print("CSVデータの処理と保存が完了しました。")
