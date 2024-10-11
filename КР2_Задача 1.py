n, m = map(int, input().split())
A = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            A[i][j] = i * m + j
        else:
            A[i][j] = i * m + (m - 1 - j)

for row_num in A:
    print(" ".join(f"{num:2d}" for num in row_num))
