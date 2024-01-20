# 문자열 반복
import sys
input = sys.stdin.readline

# 입력
t = int(input()) # 테스트 케이스의 수

for _ in range(t):
    r, s = input().split()
    r = int(r)

    # 연산
    ans = ''.join(c * r for c in s)

    # 출력
    print(ans)