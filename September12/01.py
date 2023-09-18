import threading
numbers = tuple(range(50))
result = 0
lock = threading.Lock()

def average(numb):
    sum = 0
    for x in numb:
        sum += x
    global result
    lock.acquire()
    result += sum/len(numb)
    lock.release()

thread1 = threading.Thread(target = average, args=( (numbers[:10]), ))
thread2 = threading.Thread(target = average, args=( (numbers[10:20]), ))
thread3 = threading.Thread(target = average, args=( (numbers[20:30]), ))
thread4 = threading.Thread(target = average, args=( (numbers[30:40]), ))
thread5 = threading.Thread(target = average, args=( (numbers[40:50]), ))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

result = result/5
print(result)

