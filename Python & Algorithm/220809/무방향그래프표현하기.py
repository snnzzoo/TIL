# https://www.notion.so/hphk-edu/22-bb38e88c331a46628d5c6ee33ddcd50c

import sys
sys.stdin = open('무방향그래프표현하기.txt')

# 인접 행렬로 표현
N, M = map(int, input().split()) # 정점의 개수, 간선의 개수

graph = [[0] * N for _ in range(N)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

print(graph)

# 인접 리스트로 표현
N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(graph)
