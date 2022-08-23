# https://www.acmicpc.net/problem/9610

import sys
sys.stdin = open('9610_사분면.txt')

N = int(input())
cnt_Q1 = 0
cnt_Q2 = 0
cnt_Q3 = 0
cnt_Q4 = 0
AXIS = 0

for n in range(N):
    x, y = map(int, input().split())

    if x > 0 and y > 0: # 1분면: x 양, y 양
        cnt_Q1 += 1
    elif x < 0 and y > 0: # 2분면: x 음, y 양
        cnt_Q2 += 1
    elif x < 0 and y < 0: # 3분면: x 음, y 음
        cnt_Q3 += 1
    elif x > 0 and y < 0: # 4분면: x 양, y 음
        cnt_Q4 += 1
    elif x == 0 or y == 0: # 축: x or y 중 하나라도 0
        AXIS += 1

# print(f'Q1: {cnt_Q1}')
# print(f'Q2: {cnt_Q2}')
# print(f'Q3: {cnt_Q3}')
# print(f'Q4: {cnt_Q4}')
# print(f'AXIS: {AXIS}')

print('Q1:', cnt_Q1)
print('Q2:', cnt_Q2)
print('Q3:', cnt_Q3)
print('Q4:', cnt_Q4)
print('AXIS:', AXIS)