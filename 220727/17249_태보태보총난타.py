# https://www.acmicpc.net/problem/17249

import sys
sys.stdin = open('220727/17249_태보태보총난타.txt')

# 나의 방법
# 인풋 받고 리스트로 왼쪽, 오른쪽 나누기
taebo = input()
taebo_split = taebo.split('(^0^)')

# 왼쪽, 오른쪽에 각각 
taebo_left = taebo_split[0]
taebo_right = taebo_split[1]
# print(taebo_right)
# print(taebo_left)
print(taebo_left.count('@'), taebo_right.count('@'))

# 구글 헬프
# l, r = input().split('(^0^)')
# print(l.count('@'), r.count('@'))
