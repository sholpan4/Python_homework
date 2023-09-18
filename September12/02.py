import threading
import time

def my_func():
    print("Я засыпаю")
    time.sleep(3)
    print("Я проснулся")


my_thread = threading.Thread(target=my_func)
my_thread.start()

print("А это продолжается главный поток")

#my_thread.join()
print("Конец")