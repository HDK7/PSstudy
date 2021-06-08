# N가지 종류의 화폐가 있다.
# 최소한의 개수로 M원이 되도록 한다
# 예를 들어 2, 3원 이있을 때 15원을 만들려면 3원을 5개 사용하는 것이 최소한의 화폐 개수이다.
# 불가능할 경우 -1
# ex) 2개 화폐로 15를 만든다. 화폐는 2, 3 원이 있다.
# 2 15 1 <= N <=100, 1<=M<=10000
# 2
# 3
# 5 (결과)

N, M = list(map(int,input().split()))
coin = []
list = [-1] * (M + 1)
for i in range(N):
    n = int(input())
    coin.append(n)
    if(n < M + 1):
        list[n] = 1;

for i in range(1, M+1):
    for j in coin:
        if (i - j) < 0 or list[i-j] == -1:
            continue
        if list[i] == -1:
            list[i] = list[i-j]+1
        else:
            list[i] = min(list[i], list[i-j]+1)

if(M == 1):
    print(1)
elif(list[M] == 0):
    print(-1)
else:
    print(list[M])

# 나동빈님 코드
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j -array[i]] != 10001:
            d[j] = min(d[j], d[j -array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])