from decouple import config
import pandas as pd

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
max_len = 64
batch_size = 64
warmup_ratio = 0.1
num_epochs = 6
max_grad_norm = 1
log_interval = 200
learning_rate =  5e-5

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
e_model.load_state_dict(torch.load("../data/model/e_model.pt", map_location=device))
s_model.load_state_dict(torch.load("../data/model/s_model.pt", map_location=device))
g_model.load_state_dict(torch.load("../data/model/g_model.pt", map_location=device))
v_model.load_state_dict(torch.load("../data/model/v_model.pt", map_location=device))
e_model.eval()
s_model.eval()
g_model.eval()
v_model.eval()

def check_e(title):
    pdData = [[title, 5]]
    test_set = BERTDataset(pdData, 0, 1, tok, max_len, True, False) 
    test_input = torch.utils.data.DataLoader(test_set, batch_size=batch_size, num_workers=0) # num_workers = 0 으로 안하면 에러발생
    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_input):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)
        valid_length= valid_length 
        label = label.long().to(device)
        # 이때, out이 예측 결과 리스트
        e_test_out = e_model(token_ids, valid_length, segment_ids)

        logits = e_test_out[0]
        logits = logits.detach().cpu().numpy()

        if np.argmax(logits) == 0:
            return 0
        elif np.argmax(logits) == 1:
            return 1

def check_s(title):
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


from bs4 import BeautifulSoup
from pprint import pprint
import datetime
import requests
from .models import News, Corporate, Environment, Social, Governance

months = ['', 'Jan', 'Fab', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def search_news_data():
    corps = pd.read_excel("../data/기업정보.xlsx")
    corp_names = corps["종목명"]
    keyword = ''
    display = 100
    start = 1
    id = config('X_Naver_Client_Id')
    pwd= config('X_Naver_Client_Secret')
    url = f'https://openapi.naver.com/v1/search/news.json?query={keyword}&display={display}&start={start}&sort=sim'
    headers = {
        'X-Naver-Client-Id':id,
        'X-Naver-Client-Secret':pwd
    }
    for corp_name in range(len(corp_names)):
        cnt = 0
        keyword = corp_names[corp_name]
        url = f'https://openapi.naver.com/v1/search/news.json?query={keyword}&display={display}&start={start}&sort=sim'
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            datas = res.json()
            if datas['total'] == 0:
                continue
            temp = pd.DataFrame(datas['items'])
            for idx, title in enumerate(temp['title']):
                news_time = temp['pubDate'][idx].split()
                news_year = news_time[3]
                news_month = months.index(news_time[2])
                news_day = int(news_time[1])
                now = datetime.datetime.now()-datetime.timedelta(days=1)
                now_year = now.year
                now_month = now.month
                now_day = now.day
                news_created = str(news_year) + '-' + str(news_month).zfill(2) + '-' + str(news_day).zfill(2)
                if (now_year != int(news_year)) or (news_month != now_month) or (now_day != news_day): # 하루 전날 기사만 수집
                    continue
                title = temp['title'][idx].strip().replace('<b>','').replace('</b>','')\
                    .replace('&quot;','"').replace('&lt;','>').replace('&gt;','<').replace('&amp;','&')
                temp['title'][idx] = title
                e = check_e(title)
                s = check_s(title)
                g = check_g(title)
                v = check_v(title)
                if e or s or g:
                    cnt += 1
                    print(title)
                    corp_id = corps['종목코드'][corp_name]
                    link = temp['originallink'][idx]
                    content = temp['description'][idx].strip().replace('<b>','').replace('</b>','')\
                        .replace('&quot;','"').replace('&lt;','>').replace('&gt;','<').replace('&amp;','&')
                    news_date = temp['pubDate'][idx]
                    category = ''
                    if e:
                        category += 'E'
                    if s:
                        category += 'S'
                    if g:
                        category += 'G'
                    

                    print(corp_name, title, link, content, news_created, category)
                    print("e:", e, "s:", s, "g:", g,"v:", v)
        


search_news_data()