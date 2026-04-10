#중요
#함수, class, 조건문, 반복문 
import sys

print("Hello, Python!")
print("-" * 20)
print(f"현재 실행 중인 파이썬 버전: {sys.version}")
print("-" * 20)
print("축하합니다! 파이썬이 정상적으로 작동하고 있습니다.")

# 1. 리스트 (List): 수정이 가능함, 대괄호 [] 사용
my_list = ["사과", "바나나", "포도"]
my_list[0] = "딸기" # 사과를 딸기로 바꿀 수 있어요.
print(f"리스트 결과: {my_list}")
# 2. 튜플 (Tuple): 수정이 불가능함, 소괄호 () 사용
# 보통 변하지 않는 설정값이나 보안이 필요한 데이터를 담을 때 써요.
my_tuple = ("서울", "도쿄", "뉴욕")
# my_tuple[0] = "부산"  <-- 이렇게 하면 에러가 발생합니다!
print(f"튜플 결과: {my_tuple}")

"""
메모: 
리스트는 메뉴판처럼 항목을 추가/삭제할 때 좋고,
튜플은 주민번호나 좌표처럼 바뀌면 안 되는 데이터에 좋아요.
"""
# 3.(중요) 딕셔너리 (Dictionary): 키-값 쌍으로 데이터를 저장, 중괄호 {} 사용
my_dict = {"이름": "홍길동", "나이": 30, "직업": "개발자"}
print(f"딕셔너리 결과: {my_dict}")
# 딕셔너리는 키를 통해 값을 쉽게 찾을 수 있어요.
# 4. 집합 (Set): 중복을 허용하지 않는 데이터 구조, 중괄호 {} 사용
my_set = {1, 2, 3, 4, 5}
print(f"집합 결과: {my_set}")
# 집합은 중복된 값을 자동으로 제거해 줍니다.    
# 5. 문자열 (String): 텍스트 데이터를 저장, 작은따옴표 '' 또는 큰따옴표 "" 사용
my_string = "안녕하세요, 파이썬!"
print(f"문자열 결과: {my_string}")
# 문자열은 텍스트 데이터를 다루는 데 사용됩니다.
# 6. 불리언 (Boolean): 참(True) 또는 거짓(False) 값을 가지는 데이터 타입
my_boolean = True
print(f"불리언 결과: {my_boolean}")
# 불리언은 조건문에서 자주 사용됩니다.
# 7. None: 값이 없음을 나타내는 특별한 데이터 타입
my_none = None
print(f"None 결과: {my_none}")
# None은 변수에 값이 없음을 명시적으로 나타낼 때 사용됩니다.
# 8. 숫자 (Number): 정수(int)와 실수(float)로 나뉨 double은 파이썬에서 지원하지 않음
my_int = 42
my_float = 3.14
print(f"정수 결과: {my_int}")
print(f"실수 결과: {my_float}")
# 숫자는 수학적 계산에 사용됩니다.
# 9. 복소수 (Complex): 실수와 허수로 구성된 숫자 타입
my_complex = 2 + 3j
print(f"복소수 결과: {my_complex}")
# 복소수는 과학과 공학에서 사용됩니다.

# 10. 바이트 (Bytes): 이진 데이터를 저장하는 타입
my_bytes = b"Hello, Bytes!"
print(f"바이트 결과: {my_bytes}")
# 바이트는 파일 입출력이나 네트워크 통신에서 사용됩니다.
# 11. 바이트 배열 (Bytearray): 수정 가능한 바이트 시퀀스
my_bytearray = bytearray(b"Hello, Bytearray!")
print(f"바이트 배열 결과: {my_bytearray}")
# 바이트 배열은 바이트 데이터를 수정할 수 있게 해줍니다.
# 12. 메모뷰 (Memoryview): 바이트 데이터를 효율적으로 다루는 타입
my_memoryview = memoryview(b"Hello, Memoryview!")
print(f"메모뷰 결과: {my_memoryview}")
# 메모뷰는 큰 바이트 데이터를 효율적으로 처리할 때 사용됩니다.
# 13. 범위 (Range): 숫자 시퀀스를 생성하는 타입
my_range = range(1, 10)
print(f"범위 결과: {list(my_range)}")
# 범위는 반복문에서 자주 사용됩니다.
# 14. 프리즈드셋 (Frozenset): 수정이 불가능한 집합
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(f"프리즈드셋 결과: {my_frozenset}")
# 프리즈드셋은 집합과 달리 수정할 수 없는 집합입니다.
# 15. 데이트타임 (Datetime): 날짜와 시간을 다루는 타입
import datetime
my_datetime = datetime.datetime.now()
print(f"데이트타임 결과: {my_datetime}")
# 데이트타임은 날짜와 시간을 쉽게 다룰 수 있게 해줍니다.
# 16. 리스트 컴프리헨션 (List Comprehension): 간결한 리스트 생성 방법
squared_numbers = [x**2 for x in range(1, 11)]
print(f"리스트 컴프리헨션 결과: {squared_numbers}")
# 리스트 컴프리헨션은 반복문과 조건문을 한 줄로 표현
# 17. 제너레이터 (Generator): 메모리를 효율적으로 사용하는 반복자
def my_generator():

    for i in range(1, 6):
        yield i * i
gen = my_generator()
print("제너레이터 결과:")
for value in gen:
    print(value)
# 제너레이터는 필요한 값만 생성하여 메모리를 절약할 수 있습니다.
# 18. 람다 함수 (Lambda Function): 간단한 익명 함수
add = lambda x, y: x + y
result = add(5, 3)
print(f"람다 함수 결과: {result}")
# 람다 함수는 간단한 함수를 한 줄로 작성할 때 유용합니다.
# 19. (중요)클래스 (Class): 객체 지향 프로그래밍을 위한 데이터 타입
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person = Person("홍길동", 30)
print(f"클래스 결과: 이름={person.name}, 나이={person.age}")
# 클래스는 객체 지향 프로그래밍에서 데이터와 기능을 묶어주는 역할을 합니다.

# 20. 모듈 (Module): 관련된 함수와 클래스를 모아놓은 파일
import math
print(f"모듈 결과: 원주율={math.pi}")
# 모듈은 코드의 재사용성과 조직화를 돕습니다.
# 21. 패키지 (Package): 관련된 모듈을 모아놓은 디렉토리
# 패키지는 모듈을 그룹화하여 더 큰 프로젝트를 관리하는 데 사용됩니다.
# 22. 예외 (Exception): 오류를 처리하는 데이터 타입
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"예외 결과: {e}")
# 예외는 프로그램에서 발생할 수 있는 오류를 처리하는 데 사용됩니다.
# 23. 파일 (File): 파일 입출력을 위한 데이터 타입
with open("example.txt", "w") as file:
    file.write("Hello, File!")
print("파일 결과: example.txt 파일이 생성되었습니다.")
# 파일은 데이터를 영구적으로 저장하는 데 사용됩니다.
# 24. 함수 (Function): 재사용 가능한 코드 블록
def greet(name):
    return f"안녕하세요, {name}!"
print(f"함수 결과: {greet('홍길동')}")
# 함수는 특정 작업을 수행하는 코드 블록으로, 재사용이 가능합니다.
# 25. 제너레이터 표현식 (Generator Expression): 간결한 제너레이터 생성 방법
squared_gen = (x**2 for x in range(1, 11))
print(f"제너레이터 표현식 결과: {list(squared_gen)}")
# 제너레이터 표현식은 리스트 컴프리헨션과 비슷하지만, 메모리를 절약할 수 있습니다.
# 26. 데코레이터 (Decorator): 함수나 클래스를 수정하는 함수
def my_decorator(func):
    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")
    return wrapper
@my_decorator
def say_hello():
    print("안녕하세요!")
print("데코레이터 결과:")
say_hello()
# 데코레이터는 함수나 클래스의 동작을 수정하는 데 사용됩니다.
# 27. 컨텍스트 매니저 (Context Manager): 리소스 관리를 위한 데이터 타입
with open("example.txt", "r") as file:
    content = file.read()
print(f"컨텍스트 매니저 결과: {content}")
# 컨텍스트 매니저는 리소스를 자동으로 관리하는 데 사용됩니다.
# 28. 이터레이터 (Iterator): 반복 가능한 객체를 생성하는 데이터 타입
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list) 
print(f"이터레이터 결과: {next(my_iterator)}")
print(f"이터레이터 결과: {next(my_iterator)}")
# 이터레이터는 반복 가능한 객체를 순회하는 데 사용됩니다.
# 29. 제너레이터 함수 (Generator Function): 제너레이터를 생성하는 함수
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(5)
print("제너레이터 함수 결과:")
for number in counter:
    print(number)
# 제너레이터 함수는 yield 키워드를 사용하여 제너레이터를 생성하는 함수입니다.
# 30. (중요) 클래스 메서드 (Class Method): 클래스 레벨에서 동작하는 메서드
class MyClass:
    class_variable = "클래스 변수"
    
    @classmethod
    def class_method(cls):
        return f"클래스 메서드에서 클래스 변수: {cls.class_variable}"
print(f"클래스 메서드 결과: {MyClass.class_method()}")
# 클래스 메서드는 클래스 자체에서 호출할 수 있는 메서드입니다.

#31. 정적 메서드 (Static Method): 클래스와 인스턴스 모두에서 호출할 수 있는 메서드
class MyStaticClass:
    @staticmethod
    def static_method():
        return "정적 메서드입니다."
print(f"정적 메서드 결과: {MyStaticClass.static_method()}")
# 정적 메서드는 클래스나 인스턴스와 상관없이 호출할 수 있는 메서드입니다.
