# DFS
# Depth-First Search
# 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# 그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말한다.
# 프로그래밍에서는 그래프를 크게 두가지 방식으로 표현할 수 있다.
# 1. 인접 행렬(Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현하는 방식
# 2. 인접 리스트(Adjacency List): 리스트로 그래프의 연결 관계를 표현하는 방식

# 인접 행렬
# 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식이다.
# 실제 코드에서는 논리적으로 정답이 될 수 없는 큰 값(999999999) 무한의 비용을 통해 값을 초기화 시킨다.
# INF = 999999999
# graph = [
#   [0, 7, 5],
#   [7, 0, INF],
#   [5, INF, 1]
# ]

# 인접 리스트
# 모든 노드에 대한 정보를 차례대로 연결하여 저장한다
# 연결 리스트라는 자료구조를 이용해 구현하는데 파이썬은 기본적으로 리스트자료형이 append()와 메소드를 제공한다.
# 어쨋든 파이썬으로 인접 리스트를 이용해 그래프를 표현하고자 할 때에도 단순히 2차원 리스트를 이용하면 된다.

graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))
# 노드 1에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0, 7))
# 노드 2에 연결된 노드 정보 저장 (노드, 거리)
graph[2].append((0, 5))

print(graph)


# 인접 행렬 방식   :  모든 관계를 저장하므로 노드 개수가 많을수록 불필요한 메모리 낭비.
# 인접 리스트 방식  :  연결된 정보만을 저장하여 메모리 효율적 사용하지만 인접 행렬 방식에 비해 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다.

# 특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우, 인접 리스트 방식이 인접 행렬 방식에 비해 메모리 공간의 낭비가 적다.
# DFS는 특정 경로로 탐색하다가 특정 상황에서 최대한 깊숙이 들어가 노드를 방문하고, 다시 돌아가 다른 경로로 탐색하는 알고리즘이다.
# DFS는 스택을 이용한다.
# 1.탐색 시작 노드를 스택에 삽입(방문처리)
# 2.스택의 최상단 노드에 방문하지 않은 인접 노드가 있다면 그 노드를 스택에 넣고 방문 처리.
# 2.이 때 방문하지 않은 인접 노드가 없다면 스택에서 최상단 노드를 꺼냄.
# 3.2번의 과정을 더 이상 수행할 수 없을 때 까지 반복함.
