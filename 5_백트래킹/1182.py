
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def seek(i, num):
    global ans
    
    if i == n:
        return
    
    num += nums[i]
    
    if num == s:
        ans += 1
    
    seek(i + 1, num)
    
    # 반납
    seek(i + 1, num - nums[i])
        
# 입력
n, s = map(int, input().split()) # 정수의 개수, 정수
nums = list(map(int, input().split()))

# 연산
ans = 0
cal_nums = []
seek(0, 0)

# 출력
print(ans)

