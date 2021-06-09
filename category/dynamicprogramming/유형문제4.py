# n x m 금광이 있다.
# 첫번째열 어느 행부터 출발할 수 있고
# 이후 m -1 번만 큼 오른쪽, 오른쪽 위, 오른쪽 아래 중 1곳으로 움직일 수 있다.
# 얻을 수 있는 최대 금 크기
# ex)
# 1
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 출력 19

# 내 코드
T = int(input())

for i in range(T):
    n, m = list(map(int,input().split()))
    data = []
    data2 = list(map(int,input().split()))
    for j in range(n):
        data3 = []
        for k in range(m):
            data3.append(data2[j * m + k])
        data.append(data3)

    print(data)

    for j in range(1, m):
        for k in range(n):
            if k == 0:
                data[k][j] = max(data[k][j-1], data[k+1][j-1]) + data[k][j]
                continue

            if k == n-1 :
                data[k][j] = max(data[k][j-1], data[k-1][j-1]) + data[k][j]
                continue
            data[k][j] = max(data[k-1][j-1], data[k][j-1], data[k+1][j-1]) + data[k][j]
        print(data)

    result = 0
    for j in range(n):
        result = max(data[j][m - 1], result)

    print(result)

# 나동빈님 코드
# 점화식
# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    for j in range(1,m):
        for i in range(n):
            if i == 0: left_up = 0
            else: left_up = dp[i - 1][j - 1]
            if i == n - 1: left_down = 0
            else: left_down = dp[i + 1][j - 1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)