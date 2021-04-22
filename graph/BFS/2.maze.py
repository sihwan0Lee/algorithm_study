# 미로 탈출
# 괴물이 있는 부분 0, 괴물이 없는 부분 1
# 한 길을 끝까지 갔다가 막혀서 돌아오는 것과
# 가까운 길을 모두 확인하면서 가는 것.
# 길찾기에는 아무래도 BFS가 적절한가 보다.
# 항상 입구는(1, 1) 출구는 (N, M)
from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        print(x, y, "pop이전: ", queue)
        x, y = queue.popleft()
        print(x, y, queue)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                print("방문 후 : ", queue)
    return graph[n - 1][m - 1]


print(bfs(0, 0))

