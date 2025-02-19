# import selenium
import package_test.mymodule
from package_test.mymodule import my_variable_0, my_variable_1
import package_test.package_subdirectory_0
import random
from math import floor, ceil

print('Hello World 123')

addition = 2 + 2
print(addition)

subtraction = 2 - 2
print(subtraction)

multiplication = 2 * 2
print(multiplication)

division = 2 / 2
print(division)

modulo = 5 % 3
print(modulo)

floorDivision = 3 // 2
print(floorDivision)

exponent = 3 ** 2
print(exponent)

my_number = 123
print(type(my_number))

my_string = 'Hello World'
print(type(my_string))

combination = 'a' + ' test ' + 'string'
print(combination)

double_quote = "I'm Bob"
print(double_quote)

escape_char = 'He\'s Bob ' + "and \"he's Bob\""
print(escape_char)

multiline_string = """All
are
Bob"""
print(multiline_string)

newline_string = 'Line 1\nLine 2'
print(newline_string)

carriage_string = 'carry\ron'
print(carriage_string)

tab_string = 'tab\tstring\\'
print(tab_string)

print('========\n')

modified_string = 'Hello World\t 123'
print(modified_string.lower())
print(modified_string.upper())
print(len(modified_string))
print(modified_string.split(' '))
print(modified_string.split())
print(modified_string.replace('l', '*'))
print(modified_string.replace('Hello', 'Bye'))
print(modified_string[4] + modified_string[10])
print(modified_string[::-1].upper())

print('========\n')

my_money = 20
print(f'I have {my_money} money')

print('========\n')

boolean_test = True
if boolean_test:
    print('true')
else:
    print('false')

print('========\n')

print(2 > 1)
print(3 < 2)
print(4 <= 5)
print(6 == 6)
print(7 != 7)
print('h' == "i")
print("j" > 'k')

print('========\n')

print(True)
print(False)
print(not True)
print(not False)
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

print('========\n')

for letter in 'Hello World':
    print(letter)

my_list = [1, 'a', 'Hello 123']
print(my_list[2])
for item in my_list:
    print(item)

list_of_lists = [[2, 'c'], [3, 'd'], [4, 'e']]
print(list_of_lists[0][1])
print(list_of_lists[2][0])

i = 1
while i <= 4:
    print(i)
    i = i + 1

print('========\n')

def hi(name):
    if(name == ''):
        print('No name given')
    else:
        print('hi', name)

hi('Bob')

def hi_two_arguments(name0, name1):
    print('hi', name0, 'and', name1)

hi_two_arguments('Wilhelm', 'Gilbert')

def add(a, b):
    return a + b

result = add(4, 8)
print(result)

def omit_number(number):
    if number == 3:
        return
    
    print(number)

omit_number(1)
omit_number(2)
omit_number(3)
omit_number(4)

def default_arguments(value0 = 1, value1 = 3):
    print('Values are', value0, 'and', value1)

default_arguments()
default_arguments(5)
default_arguments(value1 = 7)
default_arguments(8,9)

print('========\n')

# while True:
#     input_name = input("Type in a name: ")
#     hi(input_name)

print('========\n')

print(dir(5))

print(type('a'))
print(type(1))
print(type(True))

class Vehicle:
    def __init__(self, speed = 0, started = False):
        self.speed = speed
        self.started = started
        print("Vehicle class init'ed")

    def start(self):
        self.started = True
        print("Starting. Is car running?", self.started)
    
    def stop(self):
        self.started = False
        print("Stopping. Is car running?", self.started)

    def current_speed(self):
        self.speed = 0
        print("Current speed:", self.speed)

    def speed_up(self, delta):
        self.speed += delta
        print("Speed after speeding up:", self.speed)

    def slow_down(self, delta):
        self.speed -= delta
        print("Speed after slowing down:", self.speed)


vehicle0 = Vehicle()
vehicle1 = Vehicle()

vehicle0.start()
vehicle0.stop()
vehicle0.current_speed()
vehicle0.speed_up(delta = 20)
vehicle0.slow_down(delta = 30)

print(id(vehicle0))
print(id(vehicle1))

print('========\n')

class Car(Vehicle):
    def __init__(self, trunk_open = False):
        self.trunk_open = trunk_open
        print("Car class init'ed")

    def open_trunk(self):
        self.trunk_open = True
        print('Opening trunk, is it open?', self.trunk_open)

    def close_trunk(self):
        self.trunk_open = False
        print('Closing trunk, is it open?', self.trunk_open)

car = Car()

car.start()
car.current_speed()
car.open_trunk()
car.close_trunk()

print('========\n')

class Motorcycle(Vehicle):
    def __init__(self, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__()
        print("Motorcycle class init'ed")
    
    def start(self):
        print('Starting the motorcycle')

motorcycle = Motorcycle()

motorcycle.start()
motorcycle.current_speed()

print('========\n')

package_test.mymodule.my_function()
print(my_variable_0, my_variable_1) # my_variable is imported via "from mymodule import my_variable_0, my_variable_1"

print('========\n')

print(int('123'))
print(int(1.23))
print(str(321))

print(random.randint(1, 10))

if isinstance(int('4'), int):
    print("Integer")

print(float(2.0))
print(float(2))
print(float('2'))

print(1.25e3)

print(round(1.5345))
print(round(1.5345, 2))
print(round(1.5345, 1))

print(floor(1.23))
print(ceil(1.23))

print(0.1 + 0.2)

print('========\n')

my_list = [1, "Hi", {'abc' : 'def'}]
empty_list = []

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

print(list(range(1, 7)))

list_of_lists = [[1, 2], [3, 4], [5, 6]]
print(list_of_lists[0])
print(list_of_lists[0][1])
print(list_of_lists[1][0])
print(list_of_lists[2][1])

my_list.append(4)
print(my_list)
my_list.append('ghi')
print(my_list)

list1 = [6, 5, 4]
list2 = [3, 2, 1]
list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)
print(list2)

list1.pop()
print(list1)
list1.pop(0)
print(list1)

# del list1
# print(list1)

list_remove = [1, 1 ,1, 2, 2, 3, 3, 3, 3]
list_remove.remove(1)
print(list_remove)
list_remove.remove(1)
print(list_remove)

list_remove.clear()
print(list_remove)

list_duplicates = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
print(list(set(list_duplicates)))
list_duplicates[2] = 222
print(list_duplicates)
print(len(list_duplicates))
print(list_duplicates.count(3))

if 1 in list_duplicates:
    print("It's in")

print(list_duplicates.index(4))

for i in list_duplicates:
    print(i)

string_from_list = str(list_duplicates)
print(string_from_list)

list_duplicates.sort()
print(list_duplicates)
list_duplicates.sort(reverse=True)
print(list_duplicates)

print(sorted(list_duplicates))
print(sorted(list_duplicates, reverse=True))

print(list_duplicates[5:])
print(list_duplicates[:2])
print(list_duplicates[::2])
print(list_duplicates[-1:-3:-1])

list_duplicates.reverse()
print(list_duplicates)
print(list_duplicates[::-1])

rev_list = reversed(list_duplicates)
for i in rev_list:
    print(i)

print('========\n')

tuple_numbers = (1, 2, 3)
print(tuple_numbers)
tuple_no_par = 1, 2, 3
print(tuple_no_par)
tuple_mix = (True, 2, 'Three')
print(tuple_mix)

list_for_tuple0 = [0, 1, 2]
list_for_tuple1 = [3, 4, 5]
tuple_from_lists = (*list_for_tuple0, *list_for_tuple1) # * unpacks lists into individual elements
print(tuple_from_lists)
print(tuple_from_lists[2])
print(tuple_from_lists[4])
print(len(tuple_from_lists))

print(list(tuple_from_lists))
print(set(tuple_from_lists))
print(str(tuple_from_lists))

print('========\n')

my_set = {"hi", "there", "world"}
print(my_set)
my_mixed_set = {1, "two", (3, 4)}
print(my_mixed_set)

another_set = set()
print(another_set)
another_set.add(1)
print(another_set)
another_set.add("oi")
print(another_set)
another_set.add((4, 6))
print(another_set)
another_set.update([8, 9, 10])
print(another_set)

deduplicate_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5]
deduplicate_set = set(deduplicate_list)
print(deduplicate_set)

list_from_set = list(deduplicate_set)
print(list_from_set)

set_A = {1, 2, 3, 4, 5}
set_B = {3, 4, 5, 6, 7}
print(set_A - set_B)
print(set_B - set_A)
print(set_A ^ set_B)
print(set_A & set_B)

set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
set_3 = {1, 2, 3, 10}
print(set_1 < set_2)
print(set_3 < set_2)
print(set_2 > set_1)
print(set_2 > set_3)
print(set_1 < set_1)
print(set_1 <= set_1)
print(set_1 >= set_1)

print(set_1 | set_2 | set_3)

set_1.pop()
print(set_1)
set_1.pop()
print(set_1)
set_1.pop()
print(set_1)
set_2.clear()
print(set_2)
set_3.remove(10)
print(set_3)

print('========\n')