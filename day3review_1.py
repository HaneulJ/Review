# 1/7 실습1

# 1번
print("<<1번>>")
# 5부터 10사이의 난수를 추출한다.
# 1부터 추출된 숫자값까지의 각 숫자들의 제곱값을 행단위로 출력한다.
# ===>  7이 추출되면
# 1 -> 1
# 2 -> 4
# 3 -> 9
# 4 -> 16
# 5 -> 25
# 6 -> 36
# 7 -> 49
import random
i = 1
n = random.randint(5,10)
while i <= n :
    print(i, "->", i**2)
    i += 1

print("\n")

# 2번
print("<<2번>>")
# 1부터 6사이의 두 개 난수를 추출하여 각각 pairNum1, pairNum2 에 저장한다. 추출된 두 개의 숫자가 서로 다르면 값의 크기를 비교하여
# "pairNum1이 pairNum2 보다 크다." 또는 "pairNum1이 pairNum2 보다 작다." 출력한다.

import random
pairNum1 = random.randint(1,6)
pairNum2 = random.randint(1,6)
while True:
    if pairNum1 < pairNum2:
        print("pairNum1이 pairNum2보다 작다.")
    elif pairNum1 > pairNum2:
        print("pairNum1이 pairNum2보다 크다.")
    else:
        print("게임 끝")
    break

print("\n")
# 3번
print("<<3번>>")
# 0부터 30사이의 난수를 추출한다.
# 추출된 숫자가 1이면 'A', 2 이면 'B', ... 26이면 'Z' 를 출력하는데 계속 난수 추출과 출력을 반복하다가 난수가 0이 추출되거나
# 27~30이 추출되면 반복을 끝낸다.
# 반복하는 동안 출력형식 :B(2)
# 마지막에는 "수행횟수는 x 번입니다"를 출력하고 종료한다. 수행 횟수는 출력을 기준으로 계산한다.
import random
count = 0
# i = random.randint(0,30) 가 여기에 있으면 하나의 i만 무한루프
while True:
    i = random.randint(0,30)
    if 1 <= i < 27:
        count += 1
        print(chr(i+64),"(",i,")",sep="")
    else:
        break
print("수행횟수는", count, "번입니다.")

print("\n")
# 4번
print("<<4번>>")
# 사용자로부터 월에 해당하는 숫자를 하나 입력 받는다.
# 입력된 숫자가 1~12 사이의 값이면
# 12, 1, 2의 경우엔 x월은 겨울
# 3, 4, 5의 경우엔 x월은 봄
# 6, 7, 8의 경우엔 x월은 여름
# 9, 10, 11의 경우엔 x월은 가을을 출력한다.
# 입력된 숫자가 1~12 사이가 아니면 1~12 사이의 값을 입력하세요! 를 출력하고 종료한다.
n = int(input("숫자를 입력하세요:"))
while True:
    if n == 1 or n == 2 or n == 12:
        print(n,"월은 겨울")
    elif 3 <= n <= 5:
        print(n, "월은 봄")
    elif 6 <= n <= 8:
        print(n, "월은 여름")
    elif 9 <= n <= 11:
        print(n, "월은 가을")
    else:
        print("1~12 사이의 값을 입력하세요!")
    break

print("\n")

# 5번
print("<<5번>>")
# 사용자로부터 문자열을 하나 입력받아 word 라는 변수에 저장한다.
# word 변수에 저장된 데이터의 길이를 추출하여(문자열 길이는 len() 이라는 함수를 사용한다.) wordlength 라는 변수에 저장한다.
# wordlength 라는 변수에 할당된 값에 따라서 다음 기능을 수행한다.
# wordlength 라는 변수의 값이 0 이면 반복을 종료한다.
# wordlength 라는 변수의 값이 5 이상이고 8 이하이면 아무 기능도 수행하지 않고 입력받는 기능부터 다시 수행한다.
# wordlength 라는 변수의 값이 5 미만이면 문자열의 앞과 뒤에 “*” 기호를 붙여서 result 변수에 저장한다.
# wordlength 라는 변수의 값이 8 초과이면 문자열의 앞과 뒤에 “$” 기호를 붙여서 result 변수에 저장한다.
# result 변수의 값을 다음 형식으로 출력한다. 유효한 입력 결과 : ........

# word = str(input("문자를 입력하세요:"))
# wordlength = len(word)
# while문 전에 먼저 호출하면 하나의 문자열만 무한루프
while True:
    word = str(input("문자를 입력하세요:"))
    wordlength = len(word)
    if 5 <= wordlength <= 8:
        continue
    elif 0 < wordlength < 5:
        result = "*"+word+"*"
    elif wordlength == 0:
        print("종료")
        break
    else:
        result = "$"+word+"$"
    print("유효한 입력 결과:", result)

print("\n")

# 6번
print("<<6번>>")
# 숫자를 하나 입력받는다.
# 입력된 숫자가 0 이면 “종료”라는 메시지를 출력하고 수행을 종료한다.
# 입력된 숫자가 -10 보다 작거나 10보다 크면 입력 받는 것부터 다시 시작한다.
# 입력된 숫자가 양수이면 “입력값 : x” 행을 출력한 다음 행에 1부터 입력된 숫자 값까지의 곱한 결과를 출력한다.
# 입력된 숫자가 음수이면 양수로 변경하여 “입력값(부호변경) : x” 를 출력한 다음 행에 1부터 입력된 숫자 값까지의 곱한 결과를 출력한다.
while True:
    num = int(input("숫자를 입력하시오:"))
    sum = 1
    if  -10 > num or num < 10:
        continue
    elif 0 < num:
        for i in range(1,num+1):
            sum *= i
        print("입력값:", num)
        print(sum)
    elif num < 0:
        num *= (-1)
        for i in range(1,num+1):
            sum *= i
        print("입력값(부호 변경):",num)
        print(sum)
    elif num == 0:
        print("종료")
        break