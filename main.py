from selenium import webdriver
from selenium.webdriver.common.by import By

# x. Chrome の起動オプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# x. ブラウザの新規ウィンドウを開く
print('connectiong to remote browser...')
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options,
)

# 1. Qiita の Chanmoro のプロフィールページにアクセスする
driver.get('https://qiita.com/Hirochon')
print(driver.current_url)
# > https://qiita.com/Chanmoro

# 2. 「最近の記事」に表示されている記事一覧の 2 ページ目に移動する
driver.find_element(By.XPATH, '//a[@class="css-2p454n" and text()="実例から学ぼう！競プロの最悪な歩み方"]').click()
print(driver.current_url)
# > https://qiita.com/Chanmoro?page=2

# 3. 2 ページ目の一番最初に表示されている記事のタイトルを URL を取得する
article_title = driver.find_elements(By.XPATH, '//h1[@class="css-8py6gv"]')
print(article_title[0].text)

# x. ブラウザを終了する
driver.quit()