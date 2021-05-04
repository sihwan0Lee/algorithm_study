def solution(n, datas):
    x, y = 1, 1
    # L R U D
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for data in datas:
        for i in range(len(move_types)):
            if data == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
    return (x, y)


print(solution(5, ['R', 'R', 'R', 'U', 'D', 'D']))

