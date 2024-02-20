# 쇠막대기
import sys
input = sys.stdin.readline

# 입력
str = input().strip()

# 연산
steel = 0
ans = 0

for i in range(len(str)):
    if str[i] == '(':
        steel += 1   # 쇠막대기 추가 
    else:
        steel -= 1
        if str[i-1] == '(':  # 레이저 발견
            ans += steel     # 현재 쇠막대기 수만큼 조각 추가
        else:
            ans += 1

# 출력
print(ans)