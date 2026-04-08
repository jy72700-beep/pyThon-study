#리스트: 서로 연관된 데이터를 잘 모아 정리정돈 하는 환상적인 도구
#연관된 데이터 - 원소; element
# list_name = [e1,e2,e3]
#변수
students = ["jun","chan","yugo"]
grades = [1,2,3]
#chan이를 꺼내고 싶다
print("students[1]", students[1])
#len 
print("len(students)", len(students))
#minimum
print("min(grades)", min(grades))
#maximum
print("max(grades)", max(grades))
#sum
print("sum(grades)", sum(grades))


#통계 관련 모듈 설치
import statistics
print("statistics.mean(grades)", statistics.mean(grades)) #mean

import random
print("random.random()", random.random()) #중요 random.random뒤에 반드시 ()를 붙여야 됨 
print("무작위 숫자:", random.random())

#random.choice() 리스트 안에서 랜덤으로 원소를 뽑아줄거임
print("random.choice(students)", random.choice(students))



