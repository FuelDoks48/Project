
"""Выведение обычной функции приветствия!"""
# def greet_user():
#     print('Hello!')
# greet_user()
# ________________________________________________________________________

"""Функция приветствия пользователя!"""

# def greet_user(username):
#     print(f"Hello {username.title()}!")
# greet_user('Jessie')

# ________________________________________________________________________

"""function massage"""

# def display_message(text_file):
#     print(f'Hello, my favorite {text_file.title()}, and good luck!')
# display_message("gteeting's guys")
# ________________________________________________________________________
"""function favorite of book"""


# def favorite_book(title):
#     print(f"One of my favorite books is {title.title()}")
# favorite_book("Alice in Wonderland")
# ________________________________________________________________________
"""Function of argument position"""


# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s name is {pet_name.title()}.")
# describe_pet('snake', 'Marlboro')
# ________________________________________________________________________




"""Multipule argument of position"""


# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s name is {pet_name.title()}.")
# describe_pet('snake', 'Marlboro')
# describe_pet("hamster", "Meet")

# ________________________________________________________________________

"""Named argument"""

# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}")
#     print(f"\nMy {animal_type}'s name is {pet_name.title()}.")
# describe_pet(animal_type = 'Snake', pet_name = 'Python')
# ________________________________________________________________________

"""default values"""

# def describe_pet(pet_name, animal_type='Snake'):
#     print(f"\nI have a {animal_type}")
#     print(f"\nMy {animal_type}'s, name is {pet_name.title()}.")
# describe_pet(pet_name = 'Python')