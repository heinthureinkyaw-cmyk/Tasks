#task 1.1
def task1_1(string_value):
    h = 0
    for i in range(0,len(string_value)):
        value = 33* ord(string_value[i])
        h = h + value

    return h % 1024

print(task1_1("Hello"))
print(task1_1("Hallo"))
print(task1_1("Hullo"))



def task1_2(seed, string_value):
    combination = str(seed) + str(string_value)
    return task1_1(combination)

print(task1_2("seed-one", "Hello"))
print(task1_2("seed-two", "Hello"))
print(task1_2("seed-three", "Hello"))
