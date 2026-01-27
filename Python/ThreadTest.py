import threading # For threading.Thread()
import time # For time.sleep()

def thread_function(name):
    print(f"Thread {name}: starting")
    time.sleep(2)
    print(f"Thread {name}: finishing")

if __name__ == "__main__":
    print("Main before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    print("Main before starting thread")
    x.start()
    print("Main waiting for the thread to finish")
    print("Main done")