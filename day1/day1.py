def fuel(mass):
    return int(mass//3-2)

def fuel2(mass):
    b = 0
    y = fuel(mass)
    while(y > 0):
        b += y
        y = fuel(y)
    return b

y = 0
with open('input1.txt') as _file:
        data = _file.read().split()
        for i in range(100):
            x = int(data[i])          
            a = fuel2(x)
            y = y + a
        print(y)