# https://www.acmicpc.net/problem/14425
# set을 사용해서 풀어보자
# set을 사용하면 연산 속도가 빠르다.

import sys
sys.stdin = open('14425_문자열집합.txt')

# S = [
#     'baekjoononlinejudge', 'startlink',
#     'codeplus', 'sundaycoding', 'codingsh'
# ]
# '''
# baekjoon
# codeplus
# codeminus
# startlink
# starlink
# sundaycoding
# codingsh
# codinghs
# sondaycoding
# startrink
# icerink
# '''

# words = [
#     'baekjoon', 'codeplus', 'codeminus', 'startlink', 'starlink',
#     'sundaycoding', 'codingsh', 'codinhs', 'sondaycoding', 'startrinkg', 'icerink'
# ]

# 풀이 1
input = sys.stdin.readline

N, M = map(int, input().split())

for i in range(N):
    S = set(input())
# word_set = set(S)
cnt = 0

for _ in range(M):
    words = input()
    if words in S:
        cnt += 1
print(cnt)


# 풀이 2
print(len(set(words) & set(S)))
# & : 교집합