
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

# ________________________________________________________________________

"""exercise in function""" 

# def make_shirts(size, text_make):
#     print(f"\nMake has size: {size} ")
#     print(f"And text on it '{text_make}'")
# make_shirts('M', 'Slipknot')
# ________________________________________________________________________

"""Big make Shirts"""

# def make_shirts(size = 'L', text_make = 'I love Python'):
#     print(f"\nMake has size: {size} ")
#     print(f"And text on it '{text_make}'")
# make_shirts()
# ________________________________________________________________________

"""coming back to simple meaning""" 

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musicians = get_formatted_name('jimi', 'hendrix')
# print(musicians)

# ________________________________________________________________________

"""Non-binding """

# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {last_name} {middle_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musicians = get_formatted_name('john', 'lee', 'hooker')
# print(musicians)

# musicians = get_formatted_name('jimi', 'hendrix')
# print(musicians)


# ________________________________________________________________________

"""dictionary return"""

# def build_person (first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person

# musicians = build_person('jimi', 'hendrix')
# print(musicians)

# ________________________________________________________________________

"""expansion of function"""


# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musicians = build_person('jimi', 'hendrix', age=27)
# print(musicians)
# ________________________________________________________________________
"""function country"""

# def city_country(name_city, name_country):
#     full_name = f"{name_city} {name_country}"
#     return full_name.title()

# nation = city_country('Moscow', 'Russia')
# print(nation)
# ________________________________________________________________________

