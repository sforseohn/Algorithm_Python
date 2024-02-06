# 연산자 끼워넣기
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

ADD, SUB, MUL, DIV = 0, 1, 2, 3
MAX_INT = 1e9

def calculate(n1, op, n2): # n1과 n2를 op로 연산해준다
    if op == ADD:
        return n1 + n2
    elif op == SUB:
        return n1 - n2
    elif op == MUL:
        return n1 * n2
    elif op == DIV:
        if n1 < 0 and n2 > 0:
            return -(-n1 // n2)
        return n1 // n2


def completeFormula():
    global max_ans, min_ans
    result = a[0]

    # 뽑힌 연산자마다 계산
    for i in range(n-1):
        result = calculate(result, sequence[i], a[i+1])
        
    # 최대, 최솟값 업데이트
    max_ans = max(max_ans, result)   
    min_ans = min(min_ans, result)
    

def backtrack(cnt):
    if cnt == n-1: # 연산자가 모두 뽑혔다면
        completeFormula()
        return
    
    for i in range(len(ops)):
        if not ops[i]: # 연산자가 남아 있지 않다면
            continue
        
        # 사용
        sequence[cnt] = i
        ops[i] -= 1
        
        # 다음 탐색
        backtrack(cnt + 1)
        
        # 반납
        ops[i] += 1
        

# 입력
n = int(input())
a = list(map(int, input().split()))
ops = list(map(int, input().split()))

# 연산
sequence = [0] * (n-1) # 각 연산자 저장
max_ans = -MAX_INT
min_ans = MAX_INT

backtrack(0)

# 출력
print(int(max_ans), int(min_ans), sep="\n")