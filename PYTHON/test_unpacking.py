# unpacking
def sum(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
#sum(numbers) # error

print(sum(*numbers)) # 출력 : 

# 위치인자를 unpacking할때는 위에 예에서는 list타입이였지만, Container객체라면 다 가능합니다.

print(sum(*'abc')) # 'abc'
print(sum(*(4, 5, 6))) # 15
print(sum(*{'가', '나', '다'})) # '나다가'
print(sum(*{'치킨': 3, '피자': 12, '음료수': 10})) # '치킨피자음료수'

#동일한 방식으로 키워드인자로 unpacking할 수 있습니다. unpacking하기 위해선 인자가 key와 인자로 구성되어 있는 mapping타입, 즉 dict가 필요합니다.

def cal(first, op, second):
    if op == '+':
        return first + second
    if op == '/':
        return first / second
    if op == '-':
        return first - second
    if op == '*':
        return first * second

prob = {
  'first': 12,
  'second': 34,
  'op': '*'
}

cal(**prob) # 결과 : 408