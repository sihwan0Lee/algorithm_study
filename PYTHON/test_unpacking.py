# unpacking
def sum(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
#sum(numbers) # error

print(sum(*numbers)) # 출력 : 6