# 프린터 큐
import sys, collections
input = sys.stdin.readline

def solution(n, m, numbers):
    queue = collections.deque(numbers)
    cnt = 0
    numbers.sort()
    
    while True:
        if queue[0] == numbers[-1]:
            cnt += 1
            queue.popleft()
            numbers.pop()
            if m == 0:
                return cnt
        else:
            queue.append(queue.popleft())  
        m = len(queue) - 1 if m == 0 else m - 1
        
        
tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    print(solution(n, m, numbers))

    