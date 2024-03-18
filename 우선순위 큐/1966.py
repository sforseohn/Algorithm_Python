# 프린터 큐
import sys,collections
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    q = collections.deque(list(map(int, input().split())))
    
    cnt = 0
    
    while q:
        big = max(q)
        val = q.popleft()
        m = (m - 1) 
        
        if val < big:
            q.append(val)
            if m < 0:
                m = len(q) - 1
        else:
            cnt += 1
            if m < 0:
                break
    
    print(cnt)
        