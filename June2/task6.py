#task6
hours = int(input("Enter hours:"))
minutes = int(input("Enter minutes:"))
seconds = int(input("Enter seconds:"))

def get_time(hours, minutes, seconds):
    if hours > 23:
        return "Please enter hours between 0 and 23."
    elif minutes > 59:
        return "Please enter minutes between 0 and 59."
    elif seconds > 59:
        return "Please enter seconds between 0 and 59"
    else:  
        return "%02d:%02d:%02d" % (hours, minutes, seconds)
  
message = get_time(hours, minutes, seconds)      
print(message)