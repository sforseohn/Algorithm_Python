import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

cards = deque([i for i in range(1, n+1)])

while(len(cards) > 2):
    cards.popleft()
    cards.append(cards.popleft())
    
print(cards[-1])