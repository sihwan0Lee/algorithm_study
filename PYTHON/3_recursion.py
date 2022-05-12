# 재귀 함수는 왜 사용될까?

# 재귀함수에 대해 처음 접할 때 보통 팩토리얼로 많이 접근한다.
n = int(input())


def recur(n):
    if n <= 1:
        return 1
    return n * recur(n - 1)


print(recur(n))
"""
 위의 것이 팩토리얼이다. n! = n * (n -1) * (n - 2)...... * 1  {n=1 -> 1}

 사실 위의 것만 보면 굳이 for문으로 -1 감소시켜서 1까지 곱해버린 것으로 대체할 수 있는데 왜 굳이 
 저렇게 함수를 반복 호출 하냐는 의문이 생긴다

 재귀함수, 즉 함수를 반복해서 동작시켜야 할 상황이 무엇이 있을까

 재귀함수 
 장점 : 상대적으로 간결하게 코드를 짤 수 있다. (변수 사용을 상대적으로 줄일 수 있다.)
 단점 : 메모리를 많이 사용한다. 속도가 상대적으로 느리

 반복문
 장점 : 속도가 상대적으로 빠르다
 단점 : 상대적으로 복잡해질 수 있다. 
 """
