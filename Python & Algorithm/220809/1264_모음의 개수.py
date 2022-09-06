# https://www.acmicpc.net/problem/1264

import sys
sys.stdin = open('1264_모음의 개수.txt')

while True:
    data = input()
    cnt = 0
    if data == '#': # 입력의 끝, 반복문 종료
        break
    for _ in data:
        if _ in 'aeiouAEIOU': # 모음이면
            cnt += 1
    
    print(cnt)
