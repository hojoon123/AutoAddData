import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from supabase import Client, create_client

# Supabase 설정
load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)


# 포스트 추가하기
def add_post(user_id: str, title: str, markdown: str, tags: list, series: str, description: str):
    # 현재 시간 가져오기
    created_at = datetime.now(timezone(timedelta(hours=9))).isoformat()

    # 데이터 삽입
    data = {
        "user_id": user_id,
        "title": title,
        "markdown": markdown,
        "tags": tags,
        "created_at": created_at,
        "series": series,
        "description": description
    }

    response = supabase.table("posts").insert(data).execute()
    return response

# 유저의 포스트 제목 리스트 가져오기
def get_post_titles_by_user(user_id: str):
    # 쿼리 실행
    response = supabase.table("posts").select("title").eq("user_id", user_id).execute()

    # 제목 리스트 추출
    titles = [post['title'] for post in response.data]

    return titles

# 유저 프로필 업데이트 함수
def update_profile(user_id: str, name: str, bio: str, one_line_intro: str, post_type: str):
    data = {
        "name": name,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "bio": bio,
        "one_line_intro": one_line_intro,
        "post_type": post_type
    }

    response = supabase.table("profiles").update(data).eq("id", user_id).execute()
    return response