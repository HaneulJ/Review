# 1/6 실습1

# 1번
print("<<1번>>")
# 다음과 같은 결과가 출력되도록 for문을 이용하여 구현한다.
#     1 2 3 4 5 6 7 8 9 10
for i in range(1,11):
    print(i,end=" ")

print("\n")

# 2번
print("<<2번>>")
#     9 : 홀수
#     8 : 짝수
#     7 : 홀수
#     6 : 짝수
#     5 : 홀수
#     4 : 짝수
for i in range(9,3,-1):
    if i % 2 == 0:
        print(i, ": 짝수")
    else:
        print(i, ": 홀수")


print("\n")

# 3번
print("<<3번>>")
# 1부터 10사이의 난수를 하나 추출한다.
# 30부터 40사이의 난수를 하나 추출한다.
# 첫 번째 난수부터 두 번째 난수까지의 숫자들 중에서 짝수의 합을 구해 다음 형식으로 출력한다.
# X 부터 Y 까지의 짝수의 합 : XX
import random
x = random.randint(1,10)
y = random.randint(30,40)

for i in range(x,y+1):
    if i % 2 ==0 :
        i += i
print(x,"부터", y,"까지의 짝수의 합:", i)


print("\n")
# 4번
print("<<4번>>")

# evenNum 변수와 oddNum 변수의 값을 0으로 대입한다.
# 1 부터 100 까지의 값 중에서 짝수의 합은 evenNum 에 누적하고 홀수의 합은 oddNum 에 누적한다.
import random
evenNum = 0
oddNum = 0

for i in range(1,101):
    if i % 2 == 0:
        evenNum += i
    else:
        oddNum += i
print("1부터 100까지의 숫자들 중에서\n짝수의 합은", evenNum,"이고\n홀수의 합은",oddNum,"이다.")

print("\n")
# 5번
print("<<5번>>")
# continue 문을 사용하지 않고 해결
# 1 부터 50까지의 숫자 중에서 3의 배수에 해당하는 값들의 합을 구한다. 단 5의배수는 제외한다.
# 다음과 같은 결과가 되도록 구현한다. 결과 = 318
sum = 0
for n in range(1,51):
    if n % 3 == 0 and n % 5 != 0:
        sum += n
print("결과: ", sum)

print("\n")
# 6번
print("<<6번>>")
# continue 문을 사용해서 해결
# 1 부터 50까지의 숫자 중에서 3의 배수에 해당하는 값들의 합을 구한다. 단 5의배수는 제외한다.
sum = 0
for n in range(1,51):
    if n % 3 == 0 and n % 5 != 0:
        sum += n
    else:
        continue
print("결과: ", sum)

print("\n")





