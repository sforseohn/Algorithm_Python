answer = 0
check_row = []
check_col = []
check_rd = [] # 우하향 대각선
check_ld = [] # 좌상향 대각선 

def backtrack(n, cnt, x):
    global answer, check_row, check_col, check_rd, check_ld
    if cnt == n:
        answer += 1
        return

    for y in range(n):
        rd = x + y
        ld = n - 1 - x + y
        
        if check_row[x] or check_col[y] or check_rd[rd] or check_ld[ld]:
            continue  
            
        # 사용
        check_row[x] = 1
        check_col[y] = 1
        check_rd[rd] = 1
        check_ld[ld] = 1      
        
        backtrack(n, cnt + 1, x + 1)
        
        # 반납
        check_row[x] = 0
        check_col[y] = 0
        check_rd[rd] = 0
        check_ld[ld] = 0
    

def solution(n):
    global answer, check_row, check_col, check_rd, check_ld
    
    check_row = [0] * n
    check_col = [0] * n
    check_rd = [0] * (n * 2 - 1)
    check_ld = [0] * (n * 2 - 1)
    
    backtrack(n, 0, 0)

    return answer