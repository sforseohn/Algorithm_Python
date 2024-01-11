import sys
input = sys.stdin.readline

# 입력
n = int(input())
dots = []
for i in range(n):
    dots.append(list(map(int, input().split())))

# 연산
dots.sort(key = lambda k : (k[0], k[1]))

# 출력
for i in range(n):
    print(dots[i][0], dots[i][1])
