# https://www.acmicpc.net/problem/1371

import sys
sys.stdin = open('1371_가장많은글자.txt')



# 실패

# # 문장을 끝까지 돌며 알파벳별 나온 횟수 리스트에 저장
# sentence = sys.stdin.read().split()
# print([''.join(sentence)])

# # 횟수가 가장 많은 문자 출력
# max_letter = max(set(sentence), key=sentence.count)
# print(max_letter)

# => 리스트에서 보이는 것만 붙어있지 사실은 각각의 원소이기에 각 문자의 개수를 세아릴 수 없었음

# data = [1, 3, 3, 6, 6, 9, 5, 6]
# max_num = max(set(data), key=data.count)
# print(max_num)

# print(string.ascii_lowercase)