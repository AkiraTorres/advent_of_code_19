with open('input2.txt') as _file:
    str_array = _file.read().split(",")
    int_array = [int(i) for i in str_array] 

noun1 = 12
verb2 = 2
noun = 80
verb = 18
date = 19690720

def gravity(int_array):
    global noun
    global verb
    int_array[1] = noun
    int_array[2] = verb
    opa = int_array[0]
    x = 3
    y = 2
    z = 1
    a = 0
    while (opa != 99):
        if opa == 1:
            int_array[int_array[x]] = int_array[int_array[z]] + int_array[int_array[y]]
        elif opa == 2:
            int_array[int_array[x]] = int_array[int_array[z]] * int_array[int_array[y]]
        x += 4
        y += 4
        z += 4
        a += 4
        opa = int_array[a]
    return int_array[0]

print(gravity(int_array))
out = (100*noun) + verb
print(out)
