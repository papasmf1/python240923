import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 파일 이동 경로 설정
folders = {
    'images': ['.jpg', '.jpeg', '.JPG', '.JPEG'],
    'data': ['.csv', '.xlsx'],
    'docs': ['.txt', '.doc', '.pdf'],
    'archive': ['.zip']
}

# 각 폴더의 경로 설정 및 폴더 생성
for folder, extensions in folders.items():
    folder_path = os.path.join(download_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # 폴더가 없으면 생성

# 파일 이동 함수
def move_files():
    # 다운로드 폴더의 파일 목록 확인
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)
        
        # 파일인지 확인
        if os.path.isfile(file_path):
            # 파일의 확장자 확인
            _, ext = os.path.splitext(filename)
            ext = ext.lower()  # 확장자를 소문자로 변환
            
            # 확장자에 따라 파일 이동
            for folder, extensions in folders.items():
                if ext in extensions:
                    destination = os.path.join(download_folder, folder, filename)
                    print(f'Moving {filename} to {folder} folder.')
                    shutil.move(file_path, destination)  # 파일 이동
                    break

# 파일 이동 함수 실행
move_files()
