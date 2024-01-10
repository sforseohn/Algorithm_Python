# 이중 우선순위 큐
# 데이터 삭제 시 우선순위가 가장 높거나 낮은 데이터 삭제
import heapq, sys
input = sys.stdin.readline

# 입력
t = int(input()) # 입력 데이터의 개수
for _ in range(t):
    k = int(input()) # 연산의 개수
    
    min_h = [] # 최소 힙
    max_h = [] # 최대 힙
    visited = dict()
    
    for i in range(k) :
        c, n = input().split()
        n = int(n)
        if c == 'I':  # 값 삽입
            heapq.heappush(min_h, (n, i))
            heapq.heappush(max_h, (-n, i))
            visited[i] = False
            
        elif n == 1:  # 최댓값 삭제
            while max_h and visited[max_h[0][1]]: # 이미 방문한 값은 힙에서 제거
                heapq.heappop(max_h)
            
            if max_h:
                visited[max_h[0][1]] = True       # 방문 체크
                heapq.heappop(max_h)           # 최댓값 삭제
                
        elif n == -1: # 최솟값 삭제
            while min_h and visited[min_h[0][1]]: # 이미 방문한 값은 힙에서 제거
                heapq.heappop(min_h)
            
            if min_h:
                visited[min_h[0][1]] = True       # 방문 체크
                heapq.heappop(min_h)           # 최솟값 삭제
    
    # 출력 전 최종 정보 동기화
    while max_h and visited[max_h[0][1]]: 
        heapq.heappop(max_h)
    while min_h and visited[min_h[0][1]]: 
        heapq.heappop(min_h)
           
    # 출력
    if not min_h:
        print('EMPTY')
    else:
        print(-max_h[0][0], min_h[0][0])