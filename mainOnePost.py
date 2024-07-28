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
      title="Christopher(크리스토퍼) - Bad[가사/해석/발음/의역]",
      markdown='''# Christopher(크리스토퍼) - Bad
      
  [Verse 1]
  I don't wanna be another him, that shit is over  
  아이 돈 워너 비 어나더 힘, 댓 쉿 이즈 오버  
  나는 또다른 너의 남자가 되고싶진 않아, 그런건 이제 끝이야  

  Finally you found yourself a friend, and you run him over  
  파이널리 유 파운드 유어셀프 어 프렌드, 앤드 유 런 힘 오버  
  이제야 넌 친구라고 하며 그 남자를 짓밟아버리지  

  Ever since the start, I saw the end around the corner  
  에버 신스 더 스타트, 아이 소우 디 엔드 어라운드 더 코너  
  시작부터 난 코앞에 다가온 끝을 봤어  

  'Cause I know you so well  
  커즈 아이 노우 유 쏘 웰  
  난 널 너무 잘 알거든  

  [Chorus]
  So predictable  
  쏘 프레딕터블  
  너무 예상가능해  

  You're an animal  
  유어 언 애니멀  
  너는 동물이야  

  I can't let you go  
  아이 캔트 렛 유 고  
  너를 보낼 수는 없어  

  You're so good at being bad, you know  
  유어 쏘 굿 앳 빙 배드, 유 노우  
  너는 나쁜 사람이기를 너무 잘해, 너도 알다시피  

  So predictable  
  쏘 프레딕터블  
  너무 예상가능해  

  You're an animal  
  유어 언 애니멀  
  너는 동물이야  

  I can't let you go  
  아이 캔트 렛 유 고  
  너를 보낼 수는 없어  

  You're so good at being bad (Uh)  
  유어 쏘 굿 앳 빙 배드 (어)  
  너는 나쁜 사람이기를 너무 잘해, 너도 알다시피  

  [Post-Chorus]
  My baby's bad, you know  
  마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My baby's bad, you know  
  마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My baby, my, my, my baby's bad, you know  
  마이 베이비, 마이, 마이, 마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My, my baby's bad, you know  
  마이, 마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My, my baby's bad, you know  
  마이, 마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My baby, my, my, my baby's bad, you know  
  마이 베이비, 마이, 마이, 마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  [Verse 2]
  You know I'm not gonna leave your side, and I can't deny it  
  유 노우 아임 낫 거너 리브 유어 사이드, 앤드 아이 캔트 디나이 잇  
  내가 너의 곁을 떠나지 않을거라는걸 너도 알잖아, 그리고 나는 그걸 부정할 수 없어  

  Tried to play it cool but I can't hide my true desire  
  트라이드 투 플레이 잇 쿨 벗 아이 캔트 하이드 마이 트루 디자이어  
  쿨한척 하려 했는데 내 진실된 욕망을 숨길수가 없어  

  'Cause I can see the dirty in your eyes, my favourite liar  
  커즈 아이 캔 씨 더 더티 인 유어 아이즈, 마이 페이보릿 라이어  
  너의 눈에 비치는 더러움을 볼 수 있으니까, 넌 내가 제일 좋아하는 거짓말쟁이야  

  And I know you so well, well, well, well  
  앤드 아이 노우 유 쏘 웰, 웰, 웰, 웰  
  그리고 나는 너를 너무 잘 알지  

  [Chorus]
  So predictable  
  쏘 프레딕터블  
  너무 예상가능해  

  You're an animal  
  유어 언 애니멀  
  너는 동물이야  

  I can't let you go  
  아이 캔트 렛 유 고  
  너를 보낼 수는 없어  

  You're so good at being bad, you know  
  유어 쏘 굿 앳 빙 배드, 유 노우  
  너는 나쁜 사람이기를 너무 잘해, 너도 알다시피  

  So predictable  
  쏘 프레딕터블  
  너무 예상가능해  

  You're an animal  
  유어 언 애니멀  
  너는 동물이야  

  I can't let you go  
  아이 캔트 렛 유 고  
  너를 보낼 수는 없어  

  You're so good at being bad (Uh)  
  유어 쏘 굿 앳 빙 배드 (어)  
  너는 나쁜 사람이기를 너무 잘해, 너도 알다시피  

  [Post-Chorus]
  My baby's bad, you know  
  마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My baby's bad, you know  
  마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My baby, my, my, my baby's bad, you know  
  마이 베이비, 마이, 마이, 마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My, my baby's bad, you know  
  마이, 마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My, my baby's bad, you know  
  마이, 마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My baby, my, my, my baby's bad, you know  
  마이 베이비, 마이, 마이, 마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  [Bridge]
  I can see the way you look at me, waiting to attack  
  아이 캔 씨 더 웨이 유 룩 앳 미, 웨이팅 투 어택  
  네가 나를 보는 방식을 알아, 공격하려고 기다리고 있잖아  

  You are on your worst behaviour, I want it just like that  
  유 아 온 유어 워스트 비헤이비어, 아이 원트 잇 저스트 라이크 댓  
  너는 최악의 행동을 하려하고, 난 그냥 그런걸 원해  

  I can see the way you look at me, waiting to attack  
  아이 캔 씨 더 웨이 유 룩 앳 미, 웨이팅 투 어택  
  네가 나를 보는 방식을 알아, 공격하려고 기다리고 있잖아  

  You are on your worst behaviour, I want it just like that (Uh)  
  유 아 온 유어 워스트 비헤이비어, 아이 원트 잇 저스트 라이크 댓 (어)  
  너는 최악의 행동을 하려하고, 난 그냥 그런걸 원해  

  [Post-Chorus]
  My baby's bad, you know  
  마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My baby's bad, you know  
  마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My baby, my, my, my baby's bad, you know  
  마이 베이비, 마이, 마이, 마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My, my baby's bad, you know  
  마이, 마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My, my baby's bad, you know  
  마이, 마이 베이비즈 배드, 유 노우  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  My baby, my, my, my baby's bad, you know (Uh)  
  마이 베이비, 마이, 마이, 마이 베이비즈 배드, 유 노우 (어)  
  내 사랑은 나쁜사람이야, 너도 알잖아  

  [Chorus]
  So predictable (So predictable)  
  쏘 프레딕터블 (쏘 프레딕터블)  
  너무 예상가능해  

  You're an animal (You're an animal)  
  유어 언 애니멀 (유어 언 애니멀)  
  너는 동물이야  

  I can't let you go  
  아이 캔트 렛 유 고  
  너를 보낼 수는 없어  

  You're so good at being bad, you know  
  유어 쏘 굿 앳 빙 배드, 유 노우  
  너는 나쁜 사람이기를 너무 잘해, 너도 알다시피  

  So predictable  
  쏘 프레딕터블  
  너무 예상가능해  

  You're an animal  
  유어 언 애니멀  
  너는 동물이야  

  I can't let you go  
  아이 캔트 렛 유 고  
  너를 보낼 수는 없어  

  You're so good at being bad (Uh)  
  유어 쏘 굿 앳 빙 배드 (어)  
  너는 나쁜 사람이기를 너무 잘해, 너도 알다시피

  ---

  # 오늘의 단어 (TOEIC 및 OPIc 수준별 분류)

  ## TOEIC 300-400점 / OPIc Novice
  - Another (또 다른)
  - Friend (친구)
  - Start (시작)
  - End (끝)
  - Know (알다)
  - Well (잘)
  - Side (옆)
  - Play (놀다, 하다)
  - Eyes (눈)
  - Look (보다)

  ## TOEIC 500-600점 / OPIc Intermediate
  - Predictable (예상 가능한)
  - Animal (동물)
  - Desire (욕망)
  - Favourite (가장 좋아하는)
  - Liar (거짓말쟁이)
  - Deny (부정하다)
  - Behaviour (행동)
  - Cool (쿨한, 멋진)
  - Attack (공격하다)
  - Dirty (더러운)

  ## TOEIC 700-800점 / OPIc Advanced
  - Finally (마침내)
  - Ever since (이후로 쭉)
  - Corner (모퉁이, 구석)
  - Over (끝난)
  - True (진실된)
  - Hide (숨기다)
  - Just (그냥, 단지)
  - Worst (최악의)
  - Waiting (기다리는)
  - Found (발견했다, 찾았다)

  ### 수준 분석

  **TOEIC 300-400점 / OPIc Novice**
  - 가사 기준으로 간단한 단어들로 구성되어 있어 초급 수준의 이해도 필요

  **TOEIC 500-600점 / OPIc Intermediate**
  - 감정 표현과 상황 설명에 필요한 단어들로, 중급 수준의 이해도 필요

  **TOEIC 700-800점 / OPIc Advanced**
  - 문맥상 이해가 필요하고, 감정과 상황을 더 정교하게 표현할 수 있는 단어들로 구성되어 있어 고급 수준의 이해도 필요

  ### 예시
  **TOEIC 300-400점 / OPIc Novice**
  - I don't wanna be another him, that shit is over.  
    나는 또다른 너의 남자가 되고싶진 않아, 그런건 이제 끝이야.

  **TOEIC 500-600점 / OPIc Intermediate**
  - So predictable, you're an animal.  
    너무 예상가능해, 너는 동물이야.

  **TOEIC 700-800점 / OPIc Advanced**
  - Ever since the start, I saw the end around the corner.  
    시작부터 난 코앞에 다가온 끝을 봤어.



  ''',
      
      tags=["Christopher", "Bad", "영어 노래", "영어 가사", "영어 공부", "노래 학습"],
      series="Christopher",
      description="영어 노래 가사를 해석하고 발음을 익히며 영어를 학습해봅시다."
  )

  print(response)
