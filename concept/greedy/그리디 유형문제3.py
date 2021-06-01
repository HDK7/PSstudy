# 숫자 문자열에서 숫자 사이마다 곱하기 또는 더하기를 사용하여 가장 큰 수를 구하라
# 연산은 왼쪽부터 순서대로 이루어진다

# 0, 1 이면 더하고 아니면 곱한다.

data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)