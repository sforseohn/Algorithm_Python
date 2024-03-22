import sys, heapq
input = sys.stdin.readline

def solution(lectures):
    lectures.sort()
        
    room = [-1]    
    for s, t in lectures:
        if s >= room[0]:
            heapq.heappushpop(room, t)
        else:
            heapq.heappush(room, t)
        
    return(len(room))
        
            
if __name__ == "__main__":
	# 입력
    n = int(input())
    lectures = [tuple(map(int, input().split())) for _ in range(n)]
	# 연산 & 출력
    print(solution(lectures))