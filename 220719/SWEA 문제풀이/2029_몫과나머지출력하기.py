import sys

<<<<<<< HEAD
sys.stdin = open("220719/SWEA 문제풀이/input_2029.txt", "r")
=======
sys.stdin = open("SWEA 문제풀이/input_2029.txt", "r")
>>>>>>> aa84d6f97ac5eca7207ca6a9f844f4e7f009a8d7

t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'#{i} {a//b} {a%b}')
