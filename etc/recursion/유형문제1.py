# 팩토리얼 구현

# 일반
def factorial_interative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)
# 코드가 더 간결하고 직관적이다.


print("반복", factorial_interative(5))
print("재귀", factorial_recursive(5))
