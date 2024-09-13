import math
def sum_fac(n):
    end_sum = sum(1 / math.factorial(i) for i in range(n + 1))
    return end_sum

n = int(input('Введите число n'))
result = sum_fac(n)
print(f"{result:.5f}")
