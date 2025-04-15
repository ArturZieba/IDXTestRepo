import csv
import json
import package_test.mymodule
from package_test.mymodule import my_variable_0, my_variable_1
import package_test.package_subdirectory_0
import random
from math import floor, ceil
import traceback
import os
import shutil
import subprocess
import multiprocessing
import threading
import time

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

sample_dictionary = { 
    'key0': 'pair0',
    'key1': 'pair1' 
}
print(sample_dictionary['key1'])

del(sample_dictionary['key0'])
print(sample_dictionary)

print(sample_dictionary.get('key0'))

sample_dictionary['key1'] = 'pairchange'
print(sample_dictionary['key1'])

another_dictionary = {
    'sub_dictionary': {'sub_key0': True},
    'sub_list': [1, 2, 3]
}

print(another_dictionary)

list_of_keys = ['keya', 'keyb', 'keyc']

dictionary_from_keys = dict.fromkeys(list_of_keys, 'Default')
print(dictionary_from_keys)

jsonstring = '{ "name": "bob", "age": 50, "married": false}'
print(json.loads(jsonstring))

print('sub_key0' in another_dictionary)
print('sub_key0' not in another_dictionary)
print(len(another_dictionary))

dictionary_keys = another_dictionary.keys()
dictionary_values = another_dictionary.values()
another_dictionary['hello'] = 'world'
print(dictionary_keys)
print(dictionary_values)

for key in dictionary_keys:
    print(key)

for key, value in another_dictionary.items():
    print(key, ':', value)

merged_dictionary = another_dictionary | sample_dictionary
print(merged_dictionary)

print(merged_dictionary == another_dictionary)

print('========\n')

try:
    print(2/0)
except ZeroDivisionError:
    print('Cannot divide by zero')

try:
    with open("nonexistent.txt", 'r') as f:
        f.write("Hello, World!")
except IOError as e:
    print("An error occured:", e)

try:
    f = open("idxtestrepo/Python/existent.txt", 'r')
    f.write("Hello, World!")
except IOError as e:
    print("An error occured:", e)
finally:
    print("Closing the file")
    f.close()

sample_user_json = '{"name": "Bob", "age": 21}'
sample_user = json.loads(sample_user_json)

try:
    print(sample_user['name'])
    print(sample_user['age'])
    print(sample_user['phone number'])
except KeyError as e:
    print("There are missing fields in the user object: ", e)

class CustomException(Exception):
    pass

def fetch(user_id):
    user = None

    if user == None:
        raise CustomException(f'{user_id} is not in database')
    else:
        return user

custom_users = [321, 456, 987]
for user_id in custom_users:
    try:
        fetch(user_id)
    except CustomException as e:
        print("An exception was caught: ", e)
        traceback.print_exc()

print('========\n')

def print_argument(func):
    def wrapper(a_value):
        print("Argument for", func.__name__, "is", a_value)
        return func(a_value)
    return wrapper

@print_argument
def add_one(x):
    return x + 1

print(add_one(3))

add_two = lambda x: x + 2

print(add_two(5))

list_for_lambda = [2, 4, 8, 16]
multiply_by_two = map(lambda x: x * 2, list_for_lambda)
print(list(multiply_by_two))

print('========\n')

print([x for x in range(1,10) if x % 2 == 0])

print([x + 4 for x in [1, 4, 7, 14, 20]])

def function_for_list_comprehension(i):
    return (i + 10) / 2

print([function_for_list_comprehension(x) for x in range(8)])

print([[[j for j in range(3)]] for i in range(4)])

print({s for s in range(1,5) if s % 2})

print({x: x * 2 for x in (2, 4, 6)})

print('========\n')

some_iterable = range(1, 3)
some_iterator = some_iterable.__iter__()
print(some_iterator.__next__())
print(some_iterator.__next__())
# print(some_iterator.__next__())

string_a = 'XYZ'
for letter in string_a:
    print(letter)

list_a = ['X', 'Y', 'Z']
for letter in list_a:
    print(letter)

print([x for x in [4, 3, 2, 1] if x > 2])

dictionary_a = {'name': 'Bob', 'phone number': 123654789, 'mail': 'mymail@mails.com'}
for key in dictionary_a:
    print(key)

for value in dictionary_a.values():
    print(value)

for key, value in dictionary_a.items():
    print(key, value)

class EvenNumbers:
    last = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.last += 2

        if self.last > 8:
            raise StopIteration

        return self.last

even_numbers = EvenNumbers()

for num in even_numbers:
    print(num)

print('========\n')

for i in range(5):
    print(i)

for i in range(3, 6):
    print(i)

for i in range(2, 32, 4):
    print(i)

for i in range(3, 0, -1):
    print(i)

sample_range = range(0, 3)
sample_iterator = iter(sample_range)

print(next(sample_iterator))
print(next(sample_iterator))
print(next(sample_iterator))
# print(next(sample_iterator))

list_for_range = list(range(2, 5))
print(list_for_range)

number_to_find = 3
print(number_to_find in range(0, 6))

print(range(0, 7)[2 : 4])
print(range(0, 10)[4 : 2 : -1])
print(range(0, 15)[2 : 8 : 2])

print(range(0, 5) == range(2, 5))
print(range(0) == range(4, 0))

print('========\n')

class MyDocumentedClass:
    """This class is documented"""

    def hi(self):
        """This function is documented"""
        pass

# help(MyDocumentedClass)
# help(print)
# help(str)

print('========\n')

# All of these fail to run without pass because they have no other code
def empty_function():
    pass 

if True:
    pass
else: 
    pass

try:
    pass
except Exception:
    pass

class EmptyClass:
    pass

def ellipsis_function():
    ...

print('========\n')

with open('idxtestrepo/Python/test_file.txt', 'w') as test_file:
    for i in range(1, 5):
        test_file.write('Number: ' + str(i) + '\n')

with open('idxtestrepo/Python/test_file.txt', 'a') as test_file:
    for i in range(5, 8):
        test_file.write('Appended number: ' + str(i) + '\n')

with open('idxtestrepo/Python/test_file.txt', 'r') as test_file:
    for line in test_file:
        print(line)

with open('idxtestrepo/Python/test_file.txt', 'r') as test_file:
    lines_list = test_file.readlines()
    print(lines_list)

if os.path.isfile('idxtestrepo/Python/test_file.txt'):
    print("test_file.txt is available")

if os.path.isdir('idxtestrepo/Python/'):
    print("Python dir is available")

if not os.path.isdir('idxtestrepo/Python/testdir'):
    os.mkdir('idxtestrepo/Python/testdir')

# os.rename('idxtestrepo/Python/test_file.txt', 'idxtestrepo/Python/test_file_rename.txt')
# os.remove('idxtestrepo/Python/test_file_rename.txt')

shutil.move('idxtestrepo/Python/test_file.txt', 'idxtestrepo/Python/testdir/test_file.txt')
shutil.rmtree('idxtestrepo/Python/testdir')

print('========\n')

subprocess.run(['ls', '-al'])

code_for_python_command = """
    for i in range (1, 3):
        print(f"Hello, World! {i})
"""

python_version_result = subprocess.run(['python3'], input=code_for_python_command, capture_output=True, encoding='UTF-8')
print(python_version_result)

shell_command_result = subprocess.run(['ls -al | head -n 1'], shell=True, capture_output=True, encoding='UTF-8')
print(shell_command_result)

print('========\n')

# python -m venv idxtestrepo/Python/venv
# source idxtestrepo/Python/venv/bin/activate
# deactivate
# rm -r idxtestrepo/Python/venv

print('========\n')

# pip help
# pip install simplejson
# pip freeze > idxtestrepo/Python/requirements.txt
# pip install -r idxtestrepo/Python/requirements.txt
# pip uninstall simplejson
# pip uninstall -r idxtestrepo/Python/requirements.txt

print('========\n')

# poetry --version
# /home/user/.local/bin/poetry

print('========\n')

def heavy(n, myid):
  for x in range(1, n):
    for y in range(1, n):
      x**y
  print(myid, "is done")

def sequential(n):
    for i in range(n):
        heavy(500, i)

# if __name__ == "__main__":
#     start = time.time()
#     sequential(80)
#     end = time.time()
#     print("Took: ", end - start)

print('========\n')

def threaded(n):
    threads = []

    for i in range(n):
        t = threading.Thread(target=heavy, args=(500,i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

# if __name__ == "__main__":
#     start = time.time()
#     threaded(80)
#     end = time.time()
#     print("Took: ", end - start)

def heavy_other(n, myid):
    time.sleep(2)
    print(myid, "is done")

def threaded_other(n):
    threads = []

    for i in range(n):
        t = threading.Thread(target=heavy_other, args=(500,i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

# if __name__ == "__main__":
#     start = time.time()
#     threaded_other(80)
#     end = time.time()
#     print("Took: ", end - start)

print('========\n')

def heavy_multi(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
        print(myid, "is done")

def multiproc(n):
    processes = []

    for i in range(n):
        p = multiprocessing.Process(target=heavy_multi, args=(500,i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

# if __name__ == "__main__":
#     start = time.time()
#     multiproc(80)
#     end = time.time()
#     print("Took: ", end - start)

def heavy_multi_pool(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
        print(myid, "is done")

def doit(n):
    heavy_multi_pool(500, n)

def pooled(n):
    with multiprocessing.Pool() as pool:
        pool.map(doit, range(n))

# if __name__ == "__main__":
#     start = time.time()
#     pooled(80)
#     end = time.time()
#     print("Took: ", end - start)

print('========\n')

json_sample_string = '{"name": "jason", "age": 45, "married": true}'
json_person_sample = json.loads(json_sample_string)

print(json_person_sample['name'], 'is', json_person_sample['age'], 'years old')
print(json_person_sample)
print(type(json_person_sample))

json_dump_to_string = json.dumps(json_person_sample, indent = 2)
print(json_dump_to_string)
print(type(json_dump_to_string))

with open('idxtestrepo/Python/data.json', 'w') as json_file:
    json.dump(json_person_sample, json_file)

with open('idxtestrepo/Python/data.json') as json_file:
    data = json.load(json_file)
    print('Reading', data)

print('========\n')

with open('idxtestrepo/Python/persons.csv', newline='') as f:
    csvfile = csv.reader(f)

    for row in csvfile:
        print(row)

with open('idxtestrepo/Python/output.csv', 'w') as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(["Name", "Age", "Country"])
    csv_writer.writerow(["Eliza", 25, "UK"])
    csv_writer.writerow(["Ferdinand", 35, "US"])

with open('idxtestrepo/Python/output.csv', 'a') as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(["Gabriel", 45, "FR"])
    csv_writer.writerow(["Harry", 55, "DK"])

my_dialect = csv.register_dialect("my_dialect",
    delimiter = ";",
    quotechar = '"',
    quoting = csv.QUOTE_MINIMAL
)

with open("idxtestrepo/Python/custom_dialect.csv", "w") as f:
    csv_writer = csv.writer(f, dialect = "my_dialect")

    csv_writer.writerow(["Name", "Age", "Country"])
    csv_writer.writerow(["Eliza", 25, "UK"])
    csv_writer.writerow(["Ferdinand", 35, "US"])

with open("idxtestrepo/Python/output.csv", "r") as f:
    csv_reader = csv.reader(f, dialect = "my_dialect")

    for row in csv_reader:
        print(row)

print('========\n')

# Check commit via idx