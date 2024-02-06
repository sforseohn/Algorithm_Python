# N과 M (12)
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def backtrack(cnt, prev):
    global prev_sequence
    
    # 종료 조건: m개 뽑았을 때
    if cnt == m:
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
nums = list(set(map(int, input().split())))
nums.sort()
n = len(nums)
sequence = [0] * m

# 연산
prev_sequence = []
backtrack(0, 0)
