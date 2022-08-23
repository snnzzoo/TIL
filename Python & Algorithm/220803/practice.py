'''
3 x 3 입력 받기

1 2 3
4 5 6
7 8 9
'''

from pprint import pprint

matrix = []

for _ in range(3):
    line = list(map(int, input().split()))
    matrix.append(line)

pprint(matrix)


matrix.append([list(map(int, input().split()))] for _ in range(3))
pprint(matrix)