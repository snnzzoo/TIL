import sys
sys.stdin = open("220720/SWEA 문제풀이/2019_input.txt", "r")

N = int(input())
result = 0

for i in range(0, N + 1):
    result = 2**i
    print(result, end=' ')
