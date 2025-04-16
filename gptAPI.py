import os
import re

import openai
from dotenv import load_dotenv
from openai import OpenAI

import gptData
import Post

# 환경변수 불러오기 API 키 셋팅
load_dotenv()
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# OpenAI API 호출 함수
def call_chatgpt(subject, example, system_prompt, posting_topics, posted_titles):
    # 반환 형태
    formatType = '''
    data = {
    "title": "title",
    "markdown": ''' + "markdown" + ''',
    "tags": ["tag1", "tag2"],
    "series": "series",
    "description": "description"
    }
    '''
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "당신은 언어와 관련한 글을 포스팅 합니다. 당신의 전문 언어와 한국어를 번역하는 것을 자부심으로 가지는 파워블로거입니다."},
            {"role": "assistant", "content": "알겠습니다. 저는 해당 언어를 통달한 파워블로거 입니다. SEO 형식을 최적화 하여 포스팅을 작성해 드리겠습니다."},
            {"role": "user", "content": f"반드시 지켜주셔야 할 반환 형태입니다. 따로 변수를 만들고 data 변수의 key에 변수를 담지 마시고, data = key : 제목을 바로 입력해주세요. 변수 다른 거 넣지말고. 이런 식으로 부탁합니다. 반환 형태입니다. {formatType}. value 값의 변수를 따로 정의하지 마시고 key : '내용' 형태로 부탁합니다. 반드시 data 변수를 반환해야 합니다. markdown 변수에 마크다운 형태로 담아야 합니다. 그 말은 무슨 의미냐면  '''markdown''' 형태로 감싸야 합니다."},
            {"role": "assistant", "content": "알겠습니다. markdown 변수에는 반드시 markdown 형태로 담겠습니다. 또한, data 변수 자체를 반환하겠습니다. 또한, 반드시 data 변수의 key에 직접적으로 값을 할당하겠습니다."},
            {"role": "user", "content": f"좋았어요. 자, 이제 주제를 드리겠습니다. {subject} 주제에 맞는 독창적인 콘텐츠를 작성해 주세요. 언어 학습을 위한 것이기 때문에 외국어 부분의 언어를 한국어 발음으로도 적어주시고, 단어도 추출하여 하단에 오늘의 단어라는 컨텐츠도 추가해주세요. title에는 주제를 기반으로 당신의 언어도 반드시 포함 되어야 하고 그에 맞춰서 tag도 당신의 언어를 기반한 태그를 붙여야 합니다. ex) 일본 공항 데스크, 방콕 호텔에서의 표현 등등이요."},
        ] # 아래는 형태를 위한 예시일 뿐이야. 전부 다 따라하지는 마. 형태를 보여주기 위함이니까. 주제는 노래를 했었는데, 학습에 도움이 될만한 주제로 내용도 알차게 너가 알아서 작성해줘. 굳이 음악으로 하지 않아도 되니까. 여행이든 뭐든 주제를 너 맘대로 설정해줘. 뉴스 내용도 좋고 신문도 좋고 뭐든 좋아. 그냥 언어 기초 문법 기초 단어 이런 것도 괜찮고!
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

# 정규식을 사용하여 data 변수 내의 내용만 추출하는 함수
def extract_data_variable(subject, example, system_prompt, posting_topics, posted_titles, attempt=1, max_attempts=5):
    def convert_text(text):
        # \n을 실제 줄 바꿈으로 변환
        converted_text = text.replace('\\n', '\n')
        # 삼중 따옴표로 감싸기
        return f"'''\n{converted_text}\n'''"
    
    response = call_chatgpt(subject, example, system_prompt, posting_topics, posted_titles)
    
    pattern = re.compile(
        r'data\s*=\s*{\s*"title":\s*"([^"]+)",\s*"markdown":\s*\'\'\'(.*?)\'\'\'\s*,\s*"tags":\s*\[([^\]]+)\],\s*"series":\s*"([^"]+)",\s*"description":\s*"([^"]+)"\s*}', 
        re.DOTALL
    )
    match = pattern.search(response)
    if match:
        title, markdown, tags, series, description = match.groups()
        # tags를 리스트로 변환
        tags_list = [tag.strip().strip('"') for tag in tags.split(',')]
        data = {
            "title": title,
            "markdown": markdown,
            "tags": tags_list,
            "series": series,
            "description": description
        }
        data["markdown"] = convert_text(data["markdown"])
        return data
    
    elif attempt < max_attempts:
        print(f"Attempt {attempt} failed. Retrying...")
        return extract_data_variable(subject, example, system_prompt, posting_topics, posted_titles, attempt + 1, max_attempts=5)
    else:
        return
