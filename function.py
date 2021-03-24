
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

"""function album"""

# def make_album(name_album, name_artist, collection_track=None):
#     full_name = {'album': name_album, 'artist': name_artist}
#     if collection_track:
#         full_name['collection track'] = collection_track
#     return full_name
# album = make_album('Rosehrot', 'Rummstain', '27')
# print(album)

# album = make_album('Slipknot', 'Slipknot', '16')
# print(album)

# album = make_album('System of a down', 'System of a down', '7')
# print(album)

# ________________________________________________________________________


"""function input album of user"""

# def make_album(name_album, name_artist, collection_track=None):
#     full_name = {'album': name_album, 'artist': name_artist}
#     if collection_track:
#         full_name['collection track'] = collection_track
#     return full_name
# ________________________________________________________________________

# List transfer


# def greet_users(names):
#     for name in names:                                 #выводит для каждего пользователя в списке сообщение
#         massage = f"Hello, {name.title()}!"   
#         print(massage)
# username = ['hannah', 'elizabeth', 'Gendalf']
# greet_users(username)

# ________________________________________________________________________


# without function


# unprinted_designs = ['phone case', 'robot pendant', 'demon cyber']
# completed_models = []

# while unprinted_designs:
#     current_designs = unprinted_designs.pop()
#     print(f'Printing model: {current_designs}')
#     completed_models.append(current_designs)

# print("\nThe following models have been printed: ") 
# for completed_models in completed_models:
#     print(completed_models)

# ________________________________________________________________________


# 3-D printing with use function 

# def print_models(unprinted_designs, current_design):
#     # Имитирует печать моделей,каждая модель перемещается в completed_models
#     while unprinted_designs:
#         current_designs = unprinted_designs.pop()
#         print(f'Printing model: {current_design}')
#         completed_models.append(current_designs)


# def show_comleted_models(completed_models):
#     # Выводит информацию обо всех начатых моделях
#     print('\n The following models have been printed: ') 
#     for completed_models in completed_models:
#         print(completed_models)

# unprinted_designs = ['phone', 'robot', 'spider-man']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_comleted_models(completed_models)

# ________________________________________________________________________

# writing massage's


# def print_massage(unprint_massage, current_massage):
#     while unprint_massage:
#          current_massage = unprint_massage.pop()
#          print(f'I print your massage: {current_massage}')
#          printing_massage.append(current_massage)

# def show_printing_massage(printing_massage):
#     print('\n The following massage have been complete print: ')
#     for printing_massage in printing_massage:
#         print(printing_massage)
# unprint_massage = ['Hello world', 'In your eyes', 'I love my marshmallow', 'you want buy flowers', 'star wars films now is so bad']
# printing_massage = [] 


# print_massage(unprint_massage, printing_massage)
# show_printing_massage(printing_massage)

# ________________________________________________________________________

# Перенос списка из одного в другой
# Transfer list


# def print_massage(unprint_massage, current_massage):
#     while unprint_massage:
#          current_massage = unprint_massage.pop()
#          print(f'I print your massage: {current_massage}')
#          printing_massage.append(current_massage)

# def show_printing_massage(printing_massage):
#     print('\n The following massage have been complete print: ')
#     for printing_massage in printing_massage:
#         print(printing_massage)


# def append_massage(another_list):
#     while printing_massage:
#         another_list = printing_massage.pop()
#         print(f'I pence your massage to another list: {another_list}')
#         sent_massage.append(another_list)





# unprint_massage = ['Hello world', 'In your eyes', 'I love my marshmallow', 'you want buy flowers', 'star wars films now is so bad']
# printing_massage = [] 
# sent_massage = []

# print_massage(unprint_massage, printing_massage)
# show_printing_massage(printing_massage)
# append_massage(sent_massage)




# ________________________________________________________________________


#Copy list without changes




# def print_massage(unprint_massage, current_massage):
#     while unprint_massage:
#          current_massage = unprint_massage.pop()
#          print(f'I print your massage: {current_massage}')
#          printing_massage.append(current_massage)

# def show_printing_massage(printing_massage):
#     print('\n The following massage have been complete print: ')
#     for printing_massage in printing_massage:
#         print(printing_massage)


# def append_massage(another_list):
#     while printing_massage:
#         another_list = printing_massage.pop()
#         print(f'I pence your massage to another list: {another_list}')
#         sent_massage.append(another_list)





# unprint_massage = ['Hello world', 'In your eyes', 'I love my marshmallow', 'you want buy flowers', 'star wars films now is so bad']
# printing_massage = [] 
# sent_massage = []

# print_massage(unprint_massage[:], printing_massage)
# show_printing_massage(printing_massage)
# append_massage(sent_massage)

# print(unprint_massage)

# ________________________________________________________________________
# tuple

# def make_pizza(*toppings):
#     print(toppings)

# make_pizza('green pepper') 

# ________________________________________________________________________

# Arbitrary argument set
# 
# def make_pizza(*toppings):
#     print('Making a pizza with the following toppings: ')
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('green pepper', "mushrooms")
# make_pizza('green pepper', "mushrooms", 'salt', 'oyster')

# ________________________________________________________________________

# Size pizza with arbitrary argument set

# def make_pizza(size, *toppings):
# 	print(f'\nMaking a {size}-inch  pizza with the following toppins')
# 	for topping in toppings:
# 	    print(f'- {topping}')


# make_pizza( 16, 'green pepper', "mushrooms")
# make_pizza(12, 'green pepper', "mushrooms", 'salt', 'oyster')

# ________________________________________________________________________

# Using arbitrary arguments in dictionary

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'enshtein', location='prinston', filed='physics')
# print(user_profile)

# ________________________________________________________________________
