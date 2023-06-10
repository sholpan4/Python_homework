#task8
def convert_to_time(sec):
    sec = sec % (24 * 3600)
    hours = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    
    print(hours, "hours in %d seconds" % sec)
    print(min, "minutes in %d seconds" % sec)
    return "%02d:%02d:%02d" % (hours, min, sec)

num = 10000
print("Time is: ", convert_to_time(num))
