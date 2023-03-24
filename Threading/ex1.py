import threading
import time



result = True


def counter(name):
    counter = 0
    time.sleep(5)
    while result:
        counter+=1
        print(f"{counter} - {name}")

threading.Thread(target=counter, args=("ABC",)).start()
threading.Thread(target=counter, args=("XYZ",)).start()

# counter()

input("Press enter to exit !!!!!!")

