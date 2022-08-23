# https://www.acmicpc.net/problem/10773

import sys
sys.stdin = open('10773_제로.txt')

K = int(input())
stack = []

for k in range(K):
    number = int(input())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)
print(sum(stack))
