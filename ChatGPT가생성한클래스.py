# Person 클래스 정의
class Person:
    """
    Person 클래스는 사람을 나타내는 기본 클래스입니다.
    
    속성:
        id (int): 사람의 고유 번호입니다.
        name (str): 사람의 이름입니다.
    
    메서드:
        printInfo(): 사람의 id와 이름을 출력합니다.
    """

    def __init__(self, id, name):
        """
        Person 클래스의 생성자입니다.
        
        Args:
            id (int): 사람의 고유 번호입니다.
            name (str): 사람의 이름입니다.
        """
        self.id = id  # 사람의 고유 번호를 저장
        self.name = name  # 사람의 이름을 저장

    def printInfo(self):
        """
        사람의 id와 이름을 출력하는 메서드입니다.
        """
        print(f"ID: {self.id}, Name: {self.name}")


# Manager 클래스 정의 (Person 클래스를 상속)
class Manager(Person):
    """
    Manager 클래스는 관리자를 나타내며, Person 클래스를 상속받아 확장된 클래스입니다.
    
    속성:
        title (str): 관리자의 직책을 나타냅니다.
    
    메서드:
        printInfo(): 사람의 정보와 함께 직책을 출력합니다.
    """

    def __init__(self, id, name, title):
        """
        Manager 클래스의 생성자입니다.
        
        Args:
            id (int): 관리자의 고유 번호입니다.
            name (str): 관리자의 이름입니다.
            title (str): 관리자의 직책입니다.
        """
        super().__init__(id, name)  # 상속받은 Person 클래스의 생성자를 호출하여 id와 name을 설정
        self.title = title  # 관리자의 직책을 저장

    def printInfo(self):
        """
        사람의 정보와 직책을 출력하는 메서드입니다.
        """
        super().printInfo()  # Person 클래스의 printInfo() 메서드를 호출하여 id와 name을 출력
        print(f"Title: {self.title}")  # 관리자의 직책을 출력


# Employee 클래스 정의 (Person 클래스를 상속)
class Employee(Person):
    """
    Employee 클래스는 직원을 나타내며, Person 클래스를 상속받아 확장된 클래스입니다.
    
    속성:
        skill (str): 직원의 기술을 나타냅니다.
    
    메서드:
        printInfo(): 사람의 정보와 함께 기술을 출력합니다.
    """

    def __init__(self, id, name, skill):
        """
        Employee 클래스의 생성자입니다.
        
        Args:
            id (int): 직원의 고유 번호입니다.
            name (str): 직원의 이름입니다.
            skill (str): 직원의 기술입니다.
        """
        super().__init__(id, name)  # 상속받은 Person 클래스의 생성자를 호출하여 id와 name을 설정
        self.skill = skill  # 직원의 기술을 저장

    def printInfo(self):
        """
        사람의 정보와 기술을 출력하는 메서드입니다.
        """
        super().printInfo()  # Person 클래스의 printInfo() 메서드를 호출하여 id와 name을 출력
        print(f"Skill: {self.skill}")  # 직원의 기술을 출력


# 테스트 코드
def test_person_classes():
    """
    Person, Manager, Employee 클래스의 다양한 기능을 테스트하는 함수입니다.
    
    각 클래스의 객체를 생성하고, printInfo() 메서드를 호출하여 정보를 출력합니다.
    또한, 속성 변경과 객체 타입 확인을 통해 올바르게 동작하는지 검증합니다.
    """
    # 1. Person 객체 생성 및 출력 테스트
    person1 = Person(1, "Alice")
    person1.printInfo()  # 출력: ID: 1, Name:


m1 = Manager(100, "김길동", "프로")
m1.printInfo() 

