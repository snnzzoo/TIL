import sys
sys.stdin = open('220721/SWEA 문제풀이/1926_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):

# 3, 6, 9를 문자열로 보기!
    N = int(input())
    clap = [3, 6, 9]
    result = 0

    for i in range(1, N + 1):
        # 3, 6, 9가 포함되었으면 박수
        # 3, 6, 9가 포함된 횟수만큼 박수
        if i in list(clap):
            result = '-'
            print(result, end=' ')
        # 3, 6, 9가 없으면 숫자 그대로
        else:
            result = i
            print(result, end=' ')
        
    # print(f'#{test_case} {result}')
