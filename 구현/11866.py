'''
요세푸스 문제
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
'''
import sys
input = sys.stdin.readline

# 입력
# 사람의 수, 제거할 사람
n, k = map(int, input().split())

# 연산
q = [i for i in range(1, n+1)]
result = []
for i in range(n):
    for j in range(k-1):
        q.append(q.pop(0))
    result.append(q.pop(0))

# 출력
print('<' + ', '.join(map(str, result)) + '>')
        