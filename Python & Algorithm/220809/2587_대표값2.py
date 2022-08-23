# https://www.acmicpc.net/problem/2587

import sys
sys.stdin = open('2587_대표값2.txt')

# 평균
# 중앙값
numbers = []

for _ in range(5):
    numbers.append(int(input()))
# print(numbers)
    numbers.sort()
# print(numbers)

print(sum(numbers) // 5)
print(numbers[2])
