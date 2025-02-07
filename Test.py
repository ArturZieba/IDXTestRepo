# import selenium

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

class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True
        print("Is car started?", self.started)
    
    def stop(self):
        self.started = False
        print("Is car started?", self.started)

    def speed(self):
        self.speed = 0
        print("Speed:", self.speed)

    def speed_up(self, delta):
        self.speed += delta
        print("Speed:", self.speed)

    def slow_down(self, delta):
        self.speed -= delta
        print("Speed:", self.speed)


car0 = Car()
car1 = Car()

car0.start()
car0.stop()
car0.speed()
car0.speed_up(delta = 20)
car0.slow_down(delta = 30)

print(id(car0))
print(id(car1))

print('========\n')