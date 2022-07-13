## while문
i = 1
result = 0
n = 10

while i <= n:
    result += i
    i += 1
print(result)

while i < n:
    print(f'i: {i}, result: {result}')
    i += 1
    result += i
print(result)


# 값 초기화 (처음 시작 값)
n = 0
# 0부터 더하기 위해서
result = 0
# user_input 값
user_input = int(input())

# 방법 1
while n <= user_input:
    result += n
    n += 1
print(result)

# 방법 2
while n < user_input:
    print(f'n: {n}, result: {result}') # 그때마다의 결과 적어 놓으면 디버깅 시 편리함
    n += 1
    result += n
print(result)


## for문
result = 0
n = 10

for i in range(1, n+1):
    result += i
print(result)
