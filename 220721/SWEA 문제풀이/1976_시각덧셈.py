import sys
sys.stdin = open('220721/SWEA 문제풀이/1976_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):

    A, B, C, D = map(int, input().split())
    # print(A, B, C, D)

    # 시간 덧셈
    # 12시간제로 표현
    # hour = A + C
    # 13이상일 때 -> 12로 나눴을 때 나머지
    # if hour > 12:
    # hour = hour % 12
    hour = A + C if (A + C) <= 12 else (A + C) % 12
    # print(hour)

    # 분 덧셈
    if B + D < 60:
        min = B + D
    else:
        min = (B + D) - 60
        hour += 1
    # print(min)
    
    print(f'#{test_case} {hour} {min}')
