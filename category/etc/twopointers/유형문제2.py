"""
구간 합 (Interval Sum) 빠르게 계산하기
연속으로 나열된 N개의 수가 있을 때 특정 구간의 모든 수를 합한 값을 계산하는 문제
{10, 20, 30, 40, 50} 에서 두번째부터 네 번째 수까지의 합 20 + 30 + 40 = 90

미리 계산된 합을 저장해 놓는다.
3~5번째 원소합은 (1~5번째 원소합) - (1~2번째 원소합)

시간 복잡도
N개의 정수로 구성된 수열, M개의 쿼리
O(N + M)
"""
n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])

