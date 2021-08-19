# 딥러닝

FundingManager는 크라우드 펀딩 사이트 Wadiz(www.wadiz.com) 내 커뮤니티 글을 이용하여 프로젝트에 대한 사용자의 긍정 및 부정의 반응을 분석하였습니다.

긍정 및 부정의 기준을 선정하기 위해 종료된 프로젝트 중 별점이 함께 입력 된 리뷰를 스크래핑하였습니다.

딥러닝은 다음과 같은 순서로 진행하였습니다.

## 1. 정보단계

   (1) 데이터 가져오기 : 스크래핑을 통해 추출한 데이터를 DB에 저장하여 불러옵니다.

![image-20210819205741276](https://user-images.githubusercontent.com/85269812/130071938-2cd6c5ae-f8a8-48ca-802a-25bd2d5bc3e0.png)

   (2) 데이터 정제

   - y_data 전처리 : star rate의 소수점을 없애고 [1,2,3,4,5]로 범주화하였습니다.
   - split data : x,y 데이터를 train,test set으로 나누어주었습니다.
   - NPL (테스트 전처리)
     - konlpy의 Okt를 사용하여 형태소를 분리해주었습니다.
     - stopwords를 사용하여 불용어를 제거하였습니다.

![image-20210819212614322-1629375976197](https://user-images.githubusercontent.com/85269812/130071926-5b473d4b-0c35-471d-9235-a05ce0a2a748.png)

![image-20210819212654287](https://user-images.githubusercontent.com/85269812/130071927-d2d0c196-375e-4bda-878a-81c20cec30eb.png)

   - Tokenizer

     - tensorflow.keras.preporcessing.text.Tokenizer()를 사용해 word_index 생성 후, word_counts로 빈도 측정하여 2회 미만인 단어는 제거하였습니다.
     - Tokenizer 객체에 fit_on_texts 메소드를 사용하여 현재 Tokenizer 객체를 해당 데이터에 맞게 fitting 해주었고, index_word를 통해 현재 모델 내부에 계산된 단어 인덱스를 dictionary 형태로 확인하였습니다.

![image-20210819213437765](https://user-images.githubusercontent.com/85269812/130071934-2c175ba1-7ba9-4a2f-b4c9-61e6572a2ea5.png)

     - x_train(review)을 저장 된 tokenizer를 사용하여 컴퓨터가 인지하도록 한글을 숫자화하였습니다.
     - padding : maxlen의 크기를 그래프를 통해 200으로 설정하였습니다.

![image-20210819210833126](https://user-images.githubusercontent.com/85269812/130071898-9bd17024-1015-4b88-ac9d-5fd22effff6e.png)

## 2. 학습단계

   (1) model learning

   - make model (tf.keras.model.Sequential)

![image-20210819211052746](https://user-images.githubusercontent.com/85269812/130071901-11db9ae0-be31-46b6-be56-749b1b2f23b4.png)

     - input layer
     - hidden layer : Bidirection,GRU와 같은 양방향 재귀모델을 선택하여 모델의 예측율을 높여주었습니다.
     - output layer :  activation(활성화 함수)는 다중 분류(y의 unique값)이기 때문에 softmax를 사용하였습니다.
     - gadget : loss 역시 다중 분류이기 때문에 sparse_categorical_crossentropy를 사용하였고, metrics(평가지표)는 acc를 사용하였습니다.

   (2) Evaluation : hidden layer와 epoch의 parameter를 다르게하여 더 우수한 모델을 선정하여 진행하였습니다.

![image-20210819211206091](https://user-images.githubusercontent.com/85269812/130071905-6ae8a20f-5909-4f2f-90d8-67392f1ddd33.png)

## 3. 서비스 단계

   (1) model save and load : pickle을 사용하여 서비스 제공에 필요한 파일을 저장하고 불러올 수 있게  하였습니다.

![image-20210819211410835](https://user-images.githubusercontent.com/85269812/130071909-ebc36450-cfe4-4a71-bb7e-0ca9ecc3bf33.png)

![image-20210819211544789](https://user-images.githubusercontent.com/85269812/130071915-b46f3fe6-5db7-4a45-bf84-d1f3a080dd74.png)

![image-20210819211612648](https://user-images.githubusercontent.com/85269812/130071920-7e40e954-275c-4743-9d72-5cb54935368e.png)

   (2) prediction : 딥러닝 결과를 바탕으로 사용자가 원하는 카테고리와 리뷰를 입력하면 예측값을 시각화하여 나타내도록 하였습니다.
