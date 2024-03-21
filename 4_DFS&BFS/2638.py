# 치즈
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

direcs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y, n, m, board):
    if x < 0 or x >= n or y < 0 or y  >= m or board[x][y] > 0:
        return 
    
    board[x][y] = -1 # 바깥 공기
    
    for dx, dy in direcs:
        nx = x + dx
        ny = y + dy
        dfs(nx, ny, n, m, board)


def check_disappear(x, y, board):
    cnt = 0
    
    for dx, dy in direcs:
        nx = x + dx
        ny = y + dy
        if board[nx][ny] == -1:
            cnt += 1
    
    return cnt >= 2
    
    
def solution(n, m, board):
    ans = 0
    # 외부 공기 표시
    dfs(0, 0, n, m, board)
    
    while True:
        # 없어지는 치즈 표시
        disappear = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1 and check_disappear(i, j, board):
                    disappear.append((i, j))
                        
        if not disappear: # 더이상 사라지는 치즈가 없으면 종료
            break
        
        # 치즈 없애기
        for i, j in disappear:
            board[i][j] = 0
            dfs(i, j, n, m, board)
        
        ans += 1
    return ans


if __name__ == "__main__":
    #입력
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    #연산
    answer = solution(n, m, board);    
    #출력
    print(answer)