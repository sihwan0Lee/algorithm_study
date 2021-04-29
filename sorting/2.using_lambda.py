# 성적 낮은순서로 학생을 출력하는데
# 포인트는 정렬에 람다 사용

n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
#(lambda x,y: x + y)(10, 20)
#(lambda x: x ** 2, range(5))

# # 또한 sorted(), sort()는 key 매개변수를 입력으로 받을수도 있다.
# key값으로는 하나의 함수가 들어가야 한다. 그리고 그것이 정렬 기준이 된다.

array = [("사과", 2), ("바나나", 7), ("딸기", 3)]


def setting(data):
    return data[1]


result = sorted(array, key=setting)
print(result)

# sorted(), sort() 는 key 매개변수를 입력으로 받을수 있다고 하였고, key값으로는 하나의 함수가 들어 가야한다고 했다.
# 그리고 그것이 정렬의 기준이 된다고 했다.
# lambda는 함수를 딱 한 줄만으로 만들게 해준다. 즉 함수다.
# key로 lambda 함수를 받는다는 소리이다.
