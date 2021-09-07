import pandas as pd
from pandas import DataFrame
import requests


#dart open api 인자
auth_key="2e915b536849f9c4f517c681d00833f8d83ac7ee" 
company_code=""


#excel 파일 읽기 (row : 200개)
xlsx = pd.read_excel('./corp_dataset.xlsx')
xlsx['board_ratio'] = ''

for i in range(2):
    company_code = str(xlsx.code[i]).zfill(8)
    url = 'https://opendart.fss.or.kr/api/exctvSttus.json?crtfc_key={}&corp_code={}&bsns_year=2020&reprt_code=11011'.format(auth_key, company_code)
    res = requests.get(url)
    data = res.json()
    board_list = data['list']
    total_num = len(board_list)
    out_num = 0
    percent = 0
    print(data)
    for info in board_list:
        if info['ofcps'] == "사외이사":
            out_num += 1
    percent = (out_num / total_num) * 100 
    print(percent)


