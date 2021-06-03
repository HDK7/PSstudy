#00시 00분 00초~ N시 59분 59초의 시각중에 3이 하나라도 포함되는 모든 경우의 수
#ex
# 5 입력
# 11475 출력

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
