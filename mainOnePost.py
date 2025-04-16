import Post

# rhzn5512 개발 rhzn5511 JPOP rhzn5510 POP rhzn5509 일본어 학습
# rhzzn5513 트로트 rhzn5514 X세대 노래 rhzn5515 
# 해야할 일 셀르니움 or 파이오토 -> 웹페이지 크롤링 -> ChatGPT API -> addPOST 함수로 데이터 추가
# user_id, title, markdown, tags, series, description 

# supabase에서 profiles -> data : user_id, post_type 가져오기
# 반복문 data로 돌리기
# post_type으로 데이터 크롤링 



def main():
  # 데이터 추가
  response = Post.add_post(
      user_id="rhzn5510",
      title = "Love U Like That (난 그런 너를 사랑해) [가사/해석/발음/의역]",
        markdown='''# Lauv - Love U Like That

## [Verse 1]
Drunk in the rain  
드렁크 인 더 레인  
취한 채로 빗속을 거닐어  

Really old habits, really old baggage  
릴리 올드 해빗츠, 릴리 올드 배기지  
오래된 버릇, 오래된 짐들과 함께  

Just walked away into your madness, onto your mattress  
저스트 워크드 어웨이 인투 유어 매드니스, 온투 유어 매트리스  
난 지금 너라는 소용돌이에 갇혀버렸어, 어느새 네 침대 위야  

Goddamn okay  
갓댐 오케이  
젠장, 이제 어쩌지  

You’re so attractive, how did that happen?  
유어 쏘 어트랙티브, 하우 디드 댓 해픈?  
넌 너무 매력적이야, 어쩜 이래?  

And you’re kissing on my neck  
앤드 유어 키싱 온 마이 넥  
네가 내 목에 키스를 하면  

I’m like ohhhh  
아임 라이크 오~~~  
감탄사가 절로 나와  

Got your hands up on my chest  
갓 유어 핸즈 업 온 마이 체스트  
네 손이 점점 위로 올라오면  

I’m like ohhh  
아임 라이크 오~~~  
내 기분도 하늘 위로 날아가  

Kiss me til there’s nothing left  
키스 미 틸 데얼즈 낫띵 레프트  
내가 녹아 없어질 때까지 키스해 줘  

Oh my god  
오 마이 갓  
오 마이 갓  

Oh my god  
오 마이 갓  
오 마이 갓  

## [Chorus]
You could really tear apart but  
유 쿳 릴리 테어 어파트 벗  
네가 내 가슴을 찢어 놓을 수도 있겠지만  

I love you like that  
아이 러브 유 라이크 댓  
난 그런 널 사랑해  

Everything you do just turns me on  
에브리띵 유 두 저스트 턴즈 미 온  
네가 하는 모든 행동들이 날 끌어당겨  

I love you like that  
아이 러브 유 라이크 댓  
난 그런 널 사랑해  

Body on my mind like all night long  
바디 온 마이 마인드 라이크 올 나잇 롱  
밤새도록 네 생각만 해  

6 o’clock in the morning babe  
식스 어클락 인 더 모닝 베이브  
새벽 6시가 될 때까지 멈출 수가 없어  

Want you more than yesterday  
원트 유 모어 댄 예스터데이  
시간이 갈수록 널 더 원하게 돼  

Used to judge myself now I don’t care cause  
유즈드 투 저지 마이셀프 나우 아이 돈 케어 커즈  
난 항상 내 스스로를 괴롭혔는데 이젠 그렇지 않아  

## [Verse 2]
Hey  
헤이  
있잖아  

I love you like that  
아이 러브 유 라이크 댓  
난 그런 널 사랑해  

Everything you do just turns me on  
에브리띵 유 두 저스트 턴즈 미 온  
네가 하는 모든 행동들이 날 끌어당겨  

I love you like that  
아이 러브 유 라이크 댓  
난 그런 널 사랑해  

Body on my mind like all night long  
바디 온 마이 마인드 라이크 올 나잇 롱  
밤새도록 네 생각만 해  

6 o’clock in the morning babe  
식스 어클락 인 더 모닝 베이브  
새벽 6시가 될 때까지 멈출 수가 없어  

Want you more than yesterday  
원트 유 모어 댄 예스터데이  
시간이 갈수록 널 더 원하게 돼  

Used to judge myself now I don’t care cause  
유즈드 투 저지 마이셀프 나우 아이 돈 케어 커즈  
난 항상 내 스스로를 괴롭혔는데 이젠 그렇지 않아  

I’m wide awake  
아임 와이드 어웨이크  
잠이 오질 않아  

I don’t need coffee, I know you want me  
아이 돈 니드 커피, 아이 노우 유 원트 미  
커피는 필요 없어, 네가 날 원하니까  

That’s the champagne  
댓츠 더 샴페인  
이게 그 샴페인이야  

Sipping it slowly  
시핑 잇 슬로울리  
천천히 한 모금씩 마시며  

Getting to know you  
겟팅 투 노우 유  
널 알아가면서  

And me the same  
앤드 미 더 세임  
나 자신도 알아 갔지  

You’re so attractive, how did that happen?  
유어 쏘 어트랙티브, 하우 디드 댓 해픈?  
넌 너무 매력적이야, 어쩜 이래?  

And you’re kissing on my neck  
앤드 유어 키싱 온 마이 넥  
네가 내 목에 키스를 하면  

I’m like ohhhh  
아임 라이크 오~~~  
감탄사가 절로 나와  

Got your hands up on my chest  
갓 유어 핸즈 업 온 마이 체스트  
네 손이 점점 위로 올라오면  

I’m like ohhh  
아임 라이크 오~~~  
내 기분도 하늘 위로 날아가  

Kiss me til there’s nothing left  
키스 미 틸 데얼즈 낫띵 레프트  
내가 녹아 없어질 때까지 키스해 줘  

Oh my god  
오 마이 갓  
오 마이 갓  

Oh my god  
오 마이 갓  
오 마이 갓  

## [Chorus]
You could really tear apart but  
유 쿳 릴리 테어 어파트 벗  
네가 내 가슴을 찢어 놓을 수도 있겠지만  

I love you like that  
아이 러브 유 라이크 댓  
난 그런 널 사랑해  

Everything you do just turns me on  
에브리띵 유 두 저스트 턴즈 미 온  
네가 하는 모든 행동들이 날 끌어당겨  

I love you like that  
아이 러브 유 라이크 댓  
난 그런 널 사랑해  

Body on my mind like all night long  
바디 온 마이 마인드 라이크 올 나잇 롱  
밤새도록 네 생각만 해  

6 o’clock in the morning babe  
식스 어클락 인 더 모닝 베이브  
새벽 6시가 될 때까지 멈출 수가 없어  

Want you more than yesterday  
원트 유 모어 댄 예스터데이  
시간이 갈수록 널 더 원하게 돼  

Used to judge myself now I don’t care cause  
유즈드 투 저지 마이셀프 나우 아이 돈 케어 커즈  
난 항상 내 스스로를 괴롭혔는데 이젠 그렇지 않아  

## [Bridge]
Tell me we’re something  
텔 미 위어 썸띵  
우린 특별한 사이라고 말해줘  

Tell me we’re nothing  
텔 미 위어 낫띵  
우린 아무 사이도 아니라고 말해줘  

You’re driving me crazy  
유어 드라이빙 미 크레이지  
넌 날 미치게 해  

Driving in London  
드라이빙 인 런던  
런던에서 드라이브 하는데  

My minds in the back seat  
마이 마인즈 인 더 백 시트  
내 생각은 온통 뒷좌석에 가 있고  

My hearts in the front and…  
마이 하츠 인 더 프론트 앤드…  
내 마음은 앞을 향해 있어 그리고…  

Used to judge myself now I don’t care cause  
유즈드 투 저지 마이셀프 나우 아이 돈 케어 커즈  
난 항상 내 스스로를 괴롭혔는데 이젠 그렇지 않아  

## [Chorus]
Hey  
헤이  
있잖아  

I love you like that  
아이 러브 유 라이크 댓  
난 그런 널 사랑해  

Everything you do just turns me on  
에브리띵 유 두 저스트 턴즈 미 온  
네가 하는 모든 행동들이 날 끌어당겨  

I love you like that  
아이 러브 유 라이크 댓  
난 그런 널 사랑해  

Body on my mind like all night long  
바디 온 마이 마인드 라이크 올 나잇 롱  
밤새도록 네 생각만 해  

6 o’clock in the morning babe  
식스 어클락 인 더 모닝 베이브  
새벽 6시가 될 때까지 멈출 수가 없어  

Want you more than yesterday  
원트 유 모어 댄 예스터데이  
시간이 갈수록 널 더 원하게 돼  

Used to judge myself now I don’t care cause  
유즈드 투 저지 마이셀프 나우 아이 돈 케어 커즈  
난 항상 내 스스로를

  ---
  
  ### 오늘의 단어

#### [Verse 1]
- **Drunk**: 취한
- **Rain**: 비
- **Habits**: 습관들, 버릇들
- **Baggage**: 짐
- **Madness**: 미친 상태, 소용돌이
- **Attractive**: 매력적인
- **Happen**: 일어나다, 발생하다
- **Kiss**: 키스하다
- **Chest**: 가슴
- **Left**: 남은, 남기다
- **God**: 신, 감탄사로 사용
- **Tear apart**: 찢어지다

#### [Chorus]
- **Love**: 사랑하다
- **Turn on**: 끌어당기다, 흥미를 일으키다
- **Mind**: 마음, 생각
- **Morning**: 아침
- **Yesterday**: 어제
- **Judge**: 판단하다
- **Care**: 신경 쓰다

#### [Verse 2]
- **Awake**: 깨어있는
- **Coffee**: 커피
- **Champagne**: 샴페인
- **Slowly**: 천천히
- **Know**: 알다

#### [Bridge]
- **Something**: 무언가, 특별한 것
- **Nothing**: 아무것도 아닌 것
- **Crazy**: 미친, 열광적인
- **London**: 런던 (지명)
- **Back seat**: 뒷좌석
- **Front**: 앞쪽
- **Heart**: 마음, 심장



  ''',
      
      tags = ["Lauv", "Love U Like That", "팝송", "영어 노래", "가사 번역", "영어 공부", "음악 추천", "감성 노래"],
      series = "Lauv",
      description = "Lauv의 'Love U Like That' 곡을 통해 영어 가사를 해석하고 발음을 익히며, 영어 학습을 함께 해봅시다."
  )

  print(response)
  
main()
