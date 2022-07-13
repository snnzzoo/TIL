# 문자열 word의 길이를 출력하는 코드를 각각
# word = 'happy!'
# 6
word = 'happy!'
count = 0

# 모든 문자를 돌면서
for char in word:
# 1씩 증가시킨다.
    count = count + 1
print(count)


word = 'happy!'
count = 0

for char in word:
    count = count + 1
print(count)


word = 'happy!'
count = 0

for char in word:
    count += 1
print(count)
