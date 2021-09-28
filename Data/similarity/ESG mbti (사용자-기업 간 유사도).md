## ESG mbti (사용자-기업 간 유사도)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import requests

#사용자 esg 정보
data1 = np.array([12, 15, 11])
data_df1 = pd.DataFrame(data1)
data_df1 = data_df1.T

# 기업 전부 esg 정보   
data2 = np.array([[10, 3, 19], [13, 12, 13], [10, 6, 15], [11, 12, 11]])
data_df2 = pd.DataFrame(data2)

data_df1
data_df2
```



```python
# 코사인 유사도 
from sklearn.metrics.pairwise import cosine_similarity

data_sim = cosine_similarity(data_df1, data_df2)
print(data_sim)

# 코사인 유사도로 비율 유사도가 높은 기업 순서
print(data_sim.argsort()[:,::-1])
corp_rank = data_sim.argsort()[:,::-1]
print('비율 유사도', corp_rank)

# 코사인 유사도 기준으로 기업 10개 자르기 
corp_rank = corp_rank[0][:10]
print('코사인 기준으로 10개 기업 자르기',corp_rank)

```



```python
# 유클리디안 거리 (10개 기업 중 3개 고르기)
from sklearn.metrics.pairwise import euclidean_distances

# data2에서 발탁된 10개 기업의 esg 점수 가져오기 
#(코사인으로 뽑힌 인덱스 10개를 이용해서 esg 점수 가져오기) 
# [['E_rating', 'S_rating', 'G_rating']] 얘만 나중에 추출 
data3 = data_df2.iloc[corp_rank]
print('data3', data3)

# 유클리디안 거리 계산
data_sim_d = euclidean_distances(data_df1, data3)
data_sim_rank = data_sim_d.argsort()
print('새로운 인덱스', data_sim_rank[0][0])
print('원래 인덱스', data3.index[data_sim_rank[0][0]])
# [['name']] 얘만 나중에 추출해서 상위 3개 기업 response로 보냄 
```

