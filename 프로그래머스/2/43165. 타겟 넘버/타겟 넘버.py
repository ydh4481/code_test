def solution(numbers, target):
    answer = 0
    
    def dfs(idx=0, total=0, answer=0):
        if idx == len(numbers):
            if total == target:
                answer += 1
            return answer
        answer = dfs(idx + 1, total + numbers[idx], answer)
        answer = dfs(idx + 1, total - numbers[idx], answer)
        return answer
    
    answer = dfs()
    return answer