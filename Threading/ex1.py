import threading
import time



done = False


def counter(name):
    counter = 0
    # time.sleep(5)
    while  counter<10:
        counter+=1
        print(f"{counter} - {name}")

threading.Thread(target=counter,args=("ABC",), daemon=True).start()
threading.Thread(target=counter,args=("XYZ",), daemon=False).start()

# counter()

print("It isthe terminating statement.")

'''
When daemon is set to True, the thread terminates as soon as the main thread is completed
'''

