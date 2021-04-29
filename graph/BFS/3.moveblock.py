# 블록 이동하기
# 크기가 2 x 1 인 로봇으로 N x N 크기의 지도에서 로봇음 움직여 N x N까지 이동시키려고 한다
# 숫자 0 은 빈칸을 ,1 은 벽을 나타낸다.
# 로봇은 벽기 있는 칸과 지도 밖으로는 이동할 수 없다.
# 로봇의 처음 위치는 (1, 1)에서 가로 방향으로 놓여 있다.
# 앞뒤 상관 없이 움직일 수 있다.
# 로봇이 차지하는 두 칸 중 어느 한 칸이라도 (N, N) 위치에 도착하면 된다.
# 로봇은 회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 한다.
# 로봇이 한칸 이동하거나, 90도 회전하는 데 걸리는 시간은 정확히 1초이다.
# 최소시간을 구하시오.

from collections import deque


def get_next_pos(pos, board):
    next_pos = []  # 반환 결과(이동 가능한 위치들)
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 상 하 좌 우 이동 경우 (x=행, y=열)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + \
            dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y),
                             (pos2_next_x, pos2_next_y)})
    # 현재 로봇이 가로롤 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]:  # 위쪽으로 회전하거나, 아래쪽으로 회전
            # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]:  # 왼쪽으로 회전하거나, 오른쪽으로 회전
            # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos


def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # BFS
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}  # 시작 위치
    q.append((pos, 0))  # 큐에 삽입한 뒤에
    visited.append(pos)  # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        print(pos, cost)
        # (n, n)위치에 도달 했다면, 최단 거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
      0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
