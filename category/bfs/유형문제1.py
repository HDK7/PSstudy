# N x M 크기의 직사각형 미로
# 현재위치 (1,1)
# 한번에 한칸씩만 이동가능. 괴물이 있으면 0, 괴물이 없으면 1
# 동빈이가 탈출하기 위해 움직여야하는 최소 칸의 개수
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# 10 (출력)

# 나동빈님 코드
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n -1][m - 1]

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))


# 내코드

# result = 10e5
#
# row, col = map(int,input().split())
# data = []
#
# for _ in range(row):
#     data.append(list(map(int,input())))
#
# print(data)
#
# def bfs(x, y, c):
#     # 괴물이 있거나 범위 외
#     if x < 0 or y < 0 or x >= row or y >= col or data[x][y] == 0:
#         return
#
#     # 로직
#     global result
#
#     data[x][y] = 0
#
#     if x == row -1 and y == col -1:
#         result = min(result, c)
#         return
#
#     bfs(x -1, y, c + 1)
#     bfs(x +1, y, c + 1)
#     bfs(x, y -1, c + 1)
#     bfs(x, y +1, c + 1)
#     return
#
# bfs(0,0,1)
#
# print(result)




