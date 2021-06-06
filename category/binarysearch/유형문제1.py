# 떡의 길이가 모두 다르다.
# 떡은 H값으로 고정적으로 잘린다.
# H가 15일 때 15, 14, 10, 17 은 15, 14, 10, 15가 된다.
# 즉 짤린 겂은 4, 0, 0, 2
# 손님은 6cm를 가져간다
# 손님이 Mcm 를 가져가기 위해 설정할 수 있은 최대 H 값
# 예시
# 4 6
# 19 15 10 17
# 15 (출력)
# 떡의 개수는 1,000,000 이하 M은 2000,000,000 이하

# TIP) 탐색범위가 크면 이진탐색을 떠올리는게 좋다

# 내코드
# mid -1, mid + 1 처럼 한칸 넓어지는게 포인트인것 같다.

N, M = map(int,input().split())
list = list(map(int, input().split()))
result = 0

def findH(start, end):
    global result
    print(start, end, M, N)
    if(start == end):
        return

    mid = (start + end) // 2

    sum = 0
    for i in list:
        if i < mid:
            continue
        else:
            sum += i - mid

    if(sum >= M):
        result = mid
        findH(mid + 1, end)
    else:
        findH(start, mid - 1)

findH(0, max(list))
print(result)


# 나동빈님 코드

# n, m = list(map(int, input().split()))
# array = list(map(int, input().split()))
#
# start = 0
# end = max(array)
#
# result = 0
# while(start <= end):
#     total = 0
#     mid = (start + end) //2
#     for x in array:
#         if x > mid:
#             total += x - mid
#
#     if total < m :
#         end = mid -1
#     else:
#         result = mid
#         start = mid + 1
#
# print(result)
