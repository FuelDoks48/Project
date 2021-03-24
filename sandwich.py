# Task 1


# def make_sandwich(*topings):
#     print(f'\nI Make your sandwich with a this topings: ')
#     for toping in topings:
#         print(f"- {toping}")

# make_sandwich("green paper", "tomato", "coconut", "chille paper")
# make_sandwich("green paper", "bread", "tomato", "milk", "bacon")
# _______________________________________________________________________


# Task 2

# def build_person(first_name, last_name, **person_info):
#     person_info["first"] = first_name
#     person_info['last'] = last_name 
#     return person_info

# user_build_person = build_person('Chezar', 'Aurelli', location="Rome", field="empreror", type_of_activity="warrior", mind="High")
# print(user_build_person)


# _______________________________________________________________________

# task 3

def make_car(name_car, name_model, **kwargs):
    full_make_car = f'{name_car}, {name_model}, \n{kwargs}'
    return full_make_car.title()

car = make_car("subaru", 'outback', top_rate='Low', color='blue', tow_package=True)
print(car)

