import threading

my_lock = threading.Lock()
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def my_func():
    global numbers
    for j in range(100000):
        my_lock.acquire()
        for i in range(len(numbers)):
            if i == len(numbers) - 1:
                numbers[i] += numbers[i] - numbers[i-1]+1

            else:
                numbers[i] += numbers[i+1] - numbers[i]
        my_lock.release()

thread_1 = threading.Thread(target = my_func)
thread_2 = threading.Thread(target = my_func)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(numbers)