# 거짓말
import sys
input = sys.stdin.readline

# Find: 특정 원소가 속한 집합 찾기
def find_parent(parent, x): # parent 리스트: 각 원소의 부모 저장
    if parent[x] != x:      # 루트를 찾을 때까지 find 호출
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union: 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a # 더 작은 수를 루트로 설정
    else:
        parent[a] = b
    
    
n, m = map(int, input().split())
true = list(map(int, input().split()))

if true[0] == 0: # 진실을 아는 사람이 없으면
    print(m)
    exit(0)
    
# 부모 테이블을 자기 자신으로 초기화
parent = [i for i in range(n+1)]

# 집합을 합칠 원소를 입력받고 유니온 연산 수행
for i in range(2, true[0] + 1):
    union_parent(parent, true[i-1], true[i])

leader = [] # 각 파티마다 비교할 하나의 원소만 저장
cnt = m
for i in range(m):
    party = list(map(int, input().split()))

    for j in range(2, party[0] + 1):
        union_parent(parent, party[j-1], party[j])
    leader.append(party[1])

true_root = find_parent(parent, true[1])

for i in range(m):
    if find_parent(parent, leader[i]) == true_root:
        cnt -= 1

print(cnt)    
