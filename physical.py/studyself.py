class Example_one:
    def func1():
        print("this is 1")

    def func2(self):
        print("this is 2")


#a = Example_one()
# print(a.func1())
# TypeError: func1() takes 0 positional arguments but 1 was given
# print(a.func2())
# this is 2

# func2의 첫 번째 인자인 self 는 호출할 때는 아무것도 전달하지 않는 이유는 파이썬이 자동으로 넘겨주기 떄문이다.
# 자동으로  왜 넘겨주는지 이해가 잘 가는가?
# func1 의 오류의 의미는 인자가 없지만 하나의 인자를 받아서 발생하는 오류이다.


class Ex_second:
    def func1():
        print("this is 1")

    def func2(self):
        print(id(self))
        print("this is two")


#b = Ex_second()
# print(id(b))
# 140538517261088
# print(b.func2())
# 140538517261088
# this is two

# 클래스 내에 정의된 self는 클래스 인스턴스임을 알 수 있다.

# print(Ex_second.func1())
# this is 1
#self가 없는 것은 앞의 것(인스턴스.메서드) 형식이 아닌 클래스명.메서드()형태로 호출하였다.#
# 반면 self 인자를 전달받는 func2의 경우 이렇게 불러낸다면
# print(Ex_second.func2())
# TypeError: func2() missing 1 required positional argument: 'self'
# 라는 오류가 뜬다.

# 메서드의 self로 전달되는 것은 인스턴스 자체이다. 따라서 클래스에 대한 인스턴스를 생성한 후 해당 인스턴스를 전달해야하는 것이다.

# 이 두개의 방식차이에는 아무런 차이가 없다. 보통은 인스턴스.메서드() 를 많이 쓴다.
# 쉽게 말해 파이썬은 클래스의 메소드를 정의할때 self를 명시하고, 메소드를 불러올때 self를 사용함으로서 클래스내에 정의한 멤버에 접근할수있게 되는것이다.

# __init__ 의 경우에는 파이썬에서 클래스의 생성자를 만들 때 항상 동일한 규칙이다.
# 클래스명을 쓰고 옆에 바로 인자들을 채워 넣음으로 써 그 값들을 지닌 객체를 만들어 낼수 있게 된다.

# ex


class Student:
    name = ''
    kor = 0
    eng = 0
    math = 0

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def say_hello(self):
        return '안녕하세요 {}님'.format(self.name)

    def average(self):
        return (self.kor + self.eng + self.math) / 3


# 이 클래스를 해석해보자면
# 학생 student 라는 틀을 만들 것이다. 이 클래스에는 이름,국어,영어,수학 의 점수 값을 받을 수 있다.
# 이용자는 생성자를 통해서 아무개, 국어점수, 영어점수, 수학점수 순으로 인자를 넣어서 결과를 만들것이다.
# say_hello 라는 함수는 '안녕하세요 (아무개self)님'이라고 인사하는 함수야
# average 함수는 self(아무개의) 국어 점수 영어점수 수학점수를 더하고 3으로 나눈 값을 돌려주는거야
#self를 통해 설명을해줬으니 뒤에 인자를 넣어서 직접 값을 만들어봐.#
# 라는 뜻을 컴퓨터에게 전달해준것이고
# 사용자인 우리는 그저
st1 = Student('리', 80, 80, 80)
print(st1.math)
print(st1.average())
