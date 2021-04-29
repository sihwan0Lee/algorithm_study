# 특정 거리의 도시 찾기
# N : 도시의 개수,  M : 도로의 개수,  K : 거리 정보,  X : 출발 도시의 번호
# 최단거리가 K인 모든 도시의 번호를 출력하는 프로그램을 작성하자.
# 최단거리가 K인 도시가 하나도 없다면 -1을 출력하자

# 그래프에서 모든 간선의 비용이 동일할 떄는 너비 우선 탐색을 이용하여 최단 거리를 찾을 수 있다.


from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0  # 출발 도시까지의 거리는 0으로 설정


q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
