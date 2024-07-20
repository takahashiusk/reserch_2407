import os
import csv
from bs4 import BeautifulSoup

def extract_data_from_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    
    if not soup.find(class_="sorting-list__item", string=lambda text: text and "観光・PR" in text):
        return None

    data = {}

    # 寄付金額
    quantity = soup.find(class_="gcf-lyt-detail__quantity")
    data['寄付金額'] = quantity.text.strip() if quantity else ''

    # 達成率
    achievement = soup.find(class_="gcf-cht-detail-bar__number")
    data['達成率'] = achievement.text.strip().replace('%', '') if achievement else ''

    # 目標金額
    target_amount = soup.find(class_="gcf-lyt-detail__target-amount")
    data['目標金額'] = target_amount.text.strip() if target_amount else ''

    # 支援者数
    supporters_label = soup.find('span', class_='gcf-lyt-detail-total__title', string='支援人数')
    supporters = supporters_label.find_next('span', class_='gcf-lyt-detail-total__quantity') if supporters_label else None
    data['支援者数'] = supporters.text.strip() if supporters else ''

    # 期間
    period = soup.find(class_="mT16")
    if period:
        days = period.text.strip()
        data['期間'] = ''.join(filter(str.isdigit, days))
    else:
        data['期間'] = ''

    # 応援メッセージの件数
    messages = soup.find_all(class_="gcf-bx-message__text")
    data['応援メッセージの件数'] = len(messages)

    # 進捗情報
    progress = soup.find(class_="gcf-nv-tab__button-progress-number")
    data['進捗情報'] = progress.text.strip() if progress else ''

    # 説明文字数
    article = soup.find(class_="gcf-txt-article")
    data['説明文字数'] = len(article.text.strip()) if article else 0

    # お礼品の種類
    gifts = soup.find_all(class_="goods-col_price inline")
    data['お礼品の種類'] = len(gifts)

    # お礼品の最高額
    if gifts:
        max_gift = max(int(gift.text.strip().replace(',', '').replace('円', '')) for gift in gifts)
        data['お礼品の最高額'] = max_gift
    else:
        data['お礼品の最高額'] = ''

    # お礼品の最低額
    if gifts:
        min_gift = min(int(gift.text.strip().replace(',', '').replace('円', '')) for gift in gifts)
        data['お礼品の最低額'] = min_gift
    else:
        data['お礼品の最低額'] = ''

    # 説明に使われた画像の枚数
    images = len(soup.find_all(src=lambda src: src and (".jpg" in src or ".png" in src)))
    data['説明に使われた画像の枚数'] = images - len(gifts)

    return data

def main(folder_path, output_csv):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    data_list = []

    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            data = extract_data_from_html(content)
            if data:
                data['ファイル名'] = file
                data_list.append(data)

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ファイル名', '寄付金額', '達成率', '目標金額', '支援者数', '期間', '応援メッセージの件数', '進捗情報', '説明文字数', 'お礼品の種類', 'お礼品の最高額', 'お礼品の最低額', '説明に使われた画像の枚数']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for data in data_list:
            writer.writerow(data)

if __name__ == "__main__":
    folder_path = '/Users/yusuketakahashi/dataAnalysis/ffurusato_choice'  # フォルダのパスに置き換える
    output_csv = 'output2.csv'  # 出力するCSVファイル名
    main(folder_path, output_csv)
