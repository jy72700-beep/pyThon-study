#함수, class, 조건문, 반복문 
'''
#조건문 예제
a = 3
if a > 1:
    print("a is greater than 1")

#반복문 예제
for a in [1, 2, 3]:
    print(a)

i = 0
while i < 3:
    i = i + 1
    print(i)


#함수 정의 및 예제
def add(a, b):
    return a + b

result = add(5, 3)
print("The result of addition is:", result)
'''
#02-자료형
'''
- int: 정수형
- float: 실수형
# ** 제곱값
a = 3
b = 4
a ** b # 3의 4제곱
# 나머지값
a = 10
b = 3
a % b # 10을 3으로 나눈 나머지값
# 몫값
a = 10
b = 3
a // b # 10을 3으로 나눈 몫값
- str: 문자열형
"아무거나 이런거 다 문자열"
"a"
"123" # 숫자처럼 보이지만 문자열
head = "Python"
tail = " is fun!"
print(head + tail) # 문자열 연결
#이렇게 하면 터미널에 Python is fun! 이 출력됨
- list: 리스트형
- dict: 딕셔너리형
- tuple: 튜플형
- set: 집합형
- bool: 불리언형

- NoneType: None
'''
'''
a = 14
b = 3
print(a // b)
print(a%b)
'''
'''
#multistring.py

print("=" * 50)
print("My Program")
print("=" * 50)
'''
'''
#len함수를 이용해 문자열 길이 구하기
a = "Life is too short"
print(len(a)) # 문자열의 길이 출력

a = "You need python"
print(len(a))
'''
'''
#문자열 인덱싱과 슬라이싱 인덱싱은 무엇인가를 가리킨다, 슬라이싱은 무엇인가를 잘라낸다.
a = "Life is too short, You need Python"
print(a[0]) # 문자열의 첫 번째 문자 출력
print(a[12]) # 문자열의 13번째 문자 출력
print(a[-1]) # 문자열의 마지막 문자 출력
print(a[-2]) # 문자열의 마지막에서 두 번째 문자 출력
'''
#문자열 슬라이싱
'''
a = "Life is too short, You need Python"
#print(a[0:5]) # 문자열의 0번째부터 4번째까지 출력 # 5번째는 포함되지 않음
#[0:5] 는 0 <= a < 5
print(a[3:-4])
'''
#문자열 포매팅 - 문자열 안의 특정한 값을 바꿔야 혹은 삽입 할 때 사용
'''
#숫자 바로 대입
"I eat %d apples." %3
print("I eat %d apples." %3)
#문자열 바로 대입
"I eat %s apples." %"five"
print("I eat %s apples." %"five")
#숫자면 %d, 문자열이면 %s
'''
'''
#변수로 대입
number = 3
print("I eat %d apples." %number)
'''
'''
#2개 이상의 값 넣기
number = 10
day = "three"
print("I eat %d apples. so I was sick for %s days." %(number, day))
'''
#포매팅 연산자 %s는 모든 자료형을 문자열로 바꿔서 출력
#만약 몇 프로 %를 출력하고 싶다면 %%로 하면 된다.
'''
#f문자열 포매팅
name = "홍길동"
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
#문자열 앞에 f를 붙이고, 변수를 중괄호 {} 안에 직접 넣는 방식입니다. 훨씬 깔끔하죠?
'''

fruits = ['apple', 'banana', 'cherry']

# 리스트 방식을 사용하면 단어 단위로 합쳐집니다.
result = ", ".join(fruits)
print(result) # 결과: apple, banana, cherry

#점프 투 파이썬 p.71
