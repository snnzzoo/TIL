import heapq

numbers = [5, 3, 2, 4, 1]

heapq.heapify(numbers)
# 앞에 가장 작은 갚이 오도록 (뒤는 굳이 오름차순 아님. 완전정렬 x)
# print(numbers)
heapq.heappop(numbers)
print(numbers)

