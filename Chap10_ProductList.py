import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sqlite3
import os.path

# 데이터베이스 처리를 담당하는 모델 클래스
class ProductModel:
    def __init__(self):
        # DB 파일이 있으면 연결, 없으면 새로 생성 후 연결
        if os.path.exists("ProductList.db"):
            self.con = sqlite3.connect("ProductList.db")
            self.cur = self.con.cursor()
        else:
            self.con = sqlite3.connect("ProductList.db")
            self.cur = self.con.cursor()
            # 테이블 생성
            self.cur.execute("create table Products (id integer primary key autoincrement, Name text, Price integer);")

    # 제품 추가
    def add_product(self, name, price):
        self.cur.execute("insert into Products (Name, Price) values(?,?);", (name, price))
        self.con.commit()

    # 제품 수정
    def update_product(self, product_id, name, price):
        self.cur.execute("update Products set name=?, price=? where id=?;", (name, price, product_id))
        self.con.commit()

    # 제품 삭제
    def remove_product(self, product_id):
        self.cur.execute("delete from Products where id=?;", (product_id,))
        self.con.commit()

    # 모든 제품 조회
    def get_all_products(self):
        self.cur.execute("select * from Products;")
        return self.cur.fetchall()

# 메인 윈도우 (뷰) 클래스: UI와 관련된 처리를 담당
class DemoForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

        # 모델 인스턴스 생성
        self.model = ProductModel()

        # UI 설정 및 시그널 연결
        self.setup_ui()

    def setupUi(self):
        # UI 파일 로딩
        uic.loadUi("Chap10_ProductList.ui", self)

    def setup_ui(self):
        # 엔터 키로 다음 입력 필드로 이동
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())

        # 버튼과 시그널 연결 (뷰에서 직접 처리)
        self.pushButton.clicked.connect(self.addProduct)  # 입력 버튼
        self.pushButton_2.clicked.connect(self.updateProduct)  # 수정 버튼
        self.pushButton_3.clicked.connect(self.removeProduct)  # 삭제 버튼
        self.pushButton_4.clicked.connect(self.getProduct)  # 검색 버튼

        # 더블클릭 시 필드에 데이터 채우기
        self.tableWidget.doubleClicked.connect(self.populate_fields)

        # 테이블 초기화
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)

        # 초기 데이터 불러오기
        self.getProduct()

    # 제품 추가
    def addProduct(self):
        name = self.prodName.text()
        price = self.prodPrice.text()

        if name and price:
            self.model.add_product(name, price)
            self.getProduct()

    # 제품 수정
    def updateProduct(self):
        product_id = self.prodID.text()
        name = self.prodName.text()
        price = self.prodPrice.text()

        if product_id and name and price:
            self.model.update_product(product_id, name, price)
            self.getProduct()

    # 제품 삭제
    def removeProduct(self):
        product_id = self.prodID.text()

        if product_id:
            self.model.remove_product(product_id)
            self.getProduct()

    # 제품 리스트 새로고침
    def getProduct(self):
        # 테이블 초기화
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)  # 기존 행 리셋

        products = self.model.get_all_products()
        for row, product in enumerate(products):
            self.tableWidget.insertRow(row)
            product_id = "{:10}".format(product[0])
            product_name = product[1]
            product_price = "{:10}".format(product[2])

            item_id = QTableWidgetItem(product_id)
            item_id.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, item_id)

            self.tableWidget.setItem(row, 1, QTableWidgetItem(product_name))

            item_price = QTableWidgetItem(product_price)
            item_price.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, item_price)

    # 테이블 더블 클릭 시 필드에 데이터 채우기
    def populate_fields(self):
        current_row = self.tableWidget.currentRow()
        self.prodID.setText(self.tableWidget.item(current_row, 0).text().strip())
        self.prodName.setText(self.tableWidget.item(current_row, 1).text())
        self.prodPrice.setText(self.tableWidget.item(current_row, 2).text().strip())

# 프로그램의 진입점
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 뷰 인스턴스 생성 (모델은 뷰 안에서 생성됨)
    view = DemoForm()

    # 프로그램 실행
    view.show()
    sys.exit(app.exec_())
