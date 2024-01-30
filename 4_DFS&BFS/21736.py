# 헌내기는 친구가 필요해
import sys, collections
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def bfs(start_pos):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    person_cnt = 0     # 만날 수 있는 사람의 수
    
    queue = collections.deque()
    visited[start_pos[0]][start_pos[1]] = 1
    queue.append((start_pos[0], start_pos[1]))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                
                if campus[nx][ny] == 'X':
                    continue
                
                queue.append((nx, ny))
                
                if campus[nx][ny] == 'P':
                    person_cnt += 1
    return person_cnt

# 입력
n, m = map(int, input().split())      # 캠퍼스의 크기
campus = [[] for _ in range(n)]       # 캠퍼스의 정보
visited = [[0] * m for _ in range(n)] # 방문 기록
found = False                         # 시작점 찾기
for i in range(n):
    campus[i] = list(input().strip())
    
    if not found:
        for j in range(m):
            if campus[i][j] == 'I':
                found = True
                start_pos = i, j

# 연산
person_cnt = bfs(start_pos)

# 출력
if person_cnt:
    print(person_cnt)
else:
    print('TT')