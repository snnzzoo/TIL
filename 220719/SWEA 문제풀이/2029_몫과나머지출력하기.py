import sys
sys.stdin = open("220719/SWEA 문제풀이/2029_input.txt", "r")

t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'#{i} {a//b} {a%b}')
