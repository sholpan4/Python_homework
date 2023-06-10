#task5
def get_volume(height, radian):
    pi = 3.14159
    return pi * radian ** 2 * height * 1000

height = float(input("Height of cylinder in meter: "))
radian = float(input("Radius of cylinder in meter: "))

volume = float(get_volume(height, radian))

print("Volume of cylinder is: %.2f liter." % volume)
