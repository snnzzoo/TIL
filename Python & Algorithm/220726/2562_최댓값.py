# https://www.acmicpc.net/problem/2562

import sys
sys.stdin = open('220726/2562_최댓값.txt')

# numbers = []
# for n in range(9):
    # numbers.append(int(input()))

numbers = [int(input()) for n in range(9)]
# print(numbers)
print(max(numbers))
print(numbers.index(max(numbers)) + 1)
