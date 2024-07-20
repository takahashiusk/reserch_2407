import requests #requestsライブラリをインポート
import os #osへのインターフェースモジュールをインポート
import time #timeモジュールで実行時間の管理
import pyautogui #pythonで勝手にマウスを制御するライブラリをインポートする

def fetch_and_save_html(url, save_dir): #この関数を作ることでステータスコードの処理を行う
    try:
        # HTTPリクエストを送信してレスポンスを取得
        response = requests.get(url)
        
        # ステータスコードが200番台の場合のみ処理を続行
        if response.status_code // 100 == 2:
            # レスポンスからHTMLコンテンツを取得
            html_content = response.text
            
            # URLからファイル名を生成
            file_name = os.path.join(save_dir, url.split('/')[-1])
            
            # HTMLファイルを保存
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"Saved HTML from {url} to {file_name}")
        else:
            print(f"Failed to fetch HTML from {url}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred while fetching {url}: {e}")

# 保存ディレクトリを指定
save_directory = '/Users/yusuketakahashi/dataAnalysis/ffurusato_choice'

# ディレクトリが存在しない場合は作成
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# ベースURLを指定（URLのナンバリング部分を除く）
base_url = 'https://www.furusato-tax.jp/gcf/'  # 例: https://example.com/page_1, https://example.com/page_2, ...

# ナンバリングされたURLをループで処理
for i in range(1, 2923): #2923の部分に必要な数を代入する
    # フルURLを生成
    url = f"{base_url}{i}"  # 例: https://example.com/page_1.html
    
    # HTMLを取得して保存
    fetch_and_save_html(url, save_directory)
    print(f"{i}件めの処理完了") #fを先頭につけることで、iという変数との関連をつける
    
    # マウスを動かしてスリープモードに入ることを防止
    pyautogui.moveRel(1, 0)  # 1ピクセル右に移動
    time.sleep(0.1)         # 少し待機
    pyautogui.moveRel(-1, 0) # 1ピクセル左に戻る

    # 次のリクエストまで5秒待機
    time.sleep(5)
