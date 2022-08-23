# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4364&sca=pyc0

import sys
sys.stdin = open('937_정올_이차원리스트순회연습.txt')

list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]
list_c = [[0] * 3 for _ in range(2)]

# 두 배열의 같은 위치끼리 곱하여 새로운 이차원 리스트에 저장
for i in range(2):
    for j in range(3):
        list_c[i][j] = list_a[i][j] * list_b[i][j]

# 결과 출력
for i in range(2):
    for j in range(3):
        print(list_c[i][j], end=' ')
    print()
