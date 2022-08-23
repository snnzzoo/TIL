# https://www.acmicpc.net/problem/2798

import sys
sys.stdin = open('220808/2798_블랙잭.txt')

n, m = map(int, input().split())
cards = list(map(int, input().split()))

def blackjack(n, m, cards):
    max_total = 0 # 현재 가장 큰 합

    # 완전탐색(Brute-force)
    for i in range(n-2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                total = cards[i] + cards[j] + cards[k]
                # 3중 for문을 이용해 모든 경우의 수를 탐색
                # i, j, k는 세 장의 카드의 인덱스를 의미
                # 중복으로 뽑는 경우를 방지하기 위해 range 범위 설정

                # 현재 가장 큰 합보다는 크고, m을 넘지 않아야 갱신
                if max_total < total <= m:
                    max_total = total

                # 합과 m이 같으면 더이상 탐색하는 의미가 없으므로 종료
                if total == m:
                    return total

    return max_total

print(blackjack(n, m, cards))
