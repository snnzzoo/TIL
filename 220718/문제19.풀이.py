# 문제 19. 숫자의 길이 구하기
number = 123
# 123 = 100 + 20 + 3 = 1 x 100 + 2 x 10 + 3 x 1

# 1. 123
cnt = 0
# 몫이 0이 되면 종료해야하니까!
# int : 0이 아닌 다른 수면 무조건 True!
while number != 0:
    # number = number // 10
    number //= number
    cnt += 1

print(cnt)
