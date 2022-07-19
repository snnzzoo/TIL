import sys
sys.stdin = open('SWEA 문제풀이/input_2071.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    sum = 0
    my_list = list(map(int, input().split()))
    for i in my_list:
        sum += i
    print(f'#{test_case} {round(sum/len(my_list))}')