import gptAPI
import gptData
import Post

# rhzn5512 개발 rhzn5511 JPOP rhzn5510 POP rhzn5509 일본어 학습
# rhzzn5513 트로트 rhzn5514 X세대 노래 rhzn5515 
# 해야할 일 셀르니움 or 파이오토 -> 웹페이지 크롤링 -> ChatGPT API -> addPOST 함수로 데이터 추가
# user_id, title, markdown, tags, series, description 

# supabase에서 profiles -> data : user_id, post_type 가져오기
# 반복문 data로 돌리기
# post_type으로 데이터 크롤링 



def main():
  system_prompts = gptData.system_prompts()
  posting_topics = gptData.posting_topics_by_country()

  subject = '공항에서, 호텔에서,식당에서, 관광지에서 사용할 수 있는 표현'
  example = {
    'title': "여행 중 필수 표현과 상황별 대처 방법",
    'markdown': '''# 여행 중 필수 표현과 상황별 대처 방법

## 1. 공항에서

### 체크인 할 때
- **I have a reservation.**  
  예약이 있습니다.
- **Where is the check-in desk?**  
  체크인 데스크가 어디인가요?

### 보안 검사에서
- **Do I need to take off my shoes?**  
  신발을 벗어야 하나요?
- **Is there a liquid limit?**  
  액체 반입 제한이 있나요?

### 탑승구에서
- **What time does my flight depart?**  
  제 비행기는 몇 시에 출발하나요?
- **Is this seat taken?**  
  이 좌석은 비어있나요?

## 2. 호텔에서

### 체크인 할 때
- **I have a booking under the name...**  
  ...라는 이름으로 예약했습니다.
- **Could I have a room with a view?**  
  전망 좋은 방으로 받을 수 있을까요?

### 요청할 때
- **Can I have extra towels?**  
  수건 추가로 받을 수 있을까요?
- **Is breakfast included?**  
  아침 식사가 포함되어 있나요?

## 3. 식당에서

### 주문할 때
- **I’d like to order...**  
  ...를 주문할게요.
- **Could we have the bill, please?**  
  계산서 좀 주시겠어요?

### 응답할 때
- **It’s delicious!**  
  정말 맛있어요!
- **I’m allergic to...**  
  ...에 알레르기가 있어요.

## 4. 관광지에서

### 길 묻기
- **Excuse me, where is...?**  
  실례합니다, ...가 어디인가요?
- **How long does it take to get there?**  
  거기까지 가는데 얼마나 걸리나요?

### 사진 촬영 부탁하기
- **Could you take a picture of us?**  
  저희 사진 좀 찍어주시겠어요?
- **Where is a good spot to take pictures?**  
  사진 찍기 좋은 곳이 어디인가요?

---

# 오늘의 유용한 표현 (상황별)

## 공항에서
- **Check-in desk**: 체크인 데스크
- **Boarding pass**: 탑승권
- **Departure gate**: 출발 탑승구

## 호텔에서
- **Reservation**: 예약
- **Room service**: 룸 서비스
- **Check-out**: 체크아웃

## 식당에서
- **Menu**: 메뉴
- **Bill/Check**: 계산서
- **Table for two**: 두 사람용 테이블

## 관광지에서
- **Map**: 지도
- **Guide**: 가이드
- **Souvenir**: 기념품

### 예시
**Check-in desk**
- 영어: Where is the check-in desk?
- 한국어: 체크인 데스크가 어디인가요?

**Reservation**
- 영어: I have a reservation under the name...
- 한국어: ...라는 이름으로 예약했습니다.
''',
    'tags': ['여행', '표현', '상황별 대처', '여행 팁', '여행 준비'],
    'series': "여행 준비 가이드",
    'description': "여행 중 다양한 상황에서 유용하게 사용할 수 있는 필수 표현과 대처 방법을 소개합니다."
}
  user = {}
    
  # ChatGPT API 호출
  for id in system_prompts:
      posted_titles = Post.get_post_titles_by_user(id)
      response = gptAPI.extract_data_variable(subject, example, system_prompts[id], posting_topics[id], posted_titles)

      if response != None:
        print(response)
        user[id] = True
        Post.add_post(id, response['title'], response['markdown'], response['tags'], response['series'], response['description'])
  return user

print(main())



