# 기타 레슨
import sys
input = sys.stdin.readline

def countBlurays(bluray): # 주어진 블루레이 길이로 몇 개의 블루레이가 필요한지 계산
    cnt = 1
    cur_sum = 0
    
    for l in lectures:
        if cur_sum + l > bluray:
            cnt += 1
            cur_sum = 0
        cur_sum += l
    return cnt    

# 입력
n, m = map(int, input().split()) # 강의, 블루레이의 수
lectures = list(map(int, input().split()))

# 연산
r = sum(lectures)
l = max(lectures)
result = 0

while l <= r:
    mid = (l + r) // 2
    if countBlurays(mid) <= m:
        result = mid
        r = mid - 1
    else:
        l = mid + 1

# 출력
print(result)
