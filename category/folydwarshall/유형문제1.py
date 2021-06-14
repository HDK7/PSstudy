# 1~N 번 회사가 있다.
# 방문 판매원 A는 1번 회사에 있고 X 회사에 방문해 물건을 판매하고자 한다.
# 회사끼리 연결된 통로는 양방향이다.
# 통로가 있으면 무조건 1의 시간이 걸린다.
# A는 K번 회사에 소개팅도 참석 하고자 한다.
# A는 1번 회사를 출발하여 K번 회사를 방문한 뒤 X번 회사로 가는 것이 목표이다.
# 방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성 하시오.

# 회사의 개수 N, 경로의 개수 M // 1<=N,M<= 100
# 두 회사의 번호
# 마지막 X, K
# 최소이동시간출력, 불가능할시 -1
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# 3 (출력)

# 내 코드
N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF] * N for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
    graph[y - 1][x - 1] = 1

X, K = map(int, input().split())

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if (graph[0][K-1] + graph[K-1][X-1]) >= INF:
    print(-1)
else:
    print(graph[0][K-1] + graph[K-1][X-1])

# 나동빈님 코드
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 내가 빠뜨린 부분. 자기 자신에게 가는 최단거리는 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

