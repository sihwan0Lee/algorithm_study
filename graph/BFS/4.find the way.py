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
print(distance)

q = deque([x])

while q:
    print("q :", q)
    now = q.popleft()
    print("now : ", now)
    for next_node in graph[now]:
        print("next_node : ", next_node)
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            print("q :", q)
            print("distance : ", distance)
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)


# distance를 노드 갯수에 맞춰 리스트를 구성한다음, 방문할때마다 업데이트 한다.
# 현재 노드가 1일때,
# 현재 노드를 데크에서 빼고, 그래프에는 해당 노드위치에 연결된 노드들의 정보가 있으니까
# 얘네로 반복문을 돌리면 다음 노드에 대한 정보를 알수 있다.
# 그렇게 distance를 업데이트 해나가는 방식.

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4
# [-1, 0, -1, -1, -1]
# q : deque([1])
# now :  1
# next_node :  2
# q : deque([2])
# distance :  [-1, 0, 1, -1, -1]
# next_node :  3
# q : deque([2, 3])
# distance :  [-1, 0, 1, 1, -1]
# q : deque([2, 3])
# now :  2
# next_node :  3
# next_node :  4
# q : deque([3, 4])
# distance :  [-1, 0, 1, 1, 2]
# q : deque([3, 4])
# now :  3
# q : deque([4])
# now :  4
# 4
