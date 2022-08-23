from pprint import pprint

n , m = map(int, input().split())  # 8 7
matrix = []

for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)


matrix = [list(map(int, input().split())) for _ in range(n)]

