# N x M 크기의 얼음틀 구멍은 0, 구멍이 없는부분은 1
# 연결되어 있는 그룹의 개수
# 입력
# 4 5  (세로, 가로)
# 00110
# 00011
# 11111
# 00000
# 출력
# 3


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x -1, y)
        dfs(x, y -1)
        dfs(x + 1, y)
        dfs(x, y+ 1)
        return True
    return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)


