# 연구소
# N x M 크기의 연구소, 0은 빈칸 , 1은 벽, 2는 바이러스가 있는 곳이다.
# 벽을 3개 세워서 바이러스가 퍼질수 없는 안전영역을 가장 많이 확보하자.

# 이 문제는 벽을 3개 설치하는 모든 경우의 수를 다 계산해야한다.
# 가능한 모든 경우의 수를 계산하되, 안전 영역을 계산할 때 dfs, bfs를 적절히 이용해야 한다.
# 매번 벽을 설치할 때마다, 각 바이러스가 사방으로 퍼지는 것을 dfs, bfs를 통해 계산해서 안전영역을 구해야 한다.

n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]  # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# dfs를 이용해 각 바이러스가 사방으로 퍼지도록 하기


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
# 바이러스를 4방향으로 이동시킵니다.(맵을 안넘는 선에서), 만약 해당 좌표의 값이 0(빈공간)이면 2로 바이러스 영역을 표시합니다.

# 안전영역의 크기를 구하는 메서드


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# dfs를 이용해 울타리를 설치하면서 , 매번 안전영역의 크기를 계산


def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)


# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
