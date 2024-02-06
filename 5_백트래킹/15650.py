import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

MAX_N = 8

def printSequence():
    print(*sequence)


def backtrack(cnt, prev):
    # 종료 조건: m개 뽑았을 때
    if cnt == m:
        # 답을 하나 찾음
        printSequence()
        return

    # 고르려는 수 i
    for i in range(prev+1, n+1):
        # 이미 골랐던 숫자라면, 사용 불가
        if is_used[i]:
            continue

        # 사용
        sequence[cnt] = i
        is_used[i] = True

        # 다음 숫자 뽑기
        backtrack(cnt + 1, i)

        # 반납
        is_used[i] = False


# 입력
n, m = map(int, input().split())
sequence = [0] * m
is_used = [0] * (MAX_N + 1)

# 연산
backtrack(0, 0)