# 문제: 1204 최빈수
# 링크: https://swexpertacademy.com/main/code/problem/problemList.do (번호 1204 검색)
# 날짜: 2026-10-02
#
# [접근] 어떻게 풀었는지 / 왜 이 방식인지

# 파이썬 counter을 활용해 빈도수를 구할 수 있었다.
# most_common(1) 을 활용해 최고 1개 값만 추출할 수 있어 간편했다.

# [시간복잡도] O(?)

# 테스트 N개 + counter 조회 n회 -< O(n)

# [메모] 막혔던 점, 배운 점

# 막힌 부분은 없으나 most_common()의 값이 key, value 값이라 첫번쨰만 추출하기 위해서는 [0][0]을 사용해야한다.

from collections import Counter

t = int(input())
for test in range(1, t + 1):
    n = int(input())
    array = list(map(int, input().split()))

    count = Counter(array)
    for k,v in count.most_common(1):
        print(f'#{test} {k}')