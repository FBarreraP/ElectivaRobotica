def fibonacci(x):
    global data
    a = 1
    b = 1
    index = 0
    while index < x:
        data.append(a)
        temp = b
        b = a + b
        a = temp
        index += 1

data = []
fibonacci(12)
print(data)