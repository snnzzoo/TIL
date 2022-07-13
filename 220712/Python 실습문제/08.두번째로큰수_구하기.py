numbers = [-10, -100, -30]
max_number = float('-inf')
second_number = float('-inf')

# 1. 전체 숫자를 반복
for n in numbers:
    # 만약에, n이 최댓값보다 크다면
    if max_number < n:
        # 최댓값이었던 것이 두 번째로 큰 수가 됨
        second_number = max_number
        # 최댓값은 n이 됨
        max_number = n
    # elif second_number < n < max_number:
    elif second_number < n and n < max_number:
        second_number = n    
print(second_number)


numbers = [-10, -100, -30]
max_num = numbers[0]
second = numbers[0]

for i in numbers:
    if max_num < i:
        second = max_num
        max_num = i
    elif second < i and i < max_num:
        second = i
print(second)
