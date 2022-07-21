import sys
sys.stdin = open('220721/SWEA 문제풀이/1989_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):

    N = str(input())
    reverse_N = N[::-1]

    for i in N:
        # if N == reverse_N:
        #     result = 1
        # else:
        #     result = 0
        result = 1 if N == reverse_N else 0

    print(f'#{test_case} {result}')
