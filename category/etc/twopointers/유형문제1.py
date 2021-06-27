# N개의 자연수로 구성된 수열
# 합이 M인 부분 연속 수열의 개수
# O(N)

# 투포인터 호라용

"""
1. 시작점과 끝점이 둘다 첫번째 원소를 가리킨다.
이하 반복
2. 현재 부분합이 M과 같다면 카운트
3. 현재 부분 합이 M보다 작다면, end를 1 증가시킨다.
4. 현재 부분 합이 M보다 크거나 같다면, start를 1 증가시킨다.

시간복잡도 O(N)
"""

n = 5 # 데이터 개수
m = 5 # 부분합 M
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
