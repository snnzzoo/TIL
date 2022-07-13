# 최댓값 구하기
numbers = [-10, -100, -30]
max_num = numbers[0] # 최댓값 설정시 값을 초기 ~~로 하기
# max_num = -1000000
# max_num = float("-inf")

# 1. 반복
for n in numbers:
    # print(n)
    # 2. 만약, max값이 n보다 작으면 바꾼다.
    if max_num < n:
        # print('왔냐?')
        max_num = n
print(max_num)


numbers = [-10, -100, -30]
max_num = numbers[0]

for i in numbers:
    if max_num < i:
        max_num = i
print(max_num)

