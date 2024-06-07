def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            answer += 1
            
    return answer

def dfs(computers, target, visited):
    visited[target] = True
    for i in range(len(computers)):
        if i != target and computers[target][i] == 1 and not visited[i]:
            dfs(computers, i, visited)
            