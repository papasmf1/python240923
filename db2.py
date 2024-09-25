# db1.py 
import sqlite3

#영구적으로 파일에 저장(커밋을 해서 정상적 완료)
con = sqlite3.connect("c:\\work\\sample.db")
#SQL구문은 커서객체 실행
cur = con.cursor() 
#테이블 구조를 생성(테이블 스키마)
cur.execute("create table if not exists PhoneBook (Name text, PhoneNum text);")
#1건을 입력 
cur.execute("insert into PhoneBook values ('김길동','010-111-1234');")
#입력 파라메터 처리 
name = "전우치"
phoneNumber = "010-222-1234"
cur.execute("insert into PhoneBook values (?,?);", (name, phoneNumber))
#다중의 행을 처리
datalist = (("박문수","010-345-5678"), ("홍길동","010-333-1234"))
cur.executemany("insert into PhoneBook values (?,?);", datalist)

#검색 
cur.execute("select * from PhoneBook;")
#선택한 블록: ctrl + / 
for row in cur:
    print(row[0], row[1])

#완료
con.commit() 
