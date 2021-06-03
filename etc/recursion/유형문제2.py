# 최대공약수 계산 (유클리드 호제법)
# A > B 에서 A를 B로 나눈 나머지 : R
# 이때 A와 B의 최대공약수는 B와 R의 최대 공약수와 같다.

# 재귀적 구현
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))
print(gcd(162, 192))