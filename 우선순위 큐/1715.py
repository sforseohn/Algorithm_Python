import heapq, sys
input = sys.stdin.readline

# 입력
n = int(input())
h = []
for _ in range(n) :
    heapq.heappush(h, int(input()))

sum = 0    
while len(h) > 1:
    add = heapq.heappop(h) + heapq.heappop(h)
    heapq.heappush(h, add)
    sum += add

# 출력 
print(sum)