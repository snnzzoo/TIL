# https://www.acmicpc.net/problem/10988

import sys
sys.stdin = open('220727/10988_팰린드롬인지확인하기.txt')

word = str(input())
# str 안써도 가능
# print(word)
# print(word[::-1])

# if word == word[::-1]:
#     print(1)
# else:
#     print(0)

print(1 if word == word[::-1] else 0)