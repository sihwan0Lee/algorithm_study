#위클리 챌린지  1주차_부족한 금액 계산하기

def solution(price, money, count):
    answer = (money - (price * (count * (count+1)//2)))
    if answer > 0:
        return 0
    else:
        return abs(answer)



print(solution(3, 20, 4))

# 문제를 잘 읽어야한다. 결국 돈이 0이상 즉 돈이 남거나 딱 떨어지면 0이랬지 0 일떄만 0 리턴 하라고는 안했음.