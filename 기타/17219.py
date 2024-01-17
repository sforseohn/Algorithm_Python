import sys
input = sys.stdin.readline

# 입력
# 저장된 사이트의 수, 비밀번호를 찾으려는 사이트의 수
n, m = map(int, input().split()) 

memo = dict()

for _ in range(n):
    site, pwd = input().split()
    memo[site] = pwd

# 출력
for _ in range(m):
    site = input().strip('\n')
    print(memo[site])
