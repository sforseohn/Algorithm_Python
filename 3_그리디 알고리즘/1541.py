# 잃어버린 괄호
import sys
input = sys.stdin.readline

# 입력
# - 기준으로 분리
s = input().split('-')

# + 기준으로 분리 후 각 원소별로 합 구하기
for i in range(len(s)):
    s[i] = sum(list(map(int, s[i].split('+'))))

# 총합 구하기
ans = s[0]
for i in range(1,len(s)):
    ans -= s[i]

print(ans)
    
'''
s = input().strip()
n = ''
nums = []
op = []

# 숫자와 연산자 분리하여 각각 리스트에 저장
for i in range(len(s)):
    if s[i] == '-' or s[i] == '+':
        nums.append(int(n))
        n = ''
        op.append(s[i])
        
    else: # 숫자
        n += s[i]

nums.append(int(n))

# 연산
total = nums[0]
minus = False
for i in range(len(op)):
    if op[i] == '-':
        minus = True
        total -= nums[i+1]
    elif minus == True:
        total -= abs(nums[i+1])
    else:
        total += nums[i+1]
  
# 출력      
print(total)
'''