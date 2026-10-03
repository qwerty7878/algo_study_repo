# 문제: 1859 백만
# 링크: https://swexpertacademy.com/main/code/problem/problemList.do (번호 1859 검색)
# 날짜: 2026-09-29
#
# [접근] 어떻게 풀었는지 / 왜 이 방식인지

# 일반적으로 마지막이 가능 비싼 케이스라 역순으로 조회하며 최고 금액 - 현재가 차액으로 진행
# 만약 최고값이 이전보다 크면 최고값 변경

# [시간복잡도] O(?)

# 테스트케이스 반복과 배열 역순 순회 -> O(n^2)

# [메모] 막혔던 점, 배운 점

# 막혔던 점 - 역순 조회가 아닌 max로 값을 찾은 후 탐색하고 중간에 최대값인 경우 새 배열을 만드는 방식을 진행했더니 시간초과가 나왔다.

t = int(input())
for test in range(1, t + 1):

    n = int(input())
    arr = list(map(int, input().split()))

    max_price = arr[-1]
    total = 0

    for idx in range(n - 2, -1, -1):
        if arr[idx] > max_price:
            max_price = arr[idx]
        total += (max_price - arr[idx])
    print(f"#{test} {total}")