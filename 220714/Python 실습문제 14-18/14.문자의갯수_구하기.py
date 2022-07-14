# 'apple', 'a' 카운트

word = 'apple'

# chr는 이름 붙이기
# word의 요소를 하나씩 char 바인딩
cnt = 0
for char in word:
    if char == 'a':
        cnt += 1
print(cnt)

