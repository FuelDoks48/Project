class Dog():
    def __init__(self, name, age):
        self.name = name.title()
        self.age = age

    def sit(self):
        print(f'{self.name},is now sitting.')
    
    def roll_over(self):
        print(f'{self.name}, is now rolled over!')

my_dog = Dog('wille', 23)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is year old {my_dog.age}.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 9)
print(f"\nMy dog's name is {your_dog.name}")
print(f"My dog is year old {your_dog.age}.")
your_dog.sit()
your_dog.roll_over()
