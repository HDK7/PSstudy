# (1,1) 에서 시작한다.
# N * N 크기 안에서 R(right) L(left) U(up) D(down) 을 따라 움직인다.
# 벽을 넘어가는 명령은 무시된다.
# 5
# R R R U D D
# 3 4 (정답)

n = int(input())
go = (input().split())
dir = {'R' : [0, 1], 'L' : [0, -1], 'U' : [-1, 0], 'D' : [1, 0]}

location = [1,1]
for i in go:
    dx, dy = dir[i][0], dir[i][1]
    if ( 1 <= location[0] + dx <= n):
        location[0] = location[0] + dx

    if ( 1 <= location[1] + dy <= n):
        location[1] = location[1] + dy

print(location[0], location[1])