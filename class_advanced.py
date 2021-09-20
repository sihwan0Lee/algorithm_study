#a = [3, 2, 1]
#b = [1, 2, 3]

# if a == b:
#    print("True")
# else:
#    print("False")

# 파이썬 심화
# 객체 지향 프로그래밍 (OOP) -> 코드의 재사용, 코드의 중복 방지 목적

# 클래스 상세 설명

class Student():
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._name, self._details)


student1 = Student('kim', 1, 1, {'gender': 'Male', 'score1': 95, 'score2': 98})
student2 = Student(
    'Lee', 2, 1, {'gender': 'Female', 'score1': 99, 'score2': 97})
print(student1.__dict__)

students_list = []
students_list.append(student1)
students_list.append(student2)

# 반복 (__str__)
for x in students_list:
    print(x)

# 파이썬의 모든 객체는 학생의 네임스페이스, 딕셔너리 기반의 네임스페이스의 속성값을 가지게 되어있다.
