import pandas as pd
from pandas import DataFrame
import requests


#dart open api 인자
auth_key="2e915b536849f9c4f517c681d00833f8d83ac7ee" 
company_code=""


#excel 파일 읽기 (row : 200개)
xlsx = pd.read_excel('./corp_dataset.xlsx')
xlsx['largest shareholder'] = ''
#비율
trmend_posesn_stock_qota_rt = ''
for i in range(2):
    company_code = str(xlsx.code[i]).zfill(8)
    url = 'https://opendart.fss.or.kr/api/hyslrSttus.json?crtfc_key={}&corp_code={}&bsns_year=2020&reprt_code=11011'.format(auth_key, company_code)
    res = requests.get(url)
    data = res.json()
    share_list = data['list']
    print(share_list)
    print('')
    largest = 0

    for share in share_list:
        if share['stock_knd'] == '보통주':
            ratio = float(share['trmend_posesn_stock_qota_rt'])
            relative = share['relate']
            print('지분율 : {} 관계 :  {}'.format(ratio, relative))
                




