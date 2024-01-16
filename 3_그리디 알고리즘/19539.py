# 사과나무
# 두 물뿌리개는 동시에 사용해야 한다! -> 사용 횟수가 같음
import sys
input = sys.stdin.readline

def solution():
    total = sum(heights)    # 총 높이의 합

    if total % 3:           # 조건 1. 사과나무의 높이의 총합은 3의 배수여야 함
        return 'NO'
    elif total == 0:
        return 'YES'
    
    two_real = total / 3     # 두 번째 물뿌리개를 사용한 실제 횟수
    two_cnt = 0              # 물뿌리개 2를 사용한 횟수
    for h in heights:
        two_cnt += h // 2
    
    if two_real > two_cnt:   # 조건 2. 두 물뿌리개를 사용한 횟수는 같아야 함
        return 'NO'
    else:
        return 'YES'
    
'''
    while(True):
        two -= 1
        if two == two_num:
            return 'YES'
        elif two_num > two:
            return 'NO'
'''

# 입력
n = int(input())                          # 사과나무의 개수
heights = list(map(int, input().split())) # 바라는 나무의 높이

# 연산
result = solution()

# 출력
print(result)