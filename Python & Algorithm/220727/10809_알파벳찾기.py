# https://www.acmicpc.net/problem/10809

import sys
sys.stdin = open('220727/10809_알파벳찾기.txt')

word = input()
alphabet = [chr(i) for i in range(97, 123)]
# alphabet = 'abcdefghijklmnopqrstuvwxyz'

for a in alphabet:
    print(word.find(a), end=' ')

# .find(a) : a 없으면 -1 반환
# .index(a) : a 없으면 Error





