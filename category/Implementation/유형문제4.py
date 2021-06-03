# 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열.
# 모든 알파벳을 오름차순으로 정렬 후 모든 숫자를 더한 값을 이어서 출력
# 예를 들어 K1KA5CB7 은 ABCKK13 출력

data = input()
sum = 0
result = []

for i in data:
    if 0 <= (int(ord(i))-int(ord('0'))) and (int(ord(i))-int(ord('0')))  <= 9:
        sum += int(i)
        continue
    result.append(i)

print(''.join(sorted(result)) + str(sum))

# sum = 0일 때 제외를 안해줘서 틀렸다.


# 나동빈님 코드

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))