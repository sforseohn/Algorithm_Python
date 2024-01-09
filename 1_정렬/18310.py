# 입력
n = int(input()) # 집의 수
house = list(map(int, input().split())) # 집의 위치

# 연산
house.sort()
ant = house[(n - 1) // 2]

# 출력
print(ant)