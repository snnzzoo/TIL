# https://www.acmicpc.net/problem/2750

import sys
sys.stdin = open('220726/2750_수정렬하기.txt')

T = int(input())
numbers = []
# numbers 리스트에 숫자 넣기
for t in range(T):
    numbers.append(int(input()))
# print(numbers)
numbers.sort()
for i in range(len(numbers)):
    print(numbers[i])
