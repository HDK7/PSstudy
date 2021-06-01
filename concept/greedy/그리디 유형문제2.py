# N에서 1을 빼거나 가능하다면 N을 K로 나눈다
# 1이 될때까지 최수 횟수

# 1 <= N <= 100,000
# 2 <= K <= 100,000

# 최대한 많은 나누기를 수행하면 된다.

# 최적의 해가 되는가? 항상 K로 나누는것은 항상 1을 빼는 것보다 효과적이다.

n, k = map(int, input().split())

result = 0;

# Nlog(N) 복잡도
while True:
    #  n 이 k로 나눌수 있는 수까지 구하기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을 때 반복문 탈출
    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)
print(result)



