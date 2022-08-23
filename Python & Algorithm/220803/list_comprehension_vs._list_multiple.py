n = 4 # 행
m = 3 # 열

matrix1 = [[0] * m for _ in range(n)] # 리스트 컴프리헨션
matrix2 = [[0] * m] * n # 리스트 곱셈 연산

matrix1[0][0] = 1
matrix2[0][0] = 1

print(matrix1)
print(matrix2)