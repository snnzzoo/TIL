# 주어진 문자열 word가 주어질 때, 해당 단어에서 'a'를 모두 제거한 결과

word = 'apple'
# 반복! for
for char in 'apple':
    # 만약 'a'일 때
    if char == 'a':
        # 반복문에서 아무것도 안하고 넘어가는?
        # continues
        print('안녕?')

for char in 'apple':
    # 만약 'a'가 아닐 때
    if char != 'a':
        print(char)

for char in 'apple':
    # 만약 'a'가 아닐 때
    if char != 'a':
        result = result + char
print(result)
