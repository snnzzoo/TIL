## 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
## 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# words = list(map(int, input().split()))
# print(words)

## ValueError: invalid literal for int() with base 10: "I'm"
## map(int)때문에 str을 받지 못함

words = list(input().split())
print(words)
