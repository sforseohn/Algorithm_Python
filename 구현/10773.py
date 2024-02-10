# 제로
import sys
input = sys.stdin.readline

# 입력 & 연산
k = int(input())
stack = []

for _ in range(k):
    n = int(input())
    
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
        
# 출력
ans = sum(stack)
print(ans)