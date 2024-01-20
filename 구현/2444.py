# 별 찍기 - 7
# 입력
n = int(input())

# 출력
for i in range(1, n):
    print(' ' * (n-i) + '*' * (i*2 - 1))

print('*' * (n * 2 - 1))

for i in range(1, n):
    print(' ' * (i) + '*' * (n*2 - i*2 - 1))
