"""
플로이드-워셜 알고리즘

임의의 노드 s에서 e까지 가는 데 걸리는 최단거리를 구하기 위해,
s와 e 사이의 노드인 m에 대해 s에서 m까지 가는 데 걸리는 최단거리와 m에서 e까지 가는 데 걸리는 최단거리를 이용한다.

조금 더 구체적인 설명을 위해, 임의의 노드 s 부터 e 까지 가는데 걸리는 최단거리를 d[s][e]라고 하자. (처음에 d[s][e]의 값은 노드 s와 노드 e가 직접적으로 연결되어 있다면 그 노드의 가중치만큼,
그렇지 않다면 무한(INF)로 초기화한다.[3]) 이 d[s][e]를 구하기 위해서, s와 e 사이의 모든 노드 m에 대해, 현재 d[s][e]에 저장되어 있는 값과, d[s][m]+d[m][e]의 값을 비교한다.
이 때 d[s][m]+d[m][e]의 값이 현재의 d[s][e] 값보다 작으면, d[s][e]를 d[s][m]+d[m][e] 의 값으로 업데이트한다.

"""

if __name__ == '__main__':
    n = int(input())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    for m in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][m] and graph[m][j]:
                    graph[i][j] = 1

    for _ in graph:
        print(' '.join(map(str, _)))
