from pprint import pprint

edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 4],
    [2, 5],
    [4, 6]
]

# => flatten
# flatten_edges =[0, 1, 0, 2, 1, 3, 1, 4, 2, 4, 2, 5, 4, 6]
# print(*edges)

n = 7
m = 7

matrix =[
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0]
]

for edge in edges:
    # v1, v2 = map(int, input().split())
    v1, v2 = edge[0], edge[1]
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1

# n x n 행렬 초기화 [0으로 초기화]
matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1

pprint(matrix)