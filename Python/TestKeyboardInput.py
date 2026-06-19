#import keyboard # Does not work, needs sudo
    
def test():
    print("TestKeyboardInput")

#Does not work, keyboard requires root access, maybe a different way of doing this?
#process = Process(target=test())
#process.start()
#while process.is_alive():
#    if keyboard.is_pressed('q'):
#        process.terminate()
#        break

test()