# 1/8 실습1

# 1번
print("<<1번>>")
# 함수명 : print_triangle_withdeco
# 매개변수 : 2개, 숫자와 데코문자, 여기에서 데코문자는 기본값을 갖는다. 기본값은 ‘%’로 정한다.
# 리턴값 : 없음, 기능 : 전달된 숫자 개수로 구성되는 반대 삼각형 출력

def print_triangle_withdeco(n,deco="%"):
    if 1 <= n <= 10:
        for i in range(1,n+1):
            print(" "*(10-i),deco*i)

print_triangle_withdeco(3)
print_triangle_withdeco(5,"@")


print("\n")
# 2번
print("<<2번>>")

# 최댓값을 구하는 기능은 함수를 사용하지 않고 제어문으로 직접 구현한다.
# 다음 값들로 구성되는 리스트를 생성하여 listnum 에 저장한다. 10, 5, 7, 21, 4, 8, 18
# listnum에 저장된 값들 중에서 최댓값을 추출하여 출력한다.
listnum=[10,5,7,21,4,8,18]
lmax = listnum[0]

for i in range(1,len(listnum)):
    if lmax < listnum[i]:
        lmax = listnum[i]
print("최댓값:",lmax)


print("\n")
# 3번
print("<<3번>>")
# 최솟값을 구하는 기능은 함수를 사용하지 않고 제어문으로 직접 구현한다.
# 다음 값들로 구성되는 리스트를 생성하여 listnum2에 저장한다. 10, 5, 7, 21, 4, 8, 18
# listnum에 저장된 값들 중에서 최솟값을 추출하여 출력한다.
lmin=listnum[0]
for i in range(1,len(listnum)):
    if lmin > listnum[i]:
        lmin = listnum[i]
print("최솟값:",lmin)


print("\n")
# 5번
print("<<5번>>")
# 비어있는 리스트를 하나 생성하여 listnum2 이라는 변수에 저장한다.
# 1~50 사이의 난수를 10개 추출하여 listnum2 에 추출 순서대로 저장한다. (for문 사용)
# listnum2의 모든 값들을 출력한다.(이 때 반복문을 사용하지 않아도 된다.)
listnum2=[]
import random
for i in range(10):
    listnum2.append(random.randint(1,50))
print(listnum2)

# 리스트에서 10보다 작은 값들은 100으로 변경한다. (for문 사용)
# listnum2의 모든 값들을 출력한다.(이 때 반복문을 사용하지 않아도 된다.)
for n in range(10):
    if 10 > listnum2[n]:
        listnum2[n] = 100
print(listnum2)

# 인덱싱 방법으로 listnum2의 첫 번째 데이터를 출력한다.
print(listnum2[0])

# 인덱싱 방법으로 listnum2의 마지막 데이터를 출력한다.
print(listnum2[-1])

# 슬라이싱 방법으로 listnum2의  두 번째 데이터부터 여섯 번째 데이터만 추출하여 출력한다.
print(listnum2[1:6])

# 슬라이싱 방법으로 listnum2의 데이터를 역순으로 출력한다.
print(listnum2[::-1])

# 슬라이싱 방법으로 listnum2의 데이터를 모두 출력한다.
print(listnum2[:])

# 인덱싱 방법으로 5번째 데이터를 삭제한다.
del listnum2[4]

# 슬라이싱 방법으로 listnum2의 데이터를 모두 출력한다.
print(listnum2[:])

# 슬라이싱 방법으로 2~3번째 데이터를 삭제한다.
listnum2[1:3]=[]

# 슬라이싱 방법으로 listnum2의 데이터를 모두 출력한다.
print(listnum2[:])


print("\n")
# 6번
print("<<6번>>")
# 함수명 : sumEven1
# 매개변수 : 가변형(전달받을 수 있는 아규먼트 개수에 제한이 없다.), 리턴값 : 1개
# 기능 : 아규먼트가 몇 개가 전달되든 처리해야 한다.
#       아규먼트는 1 이상의 숫자만 온다고 정한다.
#       전달된 아규먼트들에서 짝수에 해당하는 숫자들만 합을 계산해서 리턴한다.
#       전달된 아규먼트들 중에 짝수가 없으면 0을 리턴한다.
#       아규먼트가 전달되지 않으면 -1을 리턴한다.
def sumEven1(*p):
    sum = 0
    for n in p:
        if n % 2 == 0:
            sum += n
    if len(p) == 0:
        sum = -1
    return sum

print(sumEven1(6,7,9,10))
print(sumEven1())

print("\n")
# 7번
print("<<7번>>")
# 함수명 : sumAll
# 매개변수 : 가변형(전달받을 수 있는 아규먼트 개수에 제한이 없다.), 리턴값 : 1개
# 기능 : 아규먼트가 몇 개가 전달되든 처리해야 한다.
# 호출시 전달되는 아규먼트의 데이터 타입에는 제한이 없다.
# 그러므로 전달된 아규먼트의 타입을 채크하여 숫자만 처리하고 숫자가 아닌 데이터는 무시한다.
# 아규먼트가 전달되지 않았거나 전달되었다 하더라도 숫자가 없으면 None 을 리턴한다.

def sumAll(*n):
    Asum = 0
    count = 0
    for i in n:
        if type(i) == int:
            Asum += i
            count += 1
    if len(n) == 0 or count == 0:
        Asum = None
    return Asum

print(sumAll(3,"h,f",5))
print(sumAll())