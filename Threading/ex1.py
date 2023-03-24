import threading
import time



result = True


def counter():
    counter = 0
    time.sleep(1)
    while result:
        counter+=1
        print(counter)

counter()

input("Press enter to exit !!!!!!")

