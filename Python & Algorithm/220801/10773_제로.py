input1 = [3, 0, 4, 0]
input2 = [1, 3, 5, 4, 0, 0, 7, 0, 0, 6]

# if 0이면 가장 최신값 삭제
# else 0이 아니면 계속 입력

# if 0이 아니면 stack에 append(push)
# else stack에 pop

stack = []

for elem in input2:
    if elem != 0:
        stack.append(elem)
    else:
        stack.pop(elem)



K = int(input())
input_list = []

for _ in range(K):
    input_list.append(int(input()))
# 바깥 input, output 핸들링은 빠르게 결정해서 풀 수 있기 때문에 문제 먼저 해결하고 나중에 설정하면 된다.



