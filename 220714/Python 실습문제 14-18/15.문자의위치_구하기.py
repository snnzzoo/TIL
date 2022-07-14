word = 'banana'

# 문자로 순회하는 것이 아니라
# index로 접근해서 쓰자!
# 원하는 숫자? 0, 1, 2, 3, 4, 5
# 얻는 방법은? range(len(word)) => range(6) => 0 ~ 5
for idx in range(len(word)):
    # print(idx, word[idx])
    # 'a'일 때
    if word[idx] == 'a':
        print(idx)
        break
# for 문을 다 돌았다는 뜻은
# 한 번도 break에 안 걸렸다.
# 즉, 'a'는 없었다.
else:
    print(-1)


# 메서드 사용
word = 'banana'

print(word.find('a'))
print(word.index('a'))

print(word.find('p')) # 없는 경우 -1 반환
print(word.index('p')) # 없는 경우 Error



