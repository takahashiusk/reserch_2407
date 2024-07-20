import csv
from bs4 import BeautifulSoup

# HTMLコンテンツを読み込み
with open('/mnt/data/view-source_https___www.furusato-tax.jp_gcf_2629.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# ページに「観光・PR」カテゴリーが含まれているか確認
category = soup.find('p', class_='gcf-lyt-detail__section--head__category')
if category and '観光・PR' in category.get_text():
    # 必要なデータを抽出
    donation_amount = soup.find('span', class_='gcf-amount')
    goal_amount = soup.find('span', class_='gcf-goal-amount')
    supporters_count = soup.find('span', class_='gcf-supporters-count')
    recruitment_period = soup.find('span', class_='gcf-recruitment-period')
    summary = soup.find('div', class_='gcf-summary')
    photo_count = len(soup.select('div.gcf-photos img'))

    # 要素が見つからない場合の処理
    donation_amount = donation_amount.get_text(strip=True) if donation_amount else 'N/A'
    goal_amount = goal_amount.get_text(strip=True) if goal_amount else 'N/A'
    supporters_count = supporters_count.get_text(strip=True) if supporters_count else 'N/A'
    recruitment_period = recruitment_period.get_text(strip=True) if recruitment_period else 'N/A'
    summary_length = len(summary.get_text(strip=True)) if summary else 0
    photo_count = photo_count if photo_count else 0

    # CSVを作成
    with open('/mnt/data/furusato_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['寄付金額', '目標金額', '支援人数', '寄付募集期間の日数', '概要の文字数', '写真の枚数'])
        writer.writerow([donation_amount, goal_amount, supporters_count, recruitment_period, summary_length, photo_count])

    print(f"寄付金額: {donation_amount}")
    print(f"目標金額: {goal_amount}")
    print(f"支援人数: {supporters_count}")
    print(f"寄付募集期間の日数: {recruitment_period}")
    print(f"概要の文字数: {summary_length}")
    print(f"写真の枚数: {photo_count}")
    print("データがCSVファイルに保存されました。")

else:
    print("観光・PRのカテゴリーが見つかりませんでした。")
