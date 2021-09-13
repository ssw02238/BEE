import pandas as pd
from pandas import DataFrame
import requests
import pprint

#특수 관계인 정리
relative_list = [
    "최대주주",
    "본인",
    "본인(최대주주)",
    "최대주주본인",
    "본인및특별관계자",
    "본인및특수관계인",
    "최대주주(본인)",
    "최대주주의최대주주",
    "특수",
    "특수관계",
    "특수관계인",
    "기타특수관계인",
    "최대주주의특별관계자",
    "최대주주의특수관계인",
    "최대주주의직계비속",
    "최대주주의친인척",
    "최대주주의혈족6촌",
    "최대주주의배우자",
    "최대주주의모",
    "최대주주의부",
    "최대주주의자",
    "최대주주의형제",
    "최대주주의매제",
    "최대주주의매",
    "최대주주의제",
    "최대주주의처", 
    "최대주주제의자",
    "최대주주매의자",
    "최대주주의兄",
    "최대주주의父",
    "자녀",
    "배우자",
    "형제자매",
    "친족",
    "친인척",
    "임원\n(친인척)"
    "혈족1촌", 
    "혈족2촌", 
    "혈족3촌", 
    "혈족5촌", 
    "6촌이내의혈족",
    "4촌이내의인척",
    "제",
    "매",
    "조카",
    "사위",
    "숙부",
    "자",
    "처",
    "계열회사",
    "계열사",
    "최대주주의특수관계법인",
    "최대주주의계열회사",
    "최대주주의계열비영리법인",
    "최대주주의계 비영리법인",
    "지배회사",
    "모회사",
    "대표이사"
]

#dart open api 인자
auth_key="2e915b536849f9c4f517c681d00833f8d83ac7ee" 
company_code=""


#excel 파일 읽기 (row : 200개)
xlsx = pd.read_excel('./corp_dataset.xlsx')
xlsx['largest shareholder'] = ''


#비율
trmend_posesn_stock_qota_rt = ''
for i in range(200):
    print('')
    company_name = str(xlsx.name[i])
    print(company_name)
    reprt_code = 11011
    company_code = str(xlsx.code[i]).zfill(8)
    url = 'https://opendart.fss.or.kr/api/hyslrSttus.json?crtfc_key={}&corp_code={}&bsns_year=2020&reprt_code={}'.format(auth_key, company_code, reprt_code)
    res = requests.get(url)
    data = res.json()
    
    if data['status'] == '013':
        while reprt_code < 11015:
            reprt_code += 1
            url = 'https://opendart.fss.or.kr/api/hyslrSttus.json?crtfc_key={}&corp_code={}&bsns_year=2020&reprt_code={}'.format(auth_key, company_code, reprt_code)
            res = requests.get(url)
            data = res.json()
            if data['status'] != '013':
                break

    largest = 0
    if data.get('list'):
        share_list = data['list']
        for share in share_list:
            type = share['stock_knd'].replace(" ", "")
            type = type.replace("\n", "")
            if type == '보통주' or type == '보통주식' or type == '의결권있는주식' or type == '의결권이있는주식' or type == '의결권있는보통주' or type == '의결권있는주식(보통주)' or type == '보통주(의결권있음)':
                if share['trmend_posesn_stock_qota_rt'] == '-':
                    ratio = 0
                else:
                    ratio = float(share['trmend_posesn_stock_qota_rt'])

                relative = share.get('relate')
                if relative:
                    relative = relative.replace(" ", "")
                    relative = relative.replace("\n", "")

                if relative in relative_list:
                    largest += ratio
    
    print('최대주주 및 특수관계인 지분율 : {}'.format(round(largest, 2)))