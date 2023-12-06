#ライブラリインポート
from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas as pd
import time
import re

#書き込み用のファイルを開く
fileName = 'test.txt'
file = open(fileName, 'w', encoding='utf-8')

#URLリストのファイルから読み込み
r_filepath = './urllist.txt'
with open(r_filepath, "r", encoding="utf-8") as f:
    for line in f:
        #urlを指定する
        url=line.rstrip('\n')
        #HTMLを取得する
        print('reading', url, '...')
        r=requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        content = soup.find_all('table')
        s_content= content[2]
        r_content=''.join(str(s_content).splitlines())
        #ファイルに書き込む
        print('writing', url, '...','\n')
        file.write(str(r_content))
        file.write('\n')

#終了処理・通知
file.close()
print('fin')
