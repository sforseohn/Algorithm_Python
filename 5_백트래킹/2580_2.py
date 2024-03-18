# 스도쿠
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

SIZE = 9    # 스도쿠 한 행 사이즈
check_row = [[False] * (SIZE + 1) for _ in range(SIZE)] # 각 행의 숫자 존재 여부 체크
check_col = [[False] * (SIZE + 1) for _ in range(SIZE)] # 각 열의 숫자 존재 여부 체크
check_3x3 = [[False] * (SIZE + 1) for _ in range(SIZE)] # 각 3x3 사각형의 숫자 존재 여부 체크

def calc_area(x, y):
    return (x // 3) * 3 + y // 3


def backtrack(cnt, board):
    # 빈칸을 다 채웠으면
    if cnt == SIZE * SIZE:
        return True
    
    x, y = cnt // SIZE, cnt % SIZE
    
    if board[x][y] > 0:
        return backtrack(cnt + 1, board)
        
    for n in range(1, SIZE + 1):    
        if check_row[x][n] or check_col[y][n] or check_3x3[calc_area(x, y)][n]:
            continue
        
        board[x][y] = n
        check_row[x][n] = True
        check_col[y][n] = True
        check_3x3[calc_area(x, y)][n] = True
        
        if backtrack(cnt + 1, board):
            return True
        
        board[x][y] = 0
        check_row[x][n] = False
        check_col[y][n] = False
        check_3x3[calc_area(x, y)][n] = False
    
    return False
    
    
def solution(board):
    answer = [[0] * SIZE for _ in range(SIZE)]
    # check 배열에 정보 기록
    for i in range(SIZE):
        for j in range(SIZE):
            val = board[i][j]
            answer[i][j] = val
            
            if not val:
                continue
            
            check_row[i][val] = True
            check_col[j][val] = True
            check_3x3[calc_area(i, j)][val] = True

    backtrack(0, answer)
    
    return answer
    
    
if __name__ == "__main__":
	# 입력
    sudoku = [list(map(int, input().split())) for _ in range(SIZE)]
    
    for line in solution(sudoku):
	    print(*line) 