# https://www.acmicpc.net/problem/10818

# max, min 함수
import sys
sys.stdin = open('220726/10818_최소최대.txt')

T = int(input())
N = list(map(int, input().split()))

print(min(N), max(N), end=' ')

# 오름차순으로 정렬
# 인덱스에서 첫 번째, 마지막 # list[0], list[-1]
N.sort()
print(N[0], N[-1])
