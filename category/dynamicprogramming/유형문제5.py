# N명의 병사가 무작위로 나열 되어있다.
# 전투력을 기준으로 내림차순으로 배치하고자 한다.
# 배치를 위해 병사를 병사를 열외시키는데 최소한의 열외를 통해 내림차순이 되는 열외 병사 수
# ex)
# 7     1<=N<=2000
# 15 11 4 8 5 2 4           전투력 < 10,000,000
# 2 (결과)

# 내코드 없음 - 못품

# 나동빈님 코드
# D[i] = array[i] 를 마지막 원소로 가지는 부분 수열의 최대 길이
# LIS
# 모든 O <= j < i 에 대하여, D[i] = max(D[i], D[j]+1) if array[j] < array[i]
# 이전 배열에서 자기보다 작은 숫자들의 각각 최대길이의증가배열 값 중 최댓값
# 최악의 경우 O(N^2)
n = int(input())
array = list(map(int, input().split()))
array.reverse() # 증가하는 수열 문제로 바꾼다.

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))