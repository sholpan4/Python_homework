
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]   
print("Monday")
user_in = input("Do you want to see next day? (Y=1 \ N=2)")
for day in range(len(week_days)):
    
        if user_in == 1:
            print (day)
            #continue
            user_in = input("Do you want to see next day? (Y \ N)")
            #continue
        elif user_in == 2:
              break
        
