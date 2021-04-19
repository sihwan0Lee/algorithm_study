# 8 x 8의 체스판속의 나이트
# 1. 수평으로 두 칸 이동 뒤 수직으로 한 칸
# 2. 수직으로 두 칸 이동 뒤 수평으로 한 칸
# 체스의 나이트가 위치가 주어졌을때 이동할 수 있는 경우의 수 출력하는 프로그램짜기
# 참고로 행이 숫자, 열이 알파벳
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

# input_data = a1 이라면 일단 의문이었다 보통 행열로해서 1a로 줄거같았는데. 열행으로해서 a1로 줬다.
# col에 대한 해석은 이러하다. 우리는 row에 맞춰서, a도 1이길 바란다.
# 아스키코드에서 a는 97이다. 그러므로 거기에서 a(97)을 한번더빼고 +1 을하면 1이되서
# 열 역시 a=1 로부터 시작할수있다.
# 참고로 아스키코드에서 소문자 a=97로 시작해서, z=122로 끝난다.

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)


# 이 코드를 적절히 수정하면 체스의 시스템을 만들 수 있다.
# 나에게 있어서 시사하는바가 상당히 큰 체스 프로그램이다.
