import re

# 이메일 주소를 검증하는 정규 표현식
# raw string notation:가공하지 않은 문자열 
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# 샘플 이메일 주소 리스트
email_samples = [
    "example@example.com",  # 유효
    "user.name@domain.co.kr",  # 유효
    "user_name@domain.com",  # 유효
    "user-name@domain.org",  # 유효
    "user+name@domain.net",  # 유효
    "username@domain",  # 유효하지 않음 (도메인 끝에 TLD 없음)
    "user@.com",  # 유효하지 않음 (잘못된 도메인)
    "user@domain..com",  # 유효하지 않음 (도메인에 연속된 점)
    "user@domain,com",  # 유효하지 않음 (잘못된 구두점)
    "@domain.com",  # 유효하지 않음 (사용자명 없음)
]

# 이메일 검증 함수
def check_email(email):
    if re.match(email_pattern, email):
        return True
    return False

# 이메일 주소 검사
for email in email_samples:
    print(f"{email}: {'Valid' if check_email(email) else 'Invalid'}")
