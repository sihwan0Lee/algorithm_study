# graph

# 탐색
# 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정.
# DFS, BFS가 대표적인 탐색 알고리즘이다.

# 스택 , 큐
# 스택과 큐는 push(삽입),pop(삭제) 이 두가지의 핵심적인 함수로 구성된다.
# 그리고 오버플로와 언더플로를 따져야한다.
# Overflow : 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 "삽입" 연산을 수행할 떄 발생한다.
# 즉 저장 공간을 벗어나 데이터가 넘쳐흐를 때 발생한다.
# Underflow : 특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 "삭제" 연산을 수행하면 데이터가 전혀 없는 상태에서 발생한다.

# 스택
# First In Last Out
# 파이썬에선 append(), pop() 을 이용해 간단히 스택을 표현할수 있다.
# append()는 뒤에 새로운 것을 추가하고, pop()은 인덱스를 지정해주지 않은 이상 가장 뒤에 것을 삭제 하기 때문이다.
# 5(1st.in)->3(2nd.in)->1(3rd.in)
# 5(1st.in)->3(2nd.in)->(1.out)
# 5(1st.in)->3(2.out)
# 5(3rd.out)

# 큐
# First In First Out
# 5(1st.in)
# 3(2nd.in)->5(1st.in)
# 1(3rd.in)->3(2nd.in)->5(1st.in)
# 1(3rd.in)->3(2nd.in) (5.out: first)
# 1(3rd.in)  (3.out: second)
# 파이썬으로 큐를 구현할 때에는 collections 모듈에서 제공하는 deque 자료구조를 활용하면 된다.
from collections import deque

queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(1)
print(queue)
queue.popleft()
print(queue)
queue.reverse()
print(queue)


# 재귀 함수 Recursive Function
# DFS, BFS의 구현을 위해 재귀함수를 능숙히 쓸줄 알아야한다.
# 재귀함수에는 꼭 종료 조건을 넣어줄것.
# 재귀 함수는 스택 자료구조를 이용한다. 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 , 그 앞의 이전 함수 호출이 종료되기 떄문이다.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


print(factorial(5))


# intro 끝 맺음
# 코딩 테스트 중 2차원 배열에서의 탐색 문제를 만나면 그래프 형태로 바꿔서 하면 풀이를 더 쉽게 떠올릴수 있을지도.
