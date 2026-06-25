#import keyboard # Does not work, needs sudo - python -m pip install keyboard
from multiprocessing import Process # For Process()
#from pynput.keyboard import Key, Controller # python -m pip install pynput
    
def test():
    print("TestKeyboardInput")

#Does not work, keyboard requires root access, maybe a different way of doing this?
#process = Process(target=test())
#process.start()
#while process.is_alive():
#    if keyboard.is_pressed('q'):
#        process.terminate()
#        break

#keyboard = Controller()
#keyboard.type('Hello World')

test()

while True:
    print("1 ABC")
    print("2 DEF")
    print("3 GHI")

    testinput = input("Test: ")

    if testinput == "1":
        print("Option 1")
        break
    elif testinput == "2":
        print("Option 2")
        break
    elif testinput == "3":
        print("Option 3")
        break
    else:
        print("No option")

    #print("Test")