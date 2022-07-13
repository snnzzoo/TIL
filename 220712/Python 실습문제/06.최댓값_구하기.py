# 최댓값 구하기
numbers = [0, 20, 100]
max_num = numbers[0] # 통 안의 숫자 활용하기
# 최솟값 설정
# max_num = 0
# max_num = -1000000
# max_num = float("-inf") # 음의 무한대

# 1. 반복
for n in numbers:
    # print(n)
    # 2. 만약, max값이 n보다 작으면 n으로 값을 바꾼다.
    if max_num < n:
        # print('왔냐?')
        max_num = n
print(max_num)


numbers = [-10, -100, -30]
max_num = float('-inf')

for i in numbers:
    print(i)
    if max_num < i:
        max_num = i
print(max_num)

