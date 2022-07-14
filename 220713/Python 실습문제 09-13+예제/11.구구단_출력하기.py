## f-string을 사용하지 않는 경우
# 단 설정하기 (2 이상 10 미만)
for dan in range(2, 10):
    # 현재 몇 단인지 매 단마다 출력
    print(dan, '단', sep='')
    # 각 단마다 곱하는 숫자 설정 (1이상, 10미만)
    for i in range(1, 10):
        print(dan, ' x ', i, ' = ', dan * i, sep='')


## f-string을 사용하는 경우
for dan in range (2, 10):
    # ''나 "" 앞에 f를 붙여 f-string을 사용하면, {}안에 변수를 입력할 수 있다.
    print(f'{dan}단')
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')
