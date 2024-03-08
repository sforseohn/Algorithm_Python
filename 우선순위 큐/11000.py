import heapq, sys
input = sys.stdin.readline

n = int(input())
lec = []
for i in range(n):
    s, t = map(int, input().split())
    lec.append((s, t))

lec.sort()
room = [0]
for s, t in lec:
    if room[0] <= s:
        heapq.heappushpop(room, t)
    else:
        heapq.heappush(room, t)
        
print(len(room))
    


