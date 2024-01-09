import sys
input = sys.stdin.readline

def findMaxCandy(): # 사탕의 최대 개수 찾기
    global board
    global max_cnt
    
    for i in range(n): # 행을 순회하며 탐색
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
        
        cnt = 1
        for j in range(1, n): # 열을 순회하며 탐색
            if board[i][j] == board[i][j-1]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
    return max_cnt  

n = int(input()) # 보드의 크기
board = [list(input()) for _ in range(n)]
max_cnt = 0

# 바꾸기
for i in range(n):
    for j in range(n):
        if i+1 < n and board[i][j] != board[i+1][j]:
            # 교환
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            
            # 사탕의 최대 개수 찾기
            findMaxCandy()

            # 원래대로 돌리기
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

        if j+1 < n and board[i][j] != board[i][j+1]:
            # 교환
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            
            # 사탕의 최대 개수 찾기
            findMaxCandy()
            
            # 원래대로 돌리기
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

print(max_cnt)