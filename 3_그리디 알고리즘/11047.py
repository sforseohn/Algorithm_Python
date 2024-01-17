# 동전 0
import sys
input = sys.stdin.readline

# 입력
n, k = map(int, input().split()) # 동전의 종류, 목표 가치

a_list = [0] * n
for i in range(n):
    a_list[i] = int(input()) # 동전의 가치

# 연산
# 각 동전의 가치는 더 작은 동전의 배수임! -> 그리디 접근 가능
a_list.sort(reverse=True)
cnt = 0
for a in a_list:
    if k == 0:
        break
    
    cnt += k // a # 동전의 개수 갱신
    k %= a        # 남은 값 갱신

# 출력
print(cnt)