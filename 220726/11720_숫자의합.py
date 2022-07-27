# https://www.acmicpc.net/problem/11720

import sys
sys.stdin = open('220726/11720.txt')

T = int(input())
numbers = list(map(int, input()))
print(sum(numbers))
