# 이 문제를 통해 좌표에 대한 구현을 배울 수 있다.
# N x N 크기의 공간을 벗어나는 움직임은 무시한다.
# 처음 접할 땐 좌표를 보고 xy축을 먼저 생각했지만, 여러 문제를 접하다보니 컴퓨터에서의 좌표는 선형대수를 이용하는듯 하다.
# - 행 ㅣ 렬 말이다. (행, 열)
# 왼쪽으로 이동한다는건, 열이 왼쪽으로 움직인다는 의미이다. 이는 xy축에서는 x축의 움직임으로 생각할수 있다.
# 오른쪽으로 이동한다는건, 열이 오른쪽으로 움직인다는 의미이다. 이는 xy축에서는 x축의 움직임으로 생각할수 있다.
# 위로 이동한다는건, 행의 변화이다. 이는 xy축에서는 y축의 움직임이다.
# 아래로 이동한다는건, 행의 변화이다. 이는 xy축에서는 y축의 움직임이다.
# 하지만 선형대수의 입장에서 생각해야한다. 말이 그냥 xy이지 행 렬 로 생각해야한다.
# 위를 정리해보면
#       L  R  U D
# dx = [0, 0,-1,1]
# dy = [-1,1, 0,0]

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)


# 정리
# 좌표의 포인트 -> (x,y)= (행,렬)
#       L  R  U D
# dx = [0, 0,-1,1]
# dy = [-1,1, 0,0]
