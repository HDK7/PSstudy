# x가 등장하는 횟수를 계산하시오
# 1, 1, 2, 2, 2, 2, 3
# x = 2 일경우 2 값의 개수 4 출력
# 단, O(logN) 알고리즘으로 설계하시오
# N 과 X 가 주어진다. 1 <= N <= 1,000,000 / -10^9 <= N개의 각원소값 <= 10^9
#ex)
# 7 2
# 1 1 2 2 2 2 3
# 4 (결과)

# 나동빈님 코드
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)