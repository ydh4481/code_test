def solution(numbers, target):
    answer = 0
    
    def dfs(idx=0, total=0, answer=0):
        if idx == len(numbers): # 정수를 다 썼으면,
            if total == target:     # 타겟 값과 토탈 값이 동일하면,
                answer += 1             # 정답
            return answer           # 리턴
        answer = dfs(idx + 1, total + numbers[idx], answer) # 다음 정수를 더함
        answer = dfs(idx + 1, total - numbers[idx], answer) # 다음 정수를 뺌
        return answer
    
    answer = dfs()
    return answer