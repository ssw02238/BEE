import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bee.settings')
django.setup()

from corporates.models import News, Corporate, Environment, Social, Governance
from decouple import config
import pandas as pd

from bs4 import BeautifulSoup
import datetime
import requests
from django.db.models import Q

import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import gluonnlp as nlp
import numpy as np
from tqdm import tqdm as tqdm

#kobert
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model

#transformers
from transformers import AdamW
from transformers.optimization import get_cosine_schedule_with_warmup

# CPU 사용
device = torch.device("cpu")

#BERT 모델, Vocabulary 불러오기
bertmodel, vocab = get_pytorch_kobert_model()

# 기본 Bert tokenizer 사용
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

# Setting parameters
# 학습을 위한 parameters
max_len = 64
batch_size = 64
warmup_ratio = 0.1
num_epochs = 6
max_grad_norm = 1
log_interval = 200
learning_rate =  5e-5

# 데이터셋 정의
class BERTDataset(Dataset):
    def __init__(self, dataset, sent_idx, label_idx, bert_tokenizer, max_len,
                 pad, pair):
        transform = nlp.data.BERTSentenceTransform(
            bert_tokenizer, max_seq_length=max_len, pad=pad, pair=pair)

        self.sentences = [transform([i[sent_idx]]) for i in dataset]
        self.labels = [np.int32(i[label_idx]) for i in dataset]

    def __getitem__(self, i):
        return (self.sentences[i] + (self.labels[i], ))

    def __len__(self):
        return (len(self.labels))

# 이진분류모델
class BERTClassifier(nn.Module):
    def __init__(self,
                 bert,
                 hidden_size = 768,
                 num_classes = 2,
                 dr_rate=None,
                 params=None):
        super(BERTClassifier, self).__init__()
        self.bert = bert
        self.dr_rate = dr_rate
                 
        self.classifier = nn.Linear(hidden_size , num_classes)
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)
    
    def gen_attention_mask(self, token_ids, valid_length):
        attention_mask = torch.zeros_like(token_ids)
        for i, v in enumerate(valid_length):
            attention_mask[i][:v] = 1
        return attention_mask.float()

    def forward(self, token_ids, valid_length, segment_ids):
        attention_mask = self.gen_attention_mask(token_ids, valid_length)
        
        _, pooler = self.bert(input_ids = token_ids, token_type_ids = segment_ids.long(), attention_mask = attention_mask.float().to(token_ids.device))
        if self.dr_rate:
            out = self.dropout(pooler)
        return self.classifier(out)

# 다중분류모델
class BERTClassifier2(nn.Module):
    def __init__(self,
                 bert,
                 hidden_size = 768,
                 num_classes = 3,
                 dr_rate=None,
                 params=None):
        super(BERTClassifier2, self).__init__()
        self.bert = bert
        self.dr_rate = dr_rate
                 
        self.classifier = nn.Linear(hidden_size , num_classes)
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)
    
    def gen_attention_mask(self, token_ids, valid_length):
        attention_mask = torch.zeros_like(token_ids)
        for i, v in enumerate(valid_length):
            attention_mask[i][:v] = 1
        return attention_mask.float()

    def forward(self, token_ids, valid_length, segment_ids):
        attention_mask = self.gen_attention_mask(token_ids, valid_length)
        
        _, pooler = self.bert(input_ids = token_ids, token_type_ids = segment_ids.long(), attention_mask = attention_mask.float().to(token_ids.device))
        if self.dr_rate:
            out = self.dropout(pooler)
        return self.classifier(out)

# 모델 설정
e_model = BERTClassifier(bertmodel, dr_rate=0.5).to(device)
s_model = BERTClassifier(bertmodel, dr_rate=0.5).to(device)
g_model = BERTClassifier(bertmodel, dr_rate=0.5).to(device)
v_model = BERTClassifier2(bertmodel, dr_rate=0.5).to(device)

# 모델 로드
e_model.load_state_dict(torch.load("./data/model/e_model.pt", map_location=device))
s_model.load_state_dict(torch.load("./data/model/s_model.pt", map_location=device))
g_model.load_state_dict(torch.load("./data/model/g_model.pt", map_location=device))
v_model.load_state_dict(torch.load("./data/model/v_model.pt", map_location=device))

# 평가모드 설정
e_model.eval()
s_model.eval()
g_model.eval()
v_model.eval()


def check_e(title): # E 체크
    pdData = [[title, 5]] # 데이터 형식 맞추기 위해 int형 아무거나 설정
    test_set = BERTDataset(pdData, 0, 1, tok, max_len, True, False) 
    # Colab에선 되는데 여기선 num_workers = 0 으로 안하면 에러발생
    test_input = torch.utils.data.DataLoader(test_set, batch_size=batch_size, num_workers=0) 
    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_input):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)
        valid_length= valid_length 
        label = label.long().to(device)
        # 이때, out이 예측 결과 리스트
        e_test_out = e_model(token_ids, valid_length, segment_ids)
        logits = e_test_out[0]
        
        # 연산 기록으로 부터 분리한 tensor을 반환
        logits = logits.detach().cpu().numpy()

        # np.argmax = 배열에서 큰 값 index 반환
        if np.argmax(logits) == 0:
            return 0
        elif np.argmax(logits) == 1:
            return 1


def check_s(title): # S 체크
    pdData = [[title, 5]]
    test_set = BERTDataset(pdData, 0, 1, tok, max_len, True, False) 
    test_input = torch.utils.data.DataLoader(test_set, batch_size=batch_size, num_workers=0)
    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_input):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)
        valid_length= valid_length 
        label = label.long().to(device)
        # 이때, out이 예측 결과 리스트
        s_test_out = s_model(token_ids, valid_length, segment_ids)

        logits = s_test_out[0]
        logits = logits.detach().cpu().numpy()

        if np.argmax(logits) == 0:
            return 0
        elif np.argmax(logits) == 1:
            return 1


def check_g(title):
    pdData = [[title, 5]]
    test_set = BERTDataset(pdData, 0, 1, tok, max_len, True, False) 
    test_input = torch.utils.data.DataLoader(test_set, batch_size=batch_size, num_workers=0)
    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_input):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)
        valid_length= valid_length 
        # 이때, out이 예측 결과 리스트
        g_test_out = g_model(token_ids, valid_length, segment_ids)

        logits = g_test_out[0]
        logits = logits.detach().cpu().numpy()

        if np.argmax(logits) == 0:
            return 0
        elif np.argmax(logits) == 1:
            return 1


def check_v(title):
    pdData = [[title, 5]]
    test_set = BERTDataset(pdData, 0, 1, tok, max_len, True, False) 
    test_input = torch.utils.data.DataLoader(test_set, batch_size=batch_size, num_workers=0)
    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_input):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)
        valid_length= valid_length 
        # 이때, out이 예측 결과 리스트
        v_test_out = v_model(token_ids, valid_length, segment_ids)

        logits = v_test_out[0]
        logits = logits.detach().cpu().numpy()

        if np.argmax(logits) == 0:
            return 0
        elif np.argmax(logits) == 1:
            return 1
        elif np.argmax(logits) == 2:
            return 2


months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def search_news_data():
    # 기업 리스트 불러오기
    corps = pd.read_excel("./data/기업정보.xlsx")
    corp_names = corps["종목명"]
    keyword = ''
    
    # 관련도 높은 순으로 100개 검색
    display = 100
    start = 1

    # .env에 Secret key설정
    id = config('X_Naver_Client_Id')
    pwd= config('X_Naver_Client_Secret')
    headers = {
        'X-Naver-Client-Id':id,
        'X-Naver-Client-Secret':pwd
    }
    
    # 200개 기업 체크
    for corp_id in range(len(corp_names)):
        # 오늘의 기업 체크용 ESG 관련 전체 개수
        total_cnt = 0
        # E,S,G 관련된 긍정, 부정 기사 개수
        e_negative_cnt = e_positive_cnt = 0
        s_negative_cnt = s_positive_cnt = 0
        g_negative_cnt = g_positive_cnt = 0

        # 기업명 검색어로 설정 및 검색
        keyword = corp_names[corp_id]
        url = f'https://openapi.naver.com/v1/search/news.json?query={keyword}&display={display}&start={start}&sort=sim'
        res = requests.get(url, headers=headers)

        # 검색 기업 객체 가져오기
        # pk값이 1부터 시작하므로 corp_id + 1
        corp = Corporate.objects.get(id=corp_id+1)

        # 응답 결과 문제 없으면
        if res.status_code == 200:
            # json 형식으로 변환
            datas = res.json()
            # 검색 결과가 없으면 건너뜀 / 에러발생 방지용
            if datas['total'] == 0:
                continue
            # 검색 결과 중에서 제목 체크
            temp = pd.DataFrame(datas['items'])
            for idx, title in enumerate(temp['title']):
                # 하루 전날 기사인지 체크
                news_time = temp['pubDate'][idx].split()
                news_year = news_time[3]
                news_month = months.index(news_time[2])
                news_day = int(news_time[1])
                now = datetime.datetime.now()-datetime.timedelta(days=1)
                now_year = now.year
                now_month = now.month
                now_day = now.day
                # 작성일자 2021-01-01 과 같은 형식으로 통일
                news_created = str(news_year) + '-' + str(news_month).zfill(2) + '-' + str(news_day).zfill(2)
                # 하루 전날 기사만 수집
                if (now_year != int(news_year)) or (news_month != now_month) or (now_day != news_day):
                    continue
                
                # 검색 결과에 포함된 HTML 관련 문자 제거
                title = temp['title'][idx].strip().replace('<b>','').replace('</b>','')\
                    .replace('&quot;','"').replace('&lt;','>').replace('&gt;','<').replace('&amp;','&')
                temp['title'][idx] = title

                # ESG, 긍부정 분류
                e = check_e(title)
                s = check_s(title)
                g = check_g(title)
                evaluation = check_v(title)

                # ESG 관련 기사면
                if e or s or g:
                    # 전체 갯수 증가
                    total_cnt += 1
                    link = temp['originallink'][idx]
                    content = temp['description'][idx].strip().replace('<b>','').replace('</b>','')\
                        .replace('&quot;','"').replace('&lt;','>').replace('&gt;','<').replace('&amp;','&')
                    category = ''
                    # E 관련 기사면
                    if e:
                        category += 'E'
                        # 부정이면 부정 count
                        if evaluation == 2:
                            e_negative_cnt += 1
                        # 긍정이면 긍정 count
                        elif evaluation == 1:
                            e_positive_cnt += 1
                    # S 관련 기사면
                    if s:
                        category += 'S'
                        if evaluation == 2:
                            s_negative_cnt += 1
                        elif evaluation == 1:
                            s_positive_cnt += 1
                    # G 관련 기사면
                    if g:
                        category += 'G'
                        if evaluation == 2:
                            g_negative_cnt += 1
                        elif evaluation == 1:
                            g_positive_cnt += 1

                    # 모델 형식에 맞게 각각 설정
                    news_data = News(corporate=corp, title=title, url=link, content=content, date=news_created, category=category,
                    evaluation=evaluation)

                    # 제목과 기업이 같은지 중복기사 체크
                    if not News.objects.filter(Q(title=title) & Q(corporate=corp)).exists():
                        news_data.save()

                    # 출력 확인용
                    print()
                    print(corp_id, title, link, content, news_created, category, evaluation)
                    print("e:", e, "s:", s, "g:", g,"v:", evaluation)
                    print("e_positive_cnt:", e_positive_cnt, "e_negative_cnt:", e_negative_cnt)
                    print("s_positive_cnt:", s_positive_cnt, "s_negative_cnt:", s_negative_cnt)
                    print("g_positive_cnt:", g_positive_cnt, "g_negative_cnt:", g_negative_cnt)
                    print("total_cnt:", total_cnt)
                    print("===========================================================")
                    print()
            # E 업데이트
            envirnoment = Environment.objects.get(corporate=corp)
            # 부정적인 기사가 있으면 부정 + 1
            if e_negative_cnt:
                envirnoment.news_neg_cnt = envirnoment.news_neg_cnt + 1
            # 긍정 기사가 있으면 긍정 + 1
            if e_positive_cnt:
                envirnoment.news_pos_cnt = envirnoment.news_pos_cnt + 1
            envirnoment.save()

            # S 업데이트
            social = Social.objects.get(corporate=corp)
            if s_negative_cnt:
                social.news_neg_cnt = social.news_neg_cnt + 1
            if s_positive_cnt:
                social.news_pos_cnt = social.news_pos_cnt + 1
            social.save()

            # G 업데이트
            gov = Governance.objects.get(corporate=corp)
            if g_negative_cnt:
                gov.news_neg_cnt = gov.news_neg_cnt + 1
            if g_positive_cnt:
                gov.news_pos_cnt = gov.news_pos_cnt + 1
            gov.save()

            corp.today_cnt = total_cnt
            corp.save()

        # 기업별 기사 10개 넘으면 제거
        length = len(News.objects.filter(corporate=corp))
        while length > 10:
            News.objects.filter(corporate=corp).first().delete()
            length -= 1

import time
start = time.time()  # 시작 시간 저장

search_news_data()

end = time.time()
print("시작시간 : ", start)
print("종료 시간: ", end)
print("총 실행시간 :", end - start)  # 현재시각 - 시작시간 = 실행 시간

# 시작시간 :  1633089025.5979166
# 종료 시간:  1633091180.8829184
# 총 실행시간 : 2155.2850017547607 = 약 36분