def print_models(unprinted_designs, current_design):
    # Имитирует печать моделей,каждая модель перемещается в completed_models
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_designs)


def show_comleted_models(completed_models):
    # Выводит информацию обо всех начатых моделях
    print('\n The following models have been printed: ') 
    for completed_models in completed_models:
        print(completed_models)

unprinted_designs = []
completed_models = []


