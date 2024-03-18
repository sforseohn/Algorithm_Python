import sys, collections
input = sys.stdin.readline
direction = []

def changeDirection(origin, rotation):
    global direction
    if rotation == 'L': # 왼쪽
        new_dir = (origin + 1) % 4
    else:               # 오른쪽
        new_dir = (origin - 1) % 4

    return new_dir


def solution(n, k, l, apples, rotation_t, rotation_d):
    global direction
    board = [[0] * n for _ in range(n)]
    for x, y in apples:  # 사과 위치
        board[x - 1][y - 1] = 2  # 사과 표시
        
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 상좌하우
    
    board[0][0] = 1
    queue = collections.deque()
    queue.append([0, 0])
    
    time = 0
    direc = 3
    rotation_idx = 0

    while(True):
        time += 1
        
        nx = queue[-1][0] + direction[direc][0]
        ny = queue[-1][1] + direction[direc][1]

        if max(nx, ny) >= n or min(nx, ny) < 0 or board[nx][ny] == 1: # 이동 불가
            break
        
        if board[nx][ny] != 2: # 사과 없음
            tx, ty = queue.popleft() 
            board[tx][ty] = 0
            
        board[nx][ny] = 1
        queue.append([nx, ny])
        
        if time in rotation_t:
            direc = changeDirection(direc, rotation_d[rotation_idx])
            rotation_idx += 1
    
    return time

if __name__ == "__main__":
    # 입력
    n = int(input()) # 보드의 크기
    k = int(input()) # 사과의 개수
    apples = [list(map(int, input().split())) for _ in range(k)]  # 사과 위치
    l = int(input()) # 뱀의 방향 변환 횟수
    rotation_t = []  # 시간
    rotation_d = []  # 방향
    for _ in range(l):  # 회전 정보
        t, d = input().split()
        rotation_t.append(int(t)) # t초가 끝난 뒤에
        rotation_d.append(d)      # l: 왼쪽 / d: 오른쪽

    # 연산
    answer = solution(n, k, l, apples, rotation_t, rotation_d)

    # 출력
    print(answer)