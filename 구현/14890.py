# 경사로
import sys
input = sys.stdin.readline

def seek(ground):
    global cnt
    for i in range(n):
        connected = 1     # 이어진 땅의 개수
        downhill = False  # 아래로 내려가는 경사로 여부

        for j in range(1, n):            
            diff = ground[i][j] - ground[i][j-1] # 이전 땅과의 차이   
            if abs(diff) > 1:            # 차이가 1보다 크면 탈락
                break
            
            if not downhill:                        # 이전 땅에서 이어진 경사로가 없으면
                if not diff:                        # 차이가 없다면 이어진 칸 수 + 1
                    connected += 1
                else:                               # 차이가 있다면
                    if diff == 1 and connected < l: # 현재 칸이 이전 칸보다 높은데 경사로를 놓을 장소가 충분하지 않다면 탈락
                        break
                    elif diff == -1:                # 현재 칸이 이전 칸보다 낮으면 -> 경사로 시작!                        
                        if l == 1:
                            connected = 0
                            continue
                        downhill = True  
                    connected = 1                   # 이어진 칸 수 리셋 
            else:                                   # 이전 땅에서 이어진 경사로가 있으면
                if diff:                            # 경사로를 놓을 땅의 높이가 같지 않으면 탈락
                    break
                
                connected += 1
                if connected == l:                  # 경사로 완성, 갱신
                    downhill = False
                    connected = 0         
        else: # break 없이 한 줄 순환이 끝났는데 경사로를 더 놓아야 한다면 탈락
            if not downhill: 
                cnt += 1
        
# 입력
n, l = map(int, input().split()) # 지도의 크기, 경사로의 길이
ground = [[] for _ in range(n)]
for i in range(n):
    ground[i] = list(map(int, input().split()))

# 연산
cnt = 0
seek(ground)
seek([list(row) for row in zip(*ground)])

# 출력
print(cnt)