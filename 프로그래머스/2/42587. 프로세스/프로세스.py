def solution(p, location):
    answer = 0
    max_p = max(p)
    
    while True:
        curr = p.pop(0)
        
        if curr == max_p: # 뽑은 값이 가장 큰 값이면
            answer += 1 # 프로세스 실행 + 1
            if location == 0: # 현재 로케이션이 0이면(타겟이면) 리턴
                return answer
            max_p = max(p) # max_p 재설정
            
        else: # 아니면, 맨 뒤로 이동
            p.append(curr)
            
        location = location - 1 if location else len(p) - 1 # 로케이션 위치 이동(0이었을 경우 맨 뒤로 이동)
        
                
    
    return answer