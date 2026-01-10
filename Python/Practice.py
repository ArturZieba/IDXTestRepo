class MyClass:
    def hello_world():
        print("Hello World 123")
    
    number = 456

def check_numbers(a, b):
    if (a > b):
        print(a, " is bigger.")
    elif (a < b):
        print(b, " is bigger.")
    else:
        print(a, " and ", b, " are equal.")

print(2 + 2)

MyClass.hello_world()

x = MyClass()

print(x.number)

check_numbers(2, 1)
check_numbers(3, 4)
check_numbers(5, 5)

letters = ["a", "b", "c", "d", "e", "f"]

for x in letters:
    print(x)
    if x == "c":
        break

for x in "abcdef":
    print(x)

i = 1
while i < 10:
    print(i)
    i += 1

try:
    print(abcd)
except:
    print("An exception occurred")