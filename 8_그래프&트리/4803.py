# 트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

visited = []

def dfs(parent, node, graph):
    global visited
    for child in graph[node]:
        if child == parent:
            continue
        
        if visited[child]:
            return False
        
        visited[child] = 1
        if not dfs(node, child, graph):
            return False
            
    return True
    
    
def solution(n, graph): 
    global visited
    tree_cnt = 0
    visited = [0] * (n + 1)
    for i in range(1, n+1):
        if not visited[i]:
            is_tree = dfs(0, i, graph) 
            if not is_tree:
                continue
            tree_cnt += 1

    return tree_cnt
    

if __name__ == "__main__":
    tc_cnt = 0
    while True:
        tc_cnt += 1
        n, m = map(int, input().split())
        if not n: 
            break
        graph = [[] for _ in range(n+1)] 
        
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        # 연산
        result = solution(n, graph)
        print('Case ' + str(tc_cnt) + ':', end=' ')
        if not result:
            print('No trees.')
        elif result == 1:
            print('There is one tree.')
        else:
            print(f'A forest of {result} trees.')  