def solution(board, moves):
    answer = 0
    stack = [0]
    size = len(board)
    moves = [m - 1 for m in moves]
    
    screen = [[] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if board[i][j]:
                screen[j].append(board[i][j])   

    for move in moves:
        if not screen[move]:
            continue
            
        doll = screen[move].pop(0)
        
        if stack[-1] == doll:
            stack.pop(-1)
            answer += 2
        else:
            stack.append(doll)  
    
    return answer