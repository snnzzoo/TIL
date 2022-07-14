# 방법1. for


word = 'apple'
result = ''
for char in word:
    result = char + result
print(result)

# 방법2. pythonic
print(word[::-1])

# 방법3
print(''.join(reversed(word)))

# 방법4. index
word = 'apple'

for i in range(len(word)):
    print(i)
    print(word[len(word)-i-1], end='')


# sep
# 여러 개를 동시에 출력할 때 사이에 구분값

# end (기본값 : '\n')
# print 출력이 된 이후 뒤에 뭐를 붙일 지!
print(1, end='수업끝~')
print(2, end='끝~')
print(3)

print(1, end='\n')
print(2)
print(3)