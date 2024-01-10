# 최대 힙: 최소 힙에 -값을 붙여 삽입
import heapq, sys
input = sys.stdin.readline

# 입력
n = int(input()) # 연산의 개수
h = []
for _ in range(n) :
    x = int(input())
    
    if x == 0:
        if len(h) > 0:
            print(-heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, -x)
