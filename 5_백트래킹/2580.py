# 스도쿠
   
def backtrack(cnt):
    global board
    if cnt == len(blanks): # 빈칸을 모두 채웠다면 종료
        for line in board:
            print(*line)
        exit(0)
    
    x, y = blanks[cnt][0], blanks[cnt][1]
    
    for n in range(1, 10):
        check = True # 조건 만족 여부
        for j in range(9):
            # 가로줄, 세로줄, 사각 박스를 체크해 i에 해당하는 숫자가 모두 존재하지 않는다면 현재 칸에는 i를 넣을 수 있다는 뜻이다
            # 가로줄 체크
            if board[x][j] == n:
                check = False
                break
            # 세로줄 체크
            if board[j][y] == n:
                check = False
                break
            # 사각 박스 체크
            if board[j%3 + x//3 * 3][j//3 + y//3 * 3] == n:
                check = False
                break    
                
        if not check:
            continue
        
        # 사용
        board[x][y] = n
        
        # 다음 탐색
        backtrack(cnt + 1)
        
        # 반납
        board[x][y] = 0
        

# 입력
board = [list(map(int,input().split())) for _ in range(9)]
blanks = []  # 비어있는 칸 

for i in range(9):
    for j in range(9):
        if not board[i][j]:
            blanks.append((i, j))

# 연산
backtrack(0)