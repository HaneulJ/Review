# 1/5 실습2

# 1번
print("<<1번>>")
# num 이라는 변수에 사용자로부터 숫자 하나를 입력받는다.
# 입력받은 숫자가 10보다 큰 경우에만 ‘OK’라는 문자열을 출력한다.
num = int(input("숫자를 입력하세요:"))
if num > 10:
    print("OK")
print()


# 2번
print("<<2번>>")
# color_name 이라는 변수에 사용자로부터 칼라 이름을 하나 입력받는다.
# 입력받은 칼라명이 red 이면 ‘#ff0000’라는 문자열을 출력한다.
# 입력받은 칼라명이 red 가 아니면 ‘#000000’라는 문자열을 출력한다.
color_name = input("색깔을 입력하세요:")
if color_name == "red":
    print("#ff0000")
else:
    print("#000000")
print()

# 3번
print("<<3번>>")
# grade 라는 변수에 1 부터 6 사이의 숫자를 랜덤으로 추출하고 저장한다.
# 조건 평가 시 and 연산자를 사용해서 해결한다.
# grade 의 값이 1 또는 2 또는 3이면 다음 결과를 출력한다.
import random
grade = random.randint(1,6)
if 1 <= grade and grade <= 3:
    print(grade, "학년은 저학년입니다.")
else:
    print(grade, "학년은 고학년입니다.","\n")

# 4번
print("<<4번>>")
# grade 라는 변수에 1 부터 6 사이의 숫자를 랜덤으로 추출하고 저장한다.
# 조건 평가 시 or 연산자를 사용해서 해결한다.
# grade 의 값이 1 또는 2 또는 3이면 다음 결과를 출력한다.
import random
grade = random.randint(1,6)
if grade == 1 or grade == 2 or grade == 3:
    print(grade,"학년은 저학년입니다.")
else:
    print(grade,"학년은 고학년입니다.", "\n")


# 5번
print("<<5번>>")
# score 라는 변수에 0 부터 100 사이의 숫자를 랜덤으로 추출하고 저장한다.
# score 변수의 값의 크기에 따라서 다음의 내용을 출력한다.  print() 함수를 5개 사용하여 해결한다.
# score 변수의 값이 90~100 이면   xx점은 A등급입니다.
# score 변수의 값이 80~89 이면   xx점은 B등급입니다.
# score 변수의 값이 70~79 이면   xx점은 C등급입니다.
# score 변수의 값이 60~69 이면   xx점은 D등급입니다.
# score 변수의 값이 0~59 이면   xx점은 F등급입니다.
import random
score = random.randint(0,100)
if 90 <= score <= 100:
    print(score, "점은 A등급입니다.")
elif 80 <= score <= 89:
    print(score, "점은 B등급입니다.")
elif 70 <= score <= 79:
    print(score, "점은 C등급입니다.")
elif 60 <= score <= 69:
    print(score, "점은 D등급입니다.")
else:
    print(score, "점은 F등급입니다.")

print()

# 6번
print("<<6번>>")
# 위를 복사해 한 개의 print() 함수로 해결한다.
import random
score = random.randint(0,100)
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
else:
    graed = "F"
print(score,"점은",grade,"등급입니다.")

print()

# 7번
print("<<7번>>")
# num 이라는 변수에 사용자로부터 숫자 하나를 입력받는다.
# 입력 받을 때의 메시지- 1부터 10사이의 숫자를 하나 입력하세요 :
num = input("1부터 10사이의 숫자를 하나 입력하세요:")
if 1 <= num <= 10:
    if num % 2 == 0:
        print(num, ": 짝수")
    else:
        print(num, ": 홀수")
else:
    print("1부터 10사이의 값이 아닙니다.")

print()

# 8번
print("<<8번>>")
# oper_num 이라는 변수에 1부터 10사이의 랜덤값을 추출하여 대입한다.
# 추출된 값이 1이거나 6이면 300 과 50 의 덧셈 연산을 처리한다.
# 추출된 값이 2이거나 7이면 300 과 50 의 뺄셈 연산을 처리한다.
# 추출된 값이 3이거나 8이면 300 과 50 의 곱센 연산을 처리한다.
# 추출된 값이 4이거나 9이면 300 과 50 의 나눗셈 연산을 처리한다.
# 추출된 값이 5이거나 10이면 300 과 50 의 나머지 연산을 처리한다.
# 출력 형식(단, 결과를 출력하는 수행문장은 한 번만 구현한다.  결과값 : XX
import random

oper_num = random.randint(1,10)
if oper_num == 1 or oper_num == 6:
    result = 300 + 50
elif oper_num == 2 or oper_num == 7:
    result = 300 - 50
elif oper_num == 3 or oper_num == 8:
    result = 300 * 50
elif oper_num == 4 or oper_num == 9:
    result = 300 / 50
else:
    result = 300 % 50
print("결과값: ", result)