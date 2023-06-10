def get_time(hours, minutes, seconds):
    h = int(hours)
    min = int(minutes)
    sec = int(seconds)
    
    if hours == 0:
        message = "00:%02d:%02d" % min, sec
        return message
    
    elif minutes == 0:
        message = "%02d:00:%02d" % h, sec
        return message
    
    elif seconds == 0:
        message = "%02d:%02d:00" % h, min
        return message
    else:
        message = "%02d:%02d:%02d" % h, min, sec
        return message

# hours = int(input("Enter hours:"))
# minutes = int(input("Enter minutes:"))
# seconds = int(input("Enter seconds:"))

number = get_time(2, 0, 30)
print(number)