# 외판원 순회
# 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 입력
n = int(input()) # 도시의 수
w = [0] * n      # W[i][j]: 도시 i에서 도시 j로 가는 비용
for i in range(n):
    w[i] = list(map(int, input().split()))

# 연산
min_cost = 1000000 * n
# dp[i][j] : i번 노드가 시작점, j개의 노드를 방문했을 때까지의 최솟값
dp = [[0] * n for _ in range(n)]
dp[0] = w[0].copy()

for i in range(1, n):
    for j in range(n):
        for 
        dp[i][j] = min(dp[i-1][j] + w[i][j])

# 출력
print(min_cost)