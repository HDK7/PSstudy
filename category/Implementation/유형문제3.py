# 8 x 8 좌표 평면에서 나이트 처럼
# 수평 두칸 이동후 수직 한칸 혹은
# 수직 두칸 이동후 수평 한칸 으로만 이동이 가능하다.
# 8 x 8 좌표 평면에서 나이트가 이동할 수 있는 경우의 수 출력
# 행은 1~8 열은 a~h
# ex) c2에 있을 때 이동할 수 있는 경우의 수 6가지
# 입력 a1
# 출력 2

# 내 풀이
str = input()
y = int(str[1])
dir2 = {'a' : 1, 'b' :2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8 }

x = dir2[str[0]]
dir = [[2,1], [2, -1],[-2,1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
count = 0

for i,j in dir:
    if( 1 <= x + i and x + i <= 8 and  1 <= y + j and y + j <= 8 ):
        count += 1

print(count)

# 아래는 나동빈님풀이
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(2,1), (2, -1),(-2,1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >=1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        result += 1

print(result)