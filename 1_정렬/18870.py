# 좌표 압축
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수
import sys
input = sys.stdin.readline

# 입력
n = int(input()) # 좌표의 수
x = list(map(int, input().split()))

# 연산
# 셋으로 변환하여 중복값 삭제 후 정렬
# 딕셔너리에 좌표값: 순서 형태로 저장  
x_ordered = sorted(list(set(x)))

x_dict = dict()
for i in range(len(x_ordered)):
    x_dict[x_ordered[i]] = i

# 출력
ans = ''
for key in x:
    print(x_dict[key], end=' ') # 인덱스를 찾아 출력
   