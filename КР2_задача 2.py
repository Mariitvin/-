N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
new_matrix = [[0] * N for _ in range(M)]
for i in range(N):
    for j in range(M):
        new_matrix[j][N - 1 - i] = matrix[i][j]
print(M, N)
for row_matrix in new_matrix:
    print(" ".join(map(str, row_matrix)))
