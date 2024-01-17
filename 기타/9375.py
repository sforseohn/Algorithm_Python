# 패션왕 신해빈
import sys
from itertools import combinations
import collections
input = sys.stdin.readline

# 입력
t = int(input())                                 # 테스트 케이스의 수

for _ in range(t):
    n = int(input())                             # 의상의 수
    cloth = collections.defaultdict(lambda: 1)   # 기본값이 1인 의상 딕셔너리
    
    for _ in range(n):
        name, category = input().strip().split() # 의상의 이름, 종류
        cloth[category] += 1
        
    # 연산
    # 각 의상 종류에서 하나씩을 뽑거나 뽑지 않는 경우의 수
    # 전체 * (각 의상 종류별 개수 + 1)
    cnt = 1
    for c in cloth:
        cnt *= cloth[c]
    cnt -= 1                                    # 알몸 상태는 안 되므로 제외
        
    # 출력
    print(cnt)