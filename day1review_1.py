# 1/5 실습1

# 1번
"""
- v1 변수에 100을 대입한다.
- v2 변수에 50을 대입한다.
- v1 과 v2 의 덧셈 결과를 r1 변수에 저장한다.
- v1 과 v2 의 뺄셈 결과를 r2 변수에 저장한다.
- v1 과 v2 의 곱셈 결과를 r3 변수에 저장한다.
- v1 과 v2 의 나눗셈 결과를 r4 변수에 저장한다.
r1, r2, r3, r4 변수의 값을 다음과 같이 출력한다.
"""
print("<<1번>>")
v1 = 100
v2 = 50
r1 = v1 + v2
r2 = v1 - v2
r3 = v1 * v2
r4 = v1 / v2

print("r1 = ", r1)
print("r2 = ", r2)
print("r3 = ", r3)
print("r4 = ", r4, "\n")


# 2번
print("<<2번>>")
name1 = "올"
name2 = "라"
name3 = "프"

print(name1, name2, name3, sep="")
print(name1, name2, name3, sep="@")
print(name1, name2, name3, sep="---",)
print()

# 3번
# 다음 숫자들의 합계와 평균을 구해서 제시된 형식으로 출력한다.(변수에 저장하는 것은 자율)
# 10, 25, 34
print("<<3번>>")
a = 10; b = 25; c = 34
sum = a + b + c
avg = sum / 3
print("합은", sum,"이고 평균은", avg, "입니다.")
print()