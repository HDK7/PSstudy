# 창고가 일렬로 있고, 약탈하여 식량을 뺏을 예정이다.
# 최소한 한 칸 이상 떨어진 식량 창고를 약탈한다.
# ex)
# 1 3 1 5
# {1,1} or {3, 5} 등이 가능하다. 얻을 수 있는 식량의 최댓값은 위의 경우 8이다
# 예시
# 4            3 <= N <= 100
# 1 3 1 5      0 <= K <= 1000
# 8 (결과)

# 내 코드
N = int(input())
list = list(map(int,input().split()))
maxNumber = [0] * N
result = list[0]
n1, n2 = list[0], max(list[0], list[1])

for i in range(2, N):
    result = max(n1 + list[i], n2)
    n1 = n2
    n2 = result

print(result)

# 나동빈님 코드
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i -1], d[i -2] + array[i])

print(d[n-1])


