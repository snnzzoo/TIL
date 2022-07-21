import sys
sys.stdin = open('220721/SWEA 문제풀이/1288_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    
    N = int(input())
    
    for i in range(1, N + 1):
        i *= 2
        print(i, end=' ')
    


    # print(f'#{test_case} {i}')