# 음료수 얼려먹기
# 얼음틀이 0 과 1로 구성되어있다. 구멍이 뚫린 부분이 0 으로 되어있다.
# 틀이 주어질 때 생성되는 총 얼음의 개수
# 얼음을 얼릴 수 있는 공간이 상하좌우로 연결되어 있다고 볼 수 있다.

# 특정 지점에서 주변 상하좌우를 살펴본다. 주변 지점중 값이 0이면서 아직 방문안한 곳을 방문한다.

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 아직 방문을 안했다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1


print(result)


# 0 0 1
# 0 1 0
# 1 0 1
# dfs(1, 1)을 진행하고 나면
# (True 0->1) , (True 0->1) , 1
# (True 0->1) , 1           , 0
# 1           , 0           , 1
# result = 1

# dfs(1, 2)
# False

# dfs(1, 3)
# False

# dfs(2, 1)
# False
# dfs(2, 2)
# False

# dfs(2, 3)
# (True 0->1) , (True 0->1) , 1
# (True 0->1) , 1           , (True 0->1)
# 1           , 0           , 1
# (2, 3)주변은 애초에 False
# result + 1

# dfs(3, 1)
# False
# dfs(3, 2)
# (True 0->1) , (True 0->1) , 1
# (True 0->1) , 1           , (True 0->1)
# 1           , (True 0->1) , 1
# result + 1

# 그래서 result 가 3이 돼는것이다.
# 방문 처리가 그래프에선 상당히 중요하다는걸 느끼게 된 문제이다.
