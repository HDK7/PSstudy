# 배열 A와 B.  원소는 모두 자연수
# A원소 한개와 B 원소한개를 K번 바꿔치기 가능
# 목표는 A의 모든 원소의 합이 최대

# 내 코드

N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

for i in range(K):
    for j in range(len(B)-1,-1, -1):
        if A[i] < B[j]:
            A[i], B[j] = B[j], A[i]
            break

print(sum(A))

# 나동빈님 코드

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))