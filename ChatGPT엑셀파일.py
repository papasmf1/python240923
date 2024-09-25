import openpyxl
import random

# 엑셀 파일 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Product Sales Data"

# 데이터 헤더 작성
ws.append(["제품ID", "제품명", "수량", "가격"])

# 제품명 리스트
product_names = ["Laptop", "Smartphone", "Tablet", "Smartwatch", "Headphones",
                 "Monitor", "Keyboard", "Mouse", "Printer", "Camera"]

# 랜덤 데이터 생성 및 엑셀에 추가
for i in range(1, 101):  # 100개의 데이터 생성
    product_id = f"P{i:03d}"  # 제품 ID: P001, P002, ...
    product_name = random.choice(product_names)  # 제품명은 랜덤 선택
    quantity = random.randint(1, 100)  # 수량: 1 ~ 100개 랜덤
    price = random.randint(100, 2000)  # 가격: 100 ~ 2000 달러 랜덤
    
    # 엑셀에 데이터 추가
    ws.append([product_id, product_name, quantity, price])

# 엑셀 파일 저장
wb.save("products.xlsx")

print("products.xlsx 파일이 생성되었습니다.")
