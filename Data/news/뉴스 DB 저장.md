# 뉴스 저장

### 1. 네이버 API로 뉴스 검색

- 매일 새벽에 업데이트할 예정이므로, 하루 전날 기사만 불러와서 저장
- ESG 관련 기사만 저장



### 2. 뉴스 데이터 분류

- 저장한 pt 모델을 가져와서 eval 모드로 설정

```python
# 모델 만들기
e_model = BERTClassifier(bertmodel, dr_rate=0.5).to(device)

# 모델 불러오기
e_model.load_state_dict(torch.load("../data/model/e_model.pt", map_location=device))

# 평가모드
e_model.eval()
```

- E/S/G/V 모델로 평가
  - 예측 결과 0, 1, 2 로 반환

```python
def check_v(title):
    pdData = [[title, 5]]
    test_set = BERTDataset(pdData, 0, 1, tok, max_len, True, False) 
    test_input = torch.utils.data.DataLoader(test_set, batch_size=batch_size, num_workers=0)
    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_input):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)
        valid_length= valid_length 
        v_test_out = v_model(token_ids, valid_length, segment_ids)

        logits = v_test_out[0]
        logits = logits.detach().cpu().numpy()

        if np.argmax(logits) == 0:
            return 0
        elif np.argmax(logits) == 1:
            return 1
        elif np.argmax(logits) == 2:
            return 2
```



### 3. 뉴스 저장

- DB에 저장
- ESG, 긍부정 갯수 체크 후 Corporate, Envirnoment, Social, Governance 에 반영
- 기업별 기사 10개 넘으면 제거

```python
# 기업별 기사 10개 넘으면 제거
length = len(News.objects.filter(corporate=corp))
while length > 10:
    News.objects.filter(corporate=corp).first().delete()
    length -= 1
```

- 길이 체크해서 10개 이상인것 하나씩 제거
- 일일 단위로 저장하므로 먼저 저장된 것이 과거 기사이기 때문에 다음과 같이 while문으로 first() 제거함



- 한 번 실행하는데 약 36분 소요됨
  - 시작시간 : 1633089025.5979166
  - 종료 시간: 1633091180.8829184
  - 총 실행시간 : 2155.2850017547607 = 약 36분

