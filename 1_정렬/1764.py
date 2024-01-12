import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split()) # 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M

notHeard = set()
notSeen = set()
for i in range(n):
    notHeard.add(input().strip())
for j in range(m):
    notSeen.add(input().strip())

# 연산
both = list(notHeard & notSeen)
both.sort()

# 출력
print(len(both))
for i in range(len(both)):
    print(both[i])