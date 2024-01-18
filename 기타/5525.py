# IOIOI
import sys, re
input = sys.stdin.readline

# 입력
n = int(input())     # p의 종류
m = int(input())     # s의 길이
s = input().strip()
p = 'IOI'

# 연산
cnt = 0              # 이어진 'IOI' 의 수                 
ans = 0              # 문자열이 출현한 횟수
i = 0
while i < m - 1:
    if s[i:i+len(p)] == p:
        cnt += 1
        i += 2       # 다음 'IOI' 찾기
    else:
        cnt = 0
        i += 1
    
    if cnt == n:     # 목표 p 발견
        ans += 1
        cnt -= 1     # 다음 탐색을 위해 cnt - 1

# 출력
print(ans)

'''for i in range(repeat_num):
    if s[i] != p[0]:
        continue 
    
    new_str = s[i:i+len_p] # p의 길이만큼 s의 부분 문자열 만들기
    
    if p == new_str:       # p와 부분 문자열이 동일하면
        cnt += 1           # 카운트 증가

# 출력
print(cnt)'''