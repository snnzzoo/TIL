# a, e, i, o, u

# 방법 1
word = 'apple'
cnt = 0

for char in word:
    # 각각 비교해야 한다!
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        cnt += 1
print(cnt)

# 방법 2
word = 'apple'
cnt = 0

for char in word:
    # ['a', 'e', 'i', 'o', 'u']
    if char in 'aeiou':
        cnt += 1
print(cnt)


# 방법 3. if - elif 노가다
word = 'apple'
cnt = 0

for char in word:
    if char == 'a':
        cnt += 1
    elif char == 'e':
        cnt += 1
    elif char == 'i':
        cnt += 1
    elif char == 'o':
        cnt += 1
    elif char == 'u':
        cnt += 1   
print(cnt)
