word = 'apple'

# 방법 1. for 문
result = ''
for char in word:
    # 뒤에서부터 더하기
    result = char + result
print(result)

# 방법 2. pythonic
print(word[::-1])

# 방법 3.
print(''.join(reversed(word)))

# 방법 4. index
# 익숙해질수록 나중에 알고리즘 코드 풀기 좋음!
word = 'apple'

for i in range(len(word)):
    #  print(i) 디버깅
    print(word[len(word)-i-1], end='')
    
