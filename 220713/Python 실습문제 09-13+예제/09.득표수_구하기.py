students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
name = input()
cnt = 0

for str in students:
    if name == str:
        cnt += 1
print(cnt)


students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
total = 0

for i in students:
    if i == '이영희':
        total += 1
print(total)
