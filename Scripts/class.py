# let's define the class Bike
class Bike:

    def __init__(self, color, frame_material, size):
        self.color = color
        self.frame_material = frame_material
        self.size = size
    def brake(self):
        print("Braking!")

# let's create a couple of instances
red_bike = Bike('Red', 'Carbon fiber', '18inch')
blue_bike = Bike('Blue', 'Steel', '24inch')

# let's inspect the objects we have, instances of the Bike class.

print(red_bike.color, '\n')  # prints: Red
print(red_bike.frame_material, '\n')  # prints: Carbon fiber
print(red_bike.size, '\n')
print(blue_bike.color, '\n')  # prints: Blue
print(blue_bike.frame_material, '\n')  # prints: Steel
print(blue_bike.size, '\n')
# let's brake!
red_bike.brake()  # prints: Braking!
