# 경쟁적 전염
import sys, collections
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def bfs(start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 목표 지점에서부터
    # 조건 1: 최단 경로가 가장 가까운 곳
    # 조건 2: 최단 경로가 같다면 바이러스 번호가 더 작은 곳
    queue = collections.deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1
    ans = (s+2, k)
    
    while queue:
        (x, y) = queue.popleft()
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 유효한 범위 내에 있고, 방문하지 않았을 때
            if 0 < nx <= n and 0 < ny <= n and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1  # 거리 저장
                
                if graph[nx][ny]:                              # 해당 위치에 바이러스가 있고
                    if (visited[nx][ny], graph[nx][ny]) < ans: # 거리가 작거나 거리가 같고 바이러스 수가 작으면
                        ans = (visited[nx][ny], graph[nx][ny]) # 거리와 바이러스 종류 갱신
                        
                # 바이러스가 없다면 최단 경로가 저장된 값보다 작을 때만 큐에 추가
                elif visited[nx][ny] < ans[0]: 
                    queue.append((nx, ny))
    return ans


# 입력
n, k = map(int, input().split())            # 시험관의 크기, 최대 바이러스 번호

graph = [[0] for _ in range(n+1)]           # 시험관
visited = [[0] * (n+1) for _ in range(n+1)] # 방문 체크
for i in range(1, n+1):
    graph[i] += list(map(int, input().split()))
s, x, y = map(int, input().split())         # 초, 목표 지점

if graph[x][y]:       # 이미 바이러스가 존재하는 곳이면 -> 최소 케이스 확인 중요...
    print(graph[x][y])
else:
    # 연산
    ans = bfs(x, y)

    # 출력
    if ans[0] == s+2: # 제한 시간 안에 전염되지 않았으면
        print(0)
    else:
        print(ans[1])