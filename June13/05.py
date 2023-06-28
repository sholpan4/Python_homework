class Avatar:
    name = " "
    gender = " "
    age = 0
    guild_list = ["Immortals", "Guardians", "Knights", "Phoenix"]
    transport_list = ["car", "bicycle", "truck"]
    gun = " "
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
       
    def __repr__(self) -> str:
        msg = "Avatar name: %s, guild: %s" % (self.name, self.gender)
        return msg 
    
    def get_age(self, age):
        self.age = int(input("Your age:"))
        if self.age < 21:
            print("Warning! You age is not allowed to play games.!")
            
    
    def choose_guild(self, guild_list = 0):
        print(self.guild_list)
        a = input("Choose guild: ")
        if a == "Immortals":
            a = self.guild_list[0]
            print("Welcome to the 'Immortals' guild!")
        elif a == "Guardians":
            a = self.guild_list[1]
            print("Welcome to the 'Guardians' guild!")
        elif a == "Knights":
            a = self.guild_list[2]
            print("Welcome to the 'Knights' guild!")
        elif a == "Phoenix":
            a = self.guild_list[3]
            print("Welcome to the 'Phoenix' guild!")
            
    def choose_transport(self, transport_list = 0):
        print(self.transport_list)
        a = input("Choose transport: ")       
        if a == "car":
            a = self.guild_list[0]
            print("You can reach your destination by car in 200km/h")
        elif a == "bicycle":
            a = self.guild_list[1]
            print("You can reach your destination by bicycle in 200km/h")
        elif a == "truck":
            a = self.guild_list[2]
            print("You can reach your destination by truck in 90km/h")

    def shoot(self, gun = 0):
        answer = input("Would you like to have a gun? ")
        if answer == "yes":
            print("Now you can shoot, but be careful!")
        else:
            print("Ok 😄")
                      
gamer1 = Avatar("Noa", "male")
print(gamer1)
gamer1.get_age(0)
print(gamer1)

gamer2 = Avatar("Maya", "female")
print(gamer2)
gamer2.get_age(0)
gamer2.shoot()