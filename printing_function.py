def print_models(unprinted_designs, completed_models):
    # Имитирует печать моделей,каждая модель перемещается в completed_models
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f'Printing model: {current_designs}')
        completed_models.append(current_designs)


def show_comleted_models(completed_models):
    # Выводит информацию обо всех начатых моделях
    print('\n The following models have been printed: ') 
    for completed_model in completed_models:
        print(completed_model)
