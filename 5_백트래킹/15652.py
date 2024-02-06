# N과 M (4)
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def backtrack(i, nums):
    global ans
    
    if i == m:
        ans += nums
        return
    
    ori_nums = nums
    nums.append(num[i])
    
    backtrack(i + 1, nums)
    
    backtrack(i + 1, ori_nums)


# 입력
n, m = map(int, input().split())
num = [i for i in range(1, n+1)]
# 연산
ans = []
backtrack(0, [])

# 출력
for nums in ans:
    print(nums)

