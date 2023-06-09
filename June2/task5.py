def get_volume(height, radian):
    pi=3.14159
    return pi * radian ** 2 * height

height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))

volume = get_volume
print("Volume is: ", volume)
