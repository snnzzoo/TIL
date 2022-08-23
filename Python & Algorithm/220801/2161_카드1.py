# https://www.acmicpc.net/problem/2161

import sys
sys.stdin = open('2161_카드1.txt')

# 큐 풀이
N = int(input())
queue = list(range(1, N + 1))

while len(queue) > 1:
    print(queue.pop(0), end=' ')
    queue.append(queue.pop(0))

print(queue[0])


# 덱 풀이 - 양방향 삽입, 추출이 모두 큐보다 훨씬 빠르다.
from collections import deque

N = int(input())
queue = deque(range(1, N + 1))

while len(queue) > 1:
    print(queue.popleft(), end=' ')
    queue.append(queue.popleft())

print(queue[0])

