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


0 0 pop이전:  deque([(0, 0)])
0 0 deque([])
방문 후:  deque([(1, 0)])
0 0 pop이전:  deque([(1, 0)])
1 0 deque([])
방문 후:  deque([(0, 0)])
방문 후:  deque([(0, 0), (1, 1)])
1 0 pop이전:  deque([(0, 0), (1, 1)])
0 0 deque([(1, 1)])
0 0 pop이전:  deque([(1, 1)])
1 1 deque([])
방문 후:  deque([(1, 2)])
1 1 pop이전:  deque([(1, 2)])
1 2 deque([])
방문 후:  deque([(0, 2)])
방문 후:  deque([(0, 2), (1, 3)])
1 2 pop이전:  deque([(0, 2), (1, 3)])
0 2 deque([(1, 3)])
0 2 pop이전:  deque([(1, 3)])
1 3 deque([])
방문 후:  deque([(1, 4)])
1 3 pop이전:  deque([(1, 4)])
1 4 deque([])
방문 후:  deque([(0, 4)])
방문 후:  deque([(0, 4), (1, 5)])
1 4 pop이전:  deque([(0, 4), (1, 5)])
0 4 deque([(1, 5)])
0 4 pop이전:  deque([(1, 5)])
1 5 deque([])
방문 후:  deque([(2, 5)])
1 5 pop이전:  deque([(2, 5)])
2 5 deque([])
방문 후:  deque([(3, 5)])
2 5 pop이전:  deque([(3, 5)])
3 5 deque([])
방문 후:  deque([(4, 5)])
방문 후:  deque([(4, 5), (3, 4)])
3 5 pop이전:  deque([(4, 5), (3, 4)])
4 5 deque([(3, 4)])
방문 후:  deque([(3, 4), (4, 4)])
4 5 pop이전:  deque([(3, 4), (4, 4)])
3 4 deque([(4, 4)])
방문 후:  deque([(4, 4), (3, 3)])
3 4 pop이전:  deque([(4, 4), (3, 3)])
4 4 deque([(3, 3)])
방문 후:  deque([(3, 3), (4, 3)])
4 4 pop이전:  deque([(3, 3), (4, 3)])
3 3 deque([(4, 3)])
방문 후:  deque([(4, 3), (3, 2)])
3 3 pop이전:  deque([(4, 3), (3, 2)])
4 3 deque([(3, 2)])
방문 후:  deque([(3, 2), (4, 2)])
4 3 pop이전:  deque([(3, 2), (4, 2)])
3 2 deque([(4, 2)])
방문 후:  deque([(4, 2), (3, 1)])
3 2 pop이전:  deque([(4, 2), (3, 1)])
4 2 deque([(3, 1)])
방문 후:  deque([(3, 1), (4, 1)])
4 2 pop이전:  deque([(3, 1), (4, 1)])
3 1 deque([(4, 1)])
방문 후:  deque([(4, 1), (3, 0)])
3 1 pop이전:  deque([(4, 1), (3, 0)])
4 1 deque([(3, 0)])
방문 후:  deque([(3, 0), (4, 0)])
4 1 pop이전:  deque([(3, 0), (4, 0)])
3 0 deque([(4, 0)])
3 0 pop이전:  deque([(4, 0)])
4 0 deque([])
