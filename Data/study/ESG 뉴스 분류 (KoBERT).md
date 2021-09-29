# ESG 뉴스 분류

## BERT

> Bi-directional Encoder Representations from Transformers 
>
> 구글에서 개발한 양방향 자연어 처리 모델

- 방대한 양의 텍스트 데이터로 사전 훈련된 언어모델
- Transformer를 이용하여 구현되어 있음
- 문장에서 가려진 토큰 예측 (Maked Language Model, MLM)
- 다음 문장 예측 (Next Sentence Prediction, NSP)



### 참고 자료

[딥러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)

**[토크ON세미나] 자연어 언어모델 ‘BERT’  - 자연어 처리 (NLP) | T아카데미**

> [1강](https://www.youtube.com/watch?v=qlxrXX5uBoU&t=774s&ab_channel=SKplanetTacademy), [2강](https://www.youtube.com/watch?v=zia49ZyKiX0&t=162s&ab_channel=SKplanetTacademy), [3강](https://www.youtube.com/watch?v=riGc8z3YIgQ&ab_channel=SKplanetTacademy), [4강](https://www.youtube.com/watch?v=PzvKDpQgNzc&ab_channel=SKplanetTacademy), [5강](https://www.youtube.com/watch?v=S42vDzJExIA&t=1974s&ab_channel=SKplanetTacademy)



## Transformer란?

[Attention is All You Need](https://arxiv.org/pdf/1706.03762.pdf)

[[딥러닝 기계 번역] Transformer: Attention Is All You Need (꼼꼼한 딥러닝 논문 리뷰와 코드 실습) - 동빈나](https://www.youtube.com/watch?v=AA621UofTUA&t=92s&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98)

[허민석 - 트랜스포머](https://www.youtube.com/watch?v=mxGCEWOxfe8)

[Transformer 정리](https://ahnjg.tistory.com/57)

- 기존의 CNN, RNN 모델을 사용하지 않는 Encoder/ Decoder로 구성된 딥러닝 모델
  - GPT : Decoder / BERT: Encoder 아키텍쳐 활용

- Positional Encoding
  - Attention 메커니즘 사용
  - 성능 향상을 위해 잔여 학습(Residual Learning)
  - Attention과 Nomalization 과정 반복
- 마지막 인코더 레이어의 출력이 모든 디코더 레이어에 입력
- Attention을 위한 3가지 입력요소
  - 쿼리(Query)
  - 키(Key)
  - 값(Value)
- Multi Head Attention 레이어 사용
  - Encoder Self-Attention
  - Masked Decoder Self-Attention
  - Encoder-Decoder Attention





## 학습용 데이터 분류

> Train, Validation, Test
>
> [머신러닝, 딥러닝에서 데이터를 나누는 이유](https://lsjsj92.tistory.com/545)
>
> 7:1:2 / 6:2:2 / 7:2:1

#### 1. Train / Validation data

- train data : 학습용 데이터
- validation data : training 과정에서 확인하고 검증하기 위한 데이터
  - Overfitting 방지
  - 모델이 내가 가진 학습 데이터에 너무 과적합되도록 학습한 나머지, 이를 조금이라도 벗어난 케이스에 대해서는 예측율이 현저히 떨어지는 현상

#### 2. Test data

- 모델이 한 번도 보지 못한 데이터로 평가 진행
- 최종적으로 모델 평가 지표가 된다.

#### 3. X_train, Y_train, X_test, Y_test

- X : feature
- Y : label



## KoBERT

> 한국어 데이터셋을 바탕으로 사전 학습된 모델

#### 참고자료

- [KoBERT Github](https://github.com/SKTBrain/KoBERT)
  - [Naver Sentiment Analysis Fine-Tuning with pytorch](https://colab.research.google.com/github/SKTBrain/KoBERT/blob/master/scripts/NSMC/naver_review_classifications_pytorch_kobert.ipynb) 예제
- [KoBERT 개발자 개발 리뷰](http://freesearch.pe.kr/archives/4981)
- [KoBERT로 다중분류 모델 만들기](https://velog.io/@seolini43/KOBERT%EB%A1%9C-%EB%8B%A4%EC%A4%91-%EB%B6%84%EB%A5%98-%EB%AA%A8%EB%8D%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%ACColab)
- [KoBERT를 이용한 감성 분석 예시](https://tech-diary.tistory.com/31)
- [KoBERT 쉽게 따라하고 간단한 fine-tuning 하기](https://moondol-ai.tistory.com/241)
- [[파이썬]일상/연애 주제의 한국어 대화 'BERT'로 이진 분류 모델 만들기 - 코드](https://velog.io/@seolini43/%EC%9D%BC%EC%83%81%EC%97%B0%EC%95%A0-%EC%A3%BC%EC%A0%9C%EC%9D%98-%ED%95%9C%EA%B5%AD%EC%96%B4-%EB%8C%80%ED%99%94-BERT%EB%A1%9C-%EC%9D%B4%EC%A7%84-%EB%B6%84%EB%A5%98-%EB%AA%A8%EB%8D%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0%ED%8C%8C%EC%9D%B4%EC%8D%ACColab-%EC%BD%94%EB%93%9C)



#### 사전(Vocabulary)

- 크기 : 8,002
- 한글 위키 기반으로 학습한 토크나이저(SentencePiece)
- Less number of parameters(92M < 110M )



#### KoBERT 학습 데이터 형식

> [KoBERT input data 형식](https://steminher.tistory.com/137)

- Text(X_data)
- Label(Y_data)
- [[text, label]] 과 같은 리스트 형식으로 만들어서 학습



### 사용 모듈 정리

#### train_test_split

> [train_test_split 모듈을 활용하여 학습과 테스트 세트 분리](https://teddylee777.github.io/scikit-learn/train-test-split)

- `test_size`: 테스트 셋 구성의 비율
- `shuffle`: split을 전에 섞을지
- `stratify` : stratify 값을 target으로 지정해주면 각각의 class 비율(ratio)을 train / validation 유지 (한 쪽에 쏠려서 분배되는 것을 방지)
- `random_state`: 세트를 섞을 때 해당 int 값을 보고 섞으며, 하이퍼 파라미터를 튜닝시 이 값을 고정해두고 튜닝해야 매번 데이터셋이 변경되는 것을 방지할 수 있다.



#### DataLoader

- [DataLoader Parameters](https://subinium.github.io/pytorch-dataloader/)



### 하이퍼파라미터(Hyperparameter)

#### 에폭 수(Epoch)

- 훈련 데이터셋에 포함된 모든 데이터들이 한 번씩 모델을 통과한 횟수로, 모든 학습 데이터셋을 학습하는 횟수를 의미
- epoch를 높일수록, 다양한 무작위 가중치로 학습을 해보므로, 적합한 파라미터를 찾을 확률이 올라간다.
  - 손실 값 감소
- 그러나 지나치게 epoch를 높이면, 학습 데이터셋에 Overfitting 되어 다른 데이터에 대해선 제대로 된 평가를 하지 못할 수 있다.

#### 배치 크기(Bath size)

- 연산 한 번에 들어가는 데이터의 크기
- 배치 사이즈가 너무 큰 경우 한 번에 처리해야 할 데이터의 양이 많아지므로, 학습 속도가 느려지고, 메모리 부족 문제가 발생할 위험이 있다.
- 반대로, 배치 사이즈가 너무 작은 경우 적은 데이터를 대상으로 가중치를 업데이트하고, 이 업데이트가 자주 발생하므로, 훈련이 불안정해진다.

#### 학습률(learning rate) 

- 각 배치/에폭에서 모델의 매개변수를 조절하는 비율
- 값이 작을수록 학습 속도가 느려지고, 값이 크면 학습 중 예측할 수 없는 동작이 발생할 수 있다.



### 최적화 단계 (Optimization Loop)

하나의 에폭은 다음 두 부분으로 구성

- **학습 단계(train loop)** - 학습용 데이터셋을 반복(iterate)하고 최적의 매개변수로 수렴합니다.
- **검증/테스트 단계(validation/test loop)** - 모델 성능이 개선되고 있는지를 확인하기 위해 테스트 데이터셋을 반복(iterate)합니다.



#### 손실 함수(loss function)

- 학습용 데이터를 제공하면, 학습되지 않은 신경망은 정답을 제공하지 않을 확률이 높다.
- 손실 함수(loss function)는 획득한 결과와 실제 값 사이의 틀린 정도(degree of dissimilarity)를 측정하며, 학습 중에 이 값을 최소화하려고 한다.
- 주어진 데이터 샘플을 입력으로 계산한 예측과 정답(label)을 비교하여 손실(loss)을 계산
- [BCELoss(이진분류)](https://pytorch.org/docs/stable/generated/torch.nn.BCELoss.html) + Sigmoid layer = BCEWithLogitsLoss
- [CrossEntropyLoss (다중분류)](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html) - softmax 포함
  - **이진분류에서도 사용 가능해서 예제대로 CrossEntropyLoss 사용**
- [[PyTorch] 자주쓰는 Loss Function (Cross-Entropy, MSE) 정리](https://nuguziii.github.io/dev/dev-002/)



#### 옵티마이저(optimizer)

- 최적화는 각 학습 단계에서 모델의 오류를 줄이기 위해 모델 매개변수를 조정하는 과정

- AdamW 사용
  - [Optimizers (momentum, RMSProp, Adam, AdamW)](https://aimaster.tistory.com/76?category=434406)
  - [AdamW ](https://huggingface.co/transformers/main_classes/optimizer_schedules.html#adamw-pytorch)



#### 스케줄러(scheduler)

- [get_cosine_schedule_with_warmup](https://huggingface.co/transformers/main_classes/optimizer_schedules.html#transformers.get_cosine_schedule_with_warmup)
- [다양한 Learning Rate Scheduler(pytorch)](https://dacon.io/codeshare/2373)



### 학습단계

- `optimizer.zero_grad()`를 호출하여 모델 매개변수의 변화도를 재설정합니다. 기본적으로 변화도는 더해지기(add up) 때문에 중복 계산을 막기 위해 반복할 때마다 명시적으로 0으로 설정합니다.
- `loss.backward()`를 호출하여 예측 손실(prediction loss)을 역전파합니다. PyTorch는 각 매개변수에 대한 손실의 변화도를 저장합니다.
- 변화도를 계산한 뒤에는 `optimizer.step()`을 호출하여 역전파 단계에서 수집된 변화도로 매개변수를 조정합니다.





## ESG 데이터 라벨링

#### E / S / G

- E,S,G, 기타 (0,1,2,3) 으로 한번에 하려고 했는데 여러 기준을 동시에 만족하는 기사의 경우 분류가 어려운 문제 발생
  - E / S / G 모두 이진분류
- E / S / G
  - 0 : 관련 없음
  - 1 : 관련 있음

#### value (중립/긍정/부정)

- 다중분류

- 0 , 1, 2 (중립, 긍정, 부정)





## 모델 평가

> [머신러닝 모델 평가(정밀도,재현율,f1-score등)](https://velog.io/@ljs7463/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EB%AA%A8%EB%8D%B8-%ED%8F%89%EA%B0%80%EC%A0%95%EB%B0%80%EB%8F%84%EC%9E%AC%ED%98%84%EC%9C%A8f1-score%EB%93%B1)

#### 0. 오차행렬 (confusion matrix)

![오차행렬](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FEojHI%2FbtqBuwXbsUN%2F1Tt2KW49Zp8ZM7tpBWHUcK%2Fimg.png)

#### 1. 정확도 (Accuracy)

- 실제 데이터에서 예측 데이터가 얼마나 같은지를 판단하는 지표

- 정확도(Accuracy) = (예측 결과가 동일한 데이터 건수) / (전체 예측 데이터 건수)

- (TP + TN) / Total



#### 2. 정밀도 (Precision)

- Positive로 예측한 경우 중 실제로 Positive인 비율이다: 

- TP / (TP + FP)



#### 3. 재현율 (Recall)

- 실제 Positive인 것 중 올바르게 Positive를 맞춘 것의 비율

- TP / (TP + FN)

- 민감도(Sensitivity) 혹은 TPR(True Positive Rate)이라고도 불린다
- 암 검사, 스팸 메일 체크 등 잘못 판단하면 큰일나는 경우에 중요하다.

- 정밀도 - 재현율은 trade-off 관계



#### 4. F1-Score

- Precision과 Recall의 조화평균, 데이터가 불균형이 클 때 사용하면 좋다.
- 정확도의 경우, 데이터 분류 클래스가 균일하지 못하면 머신러닝 성능을 제대로 나타낼 수 없기 때문에 F1 Score를 사용한다.
- F1 = 2 * (Precision * Recall) / (Precision + Recall)
- 높을수록 좋은 모델



- 다음과 같이 classification_report 이용하면 한번에 확인 가능 

```python
from sklearn.metrics import classification_report
classification_report(예상값, 정답)
```



- e-model

```
              precision    recall  f1-score   support

           0       0.99      0.98      0.98       351
           1       0.81      0.88      0.85        34

    accuracy                           0.97       385
   macro avg       0.90      0.93      0.91       385
weighted avg       0.97      0.97      0.97       385
```

- s-model

```
              precision    recall  f1-score   support

           0       0.97      0.96      0.96       281
           1       0.90      0.91      0.90       104

    accuracy                           0.95       385
   macro avg       0.93      0.94      0.93       385
weighted avg       0.95      0.95      0.95       385
```

- g-model

```
              precision    recall  f1-score   support

           0       0.97      0.99      0.98       308
           1       0.96      0.88      0.92        77

    accuracy                           0.97       385
   macro avg       0.96      0.94      0.95       385
weighted avg       0.97      0.97      0.97       385
```

- v-model

```
              precision    recall  f1-score   support

           0       0.91      0.96      0.93       221
           1       0.95      0.82      0.88        93
           2       0.91      0.90      0.91        71

    accuracy                           0.92       385
   macro avg       0.92      0.89      0.91       385
weighted avg       0.92      0.92      0.92       385
```





#### 모델 저장하고 불러오기

- torch.save(object, path)
- torch.load(path)



## Issue

- 메모리 초과 에러
  - `RuntimeError: CUDA out of memory. Tried to allocate 48.00 MiB (GPU 0; 11.17 GiB total capacity; 10.63 GiB already allocated; 15.81 MiB free; 10.70 GiB reserved in total by PyTorch)`
  - batch size를 줄인다.
  - Train Data, model 삭제 후 GPU 공간 확보


```python
import gc
del e_model, e_train, e_test
gc.collect()
torch.cuda.empty_cache()
```



- G, V를 제대로 체크하지 못한다.
  - V는 부정적인 기사의 수가 너무 적기때문에 학습이 제대로 되지 않음
    - 1400개중 40개정도만 부정적인 기사였음
  - 데이터 수를 늘려서 학습 진행해서 해결



- 같은 날 같은 내용의 기사가 여러 개 존재
  - ex) 에쓰오일 - 삼성물산 친환경 에너지 사업 진출... 이라는 내용의 기사만 10개이상 존재
  - 일일 기사 단위로 긍정 부정 평가 해야할지?

- 기업 이름으로 검색 시 뉴스 기사와 관련이 없는 내용인 경우가 존재



- 기업명이 분석에 사용될 수 있음

  - 기업명 다른 단어로 대체
  - 기사 제목에 기업명이 없는 경우가 있어 제대로 처리하기 힘듦






#### 데이터 불균형 문제

> [Text Classification에서 class imbalance 해결 방법](https://simonezz.tistory.com/92?category=892980)

**Resampling methods**

- 데이터셋을 수정해서 클래스의 사이즈 간의 차이를 줄이는 방법

1. undersampling
   - 데이터 수가 많은 class의 데이터를 삭제하는 방식
2. oversampling
   - 데이터 수가 적은 class를 만들어내는 방식

- 그 외에도 SMOTE, WOMOTE 등의 방법이 있다.
- 어차피 부정적인 기사 데이터를 수집해야 하므로 데이터 수집 추가 진행

- 0인 데이터가 너무 많아서 비슷한 내용의 불필요한 기사 최소화 작업 진행



- 데이터 불균형이 심해서 제대로 된 학습이 불가능
  - 기업 + ESG or 부정적 키워드로 검색해서 데이터 수집
  - [연관규칙 분석을 통한 ESG 우려사안 키워드 도출에 관한 연구](https://www.koreascience.or.kr/article/JAKO202113150644042.pdf) 참고해서 선정
  - E
    - 친환경, 기후
  - S
    - 기업명 + 사회공헌, 채용, 노동, 기부, 노조
  - G
    - 기업명 + 지배구조, 임명, 자사주
  - 부정적 키워드
    - E
      - 환경오염
    - S
      - 담합, 불법파견, 불법고용, 불매운동, 불공정거래, 하도급
    - G
      - 횡령, 갑질, 비리, 뇌물, 분식회계, 탈세
