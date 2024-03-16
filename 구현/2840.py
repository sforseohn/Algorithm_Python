import sys
input = sys.stdin.readline

n, k = map(int, input().split())
instructions = []
for _ in range(k):
    instructions.append(input().split())
wheel = ['?'] * n

idx = 0
for s, c in instructions:
    s = int(s)
    idx = (idx - s) % n
    if (wheel[idx] != '?' or c in wheel) and wheel[idx] != c:
        print('!')
        exit()
    else:
        wheel[idx] = c

ans = (wheel[idx:] + wheel[:idx])
print(''.join(ans))



