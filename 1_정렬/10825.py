import sys
input = sys.stdin.readline()

# 입력
n = int(input())
student = []
for _ in range(n):
    student.append(input().split())

# 연산
student.sort(key = lambda k : (-int(k[1]), int(k[2]), -int(k[3]), k[0]))

# 출력
for s in student:
    sys.stdout.write(s[0] + '\n')