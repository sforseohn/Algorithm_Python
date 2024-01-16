# 뒤집기
import sys
input = sys.stdin.readline

def reverse(i): # 문자가 0이면 1로, 1이면 0으로 뒤집기
    global cnt, s
    if s[i]:
        s[i] = 0
    else:
        s[i] = 1

# 입력
s = list(map(int, input().strip()))
cnt = 0

# 연산
# 문자열을 순회하며 같은 문자면 continue
# 다른 문자면 그 문자 뒤집기
# keep going
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        continue
    
    cnt += 1
    n = i
    while n < len(s):
        if s[i-1] == s[n]:
            break   
        reverse(n)
        n += 1
        
                
# 출력
print(cnt)


