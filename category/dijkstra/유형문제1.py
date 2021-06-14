# N개의 도시가 있다.
# 단방향으로만 다른도시로 메세지를 보낼 수 있다.
# 도시 C에서 최대한 많은 도시로 메세지를 보내고자 한다.
# C에서 보낸 메세지를 받게 되는 도시의 개수와, 도시들이 모두 베세지를 받는데까지 걸리는 시간

# 도시 개수 N, 통로 개수 M, 메세지를 보내는 도시 C
# 1<=N<=30,000, 1<=M<=200,000  , 1<=C<=N

# 둘째 줄 부터 M + 1 번재 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다.
# X에서 Y로 이어지는 통로, 메세지가 전달되는 시간 Z
# 1 <= X, Y <= N, 1 <= Z <= 1,000

# 첫째 줄에 도시 C에서 보낸 메세지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력

#ex)
# 3 2 1
# 1 2 4
# 1 3 2
# 출력
# 2 4

# 도시 개수, 통로 개수, 메세지를 시작 도시

# 내코드
import heapq

# N, M, C = map(int, input().split())
# INF = int(1e9)
# graph = [[INF] * N for _ in range(N)]
# result = int(1e9)
#
# # 입력
# for _ in range(M):
#     begin, end, time = map(int, input().split())
#     graph[begin - 1][end - 1] = time
#
#
# def dijkstra(start):
#     queue = []
#     heapq.heappush(queue, (0, start))
#     while queue:
#         cityTime, city = heapq.heappop(queue)
#
#         # print(cityTime, city)
#         # print(len(graph[city]))
#         for i in range(len(graph[city])):
#             aroundCity = i
#             aroundCityTime = graph[start][aroundCity]
#             TimeFromCityToAroundCity = graph[city][aroundCity]
#             if aroundCityTime > cityTime + TimeFromCityToAroundCity:
#                 graph[start][aroundCity] = cityTime + TimeFromCityToAroundCity
#                 heapq.heappush(queue, (cityTime + TimeFromCityToAroundCity, aroundCity))
#
# dijkstra(C)
#
# result = 0
# cnt = 0
# for i in graph:
#     for j in i:
#         if j != INF:
#             cnt += 1
#             result = max(result, j)
#
# print(cnt, result)


# 나동빈님 코드
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
count = 0
max_distance = 0
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)


dijkstra(start)






# def dijkstra(start):
#     q = []
#
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:








