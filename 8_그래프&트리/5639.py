import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def postOrder(left, right, tree):
    if left > right: 
        return
    
    root = tree[left]
    
    right_root = 0 # 오른쪽 서브 트리의 루트
    for i in range(left + 1, right + 1):
        if tree[i] > root:
            right_root = i
            break
        
    postOrder(left + 1, right_root - 1, tree)
    postOrder(right_root, right, tree)
    print(root)


def solution(tree):
    postOrder(0, len(tree) - 1, tree)


if __name__ == "__main__":
    tree = []
    while True:
        try:
            tree.append(int(input()))
        except:
            break

    # 연산
    result = solution(tree)