from pprint import pprint

# for _ in range(n):
#     matrix.append([0] * m)

# n x m
# n : 행의 개수
# m : 열의 개수
n = 5
m = 5

matrix1 = [[0] * m for _ in range(n)]
matrix1[0][0] = 1

print(matrix1)
pprint(matrix1)

matrix2 = [[0] * m]
pprint(matrix2)
# [[0, 0, 0, 0, 0]]

matrix3 = [[0] * m] * n
matrix3[0][0] = 1
pprint(matrix3)
# matrix1과 생긴 건 똑같지만 주소값이 다르다!