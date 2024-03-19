import sys
sys.setrecursionlimit(10 ** 6)

def postOrder(left, right, tree, result):
    # 종료 조건
    if left > right:
        return

    root = tree[left]  # 전위 순회에서 가장 먼저 순회하는 노드는 root 노드
    div = left + 1  # root보다 큰 노드 중 첫 번째 인덱스 (root 노드의 오른쪽 자식 노드)
    for i in range(left + 1, right + 1):
        if tree[i] > root:
            div = i
            break

    # 후위 순회: left -> right -> root
    postOrder(left + 1, div - 1, tree, result)  # left 서브 트리 탐색
    postOrder(div, right, tree, result)  # right 서브 트리 탐색

    result.append(root)  # root 입력


def solution(tree):
    result = []
    postOrder(0, len(tree) - 1, tree, result)
    return result


if __name__ == "__main__":
    tree = []
    while True:
        try:
            tree.append(int(input()))
        except:
            break

    # 연산
    result = solution(tree)

    # 출력
    for i in result:
        print(i)