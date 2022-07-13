# 1. 문제 제공
numbers = [3, 10, 20]

# 2. 값 초기화
result = 0
count = 0

# 3. 반복
for number in numbers:
    result = result + number
    # result += number
    count = count + 1
    # count += 1

print(result/count)
# print(sum(numbers)/len(numbers))


numbers = [3, 10, 20]

result = 0
count = 0

for i in numbers:
    result += i
    count += 1
print(result/count)

# 더해서 갯수만큼 나눈다


