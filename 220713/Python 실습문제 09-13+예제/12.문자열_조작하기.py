# 주어진 문자열 word가 주어질 때, 해당 단어에서 'a'를 모두 제거한 결과

word = 'apple'

# 'a'가 있는 지 확인
for char in 'apple':
    if char == 'a':
        print('안녕?')

result = ''

for char in 'apple':
    # 만약 'a'가 아닐 때
    if char != 'a':
        result += char
print(result)

# 한 줄씩 출력
for char in 'apple':
    if char != 'a':
        print(char)