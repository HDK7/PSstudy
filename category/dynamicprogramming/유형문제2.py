# 2, 3, 5 중 한개로 나누어 떨어지면 나눌 수 있다.
# 또는 1을 뺀다
# 최소 횟수로 숫자를 1로 만들려고 한다.
# 1 <= X <= 30000
# ex)
# 26          26 25 5 1
# 3

X = int(input())
list = [0] * (X + 1) * 5

for i in range(1, X + 1):

    if list[i+1] != 0:
        list[i+1] = min(list[i+1], list[i]+1)
    else:
        list[i+1] = list[i] + 1
    if list[i*2] != 0:
        list[i*2] = min(list[i*2], list[i]+1)
    else:
        list[i*2] = list[i] + 1
    if list[i*3] != 0:
        list[i*3] = min(list[i*3], list[i]+1)
    else:
        list[i*3] = list[i] + 1
    if list[i*5] != 0:
        list[i*5] = min(list[i*5], list[i]+1)
    else:
        list[i*5] = list[i] + 1

print(list[X])

# 나동빈님 코드
# a(i) = min(a(i-1), a(i/2), a(i/3), a(i/5)) + 1
x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[X])


