import sys

sys.stdin = open("220719/SWEA 문제풀이/input_2029.txt", "r")

t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'#{i} {a//b} {a%b}')
