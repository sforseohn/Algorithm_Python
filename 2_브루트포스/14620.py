def checkFlower(i, j): # 꽃을 놓을 수 있는 자리인지 확인
    for d in direction:
        x = i + d[0]
        y = j + d[1]
        if visited[x][y] == True: # 이미 방문했으면
            return False
    return True

def putFlower(i, j, put=True): # 꽃 놓기
    global total_price
    
    for d in direction:
        x = i + d[0]
        y = j + d[1]
        
        if put == True:
            visited[x][y] = True
            total_price += price[x][y]            
        else:
            visited[x][y] = False
            total_price -= price[x][y] 
    
def seek(cnt):
    global total_price, min_price
    
    if cnt == FLOWER_NUM:
        if total_price < min_price:
            min_price = total_price
        return
    
    # 꽃 놓기
    for i in range(1, n-1):
        for j in range(1, n-1):
            if checkFlower(i, j):
                putFlower(i, j)
                
                seek(cnt + 1)
                
                putFlower(i, j, False)

FLOWER_NUM = 3
MAX_PRICE = 200 * 10 * 10

# 입력
n = int(input()) # 한 변의 길이
price = [list(map(int, input().split())) for i in range(n)] # 화단의 지점당 가격

direction = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
min_price = MAX_PRICE
total_price = 0 
visited = [[False] * n for i in range(n)]

# 연산
seek(0)

# 출력
print(min_price)