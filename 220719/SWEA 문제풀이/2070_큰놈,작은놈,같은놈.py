import sys
<<<<<<< HEAD
sys.stdin = open('220719/SWEA 문제풀이/input_2070.txt', 'r')
=======
sys.stdin = open('SWEA 문제풀이/input_2070.txt', 'r')
>>>>>>> aa84d6f97ac5eca7207ca6a9f844f4e7f009a8d7

T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    if a < b:
        print(f'#{test_case} <')
    elif a > b:
        print(f'#{test_case} >')
    else:
        print(f'#{test_case} =')
