# N과 M (8)
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

MAX_N = 8

def backtrack(cnt, prev):
    # 종료 조건: m개 뽑았을 때
    if cnt == m:
        # 답을 하나 찾음
        print(*sequence)
        return

    # 고르려는 수 i
    for i in range(prev, n):
        # 사용
        sequence[cnt] = nums[i]

        # 다음 숫자 뽑기
        backtrack(cnt + 1, i)


# 입력
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
sequence = [0] * m

# 연산
backtrack(0, 0)