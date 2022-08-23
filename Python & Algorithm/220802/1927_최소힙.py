# https://www.acmicpc.net/problem/1927

import sys
sys.stdin = open('1927_최소힙.txt')

import heapq

heap = []
# heapq.heapify(heap)
N = int(sys.stdin.readline())
# numbers = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]

for _ in range(N):
    n = int(sys.stdin.readline())

    if n != 0:
        heapq.heappush(heap, n)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))


# input()으로 하니 백준에서 시간초과
# sys.stdin.readline()으로 