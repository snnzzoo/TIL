## 아래 코드는 숫자의 길이를 구하는 코드입니다.
## 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# number = 22020718
# print(len(number))

## TypeError: object of type 'int' has no len()
## len()은 문자열만 인식하기 때문에 str으로 바꿔준다.

number = str(22020718)
print(len(number))

number = 22020718
print(len(str(number)))
