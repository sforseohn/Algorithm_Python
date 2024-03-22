import sys
input = sys.stdin.readline

def solution(n, record):
    wheel = ['?'] * n
    i = 0
    
    for rot, c in record:
        i = (i - int(rot)) % n
        if wheel[i] != c and (wheel[i] != '?' or c in wheel):
            return '!'
        else:
            wheel[i] = c
        
    ans = wheel[i:] + wheel[:i]
    return ''.join(ans)

n, k = map(int, input().split())
record = [input().split() for _ in range(k)]

print(solution(n, record))