# 제곱근 함수가 있겠지 파이썬이니까, 근데 그걸 쓰면 무슨 의미가 있는가?
# 자 드가자

#_list = []
#x = 1
#for i in range(5):
#    a = int(input())
#    x *= a
#    _list.append(x)


def answer(_list):
    answer = 0
    for i in _list:
        for j in range(1, i + 1):
            if j * j == i:
                answer += 1
    if answer > 0:
        T = "found"
        return T
    else:
        F = "not found"
        return F
            
print(answer([5, 5, 10, 30, 30]))
                

