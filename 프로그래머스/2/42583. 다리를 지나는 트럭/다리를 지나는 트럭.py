from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    
    bridge = []
    i = 0
    while truck_weights:
        
        for truck in bridge:
            truck[1] -= 1
        
        next_truck = truck_weights[0]
        sum_bridge = sum([t[0] for t in bridge])
        if sum_bridge + next_truck <= weight:
            bridge.append([truck_weights.pop(0), bridge_length - 1])
        if bridge[0][1] == 0:
            bridge.pop(0)
            
        answer += 1
    
    return answer + bridge[-1][1]