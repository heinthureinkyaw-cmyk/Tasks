# task 2.1
import random

def task2_1(filename, quantity, maximum):
    with open(filename , 'w') as file:
        for i in range(quantity):
            value = random.randint(0 , maximum)
            value = str(value)
            file.write(value + '\n')


#task2_1("randomnumbers.txt", 1000 , 5000)




#task 2.2
def task2_2(list_of_integers):
    if len(list_of_integers) == 1:
        return list_of_integers

    mid = len(list_of_integers) // 2
    left = task2_2(list_of_integers[:mid])
    right = task2_2(list_of_integers[mid:])

    sorted_list = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))

    sorted_list += left
    sorted_list += right
    return sorted_list



#print(task2_2([56,25,4,98,0,18,4,5,7,0]) == [0,0,4,4,5,7,18,25,56,98])




#task 2.3


def task2_3(filename_in, filename_out):
    with open(filename_in, 'r') as file:
        numbers = []
        for line in file:
            num = line.strip()
            numbers.append(int(num))
    sorted_numbers = task2_2(numbers)

    with open(filename_out, 'w') as file:
        for numbers in sorted_numbers:
            file.write(str(numbers) + '\n')


task2_3("randomnumbers.txt", "sorted_numbers.txt")
