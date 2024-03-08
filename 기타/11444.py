import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def matMul(a, b):
    result = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for z in range(2):
                # c11 = a11*b11 + a12*b21
                result[i][j] += a[i][z] * b[z][j] % 1000000007
    return result
    

def power(a, b):
    if b == 1: # b가 1이 될 때까지 반복
        return a
    else: 
        tmp = power(a, b//2) # a^(b//2)
        mat_mul = matMul(tmp,tmp)
        
        if not b % 2: 
            return mat_mul
        else:
            return matMul(mat_mul, a)

# 입력
n = int(input())
matrix = [[1, 1], [1, 0]] # 피보나치 초기값

# 연산
ans = power(matrix, n)

# 출력
print(ans[0][1] % 1000000007)