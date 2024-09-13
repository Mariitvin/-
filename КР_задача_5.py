import math

def good_squares(n):
    i = 1
    squares = []
    while i * i <= n:
        squares.append(i * i)
        i += 1
    return squares

n = int(input())
squares = good_squares(n)
print(" ".join(map(str, squares)))

