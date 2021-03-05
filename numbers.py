for value in range(5):
    print(value)

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

#     # Длинна списков часто использкется,создаём переменные
    left_list_length, right_list_length = len(left_list), len(right_list)


    for x in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
#             # Сравниваем первые элементы в начале каждого списка 
#             # Если первый элемент левого подсписка меньше,добавляем его в отсортированный массив 
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
#             # Если первый элемент правого подсписка меньше, добавляем его в отсортированный массив
            else: 
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
#         # Если достигнут конец левого списка, элементы правого списка добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
#         # Если достигнут конец правого списка, элементы левого списка добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
#     # ВОзвращаем список если он состоит из одного элемента 
    if len(nums) <= 1:
        return nums
#     # Для того что бы найти середину списка,используем деление без остатка
#     # Индексы должны быть integer 
    mid = len(nums) // 2
#     # Сортируем и обьеденяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
#     # Обьеденяем отсортированные списки в результирующий 
    return merge(right_list, left_list)

# # Проверка кода.
random_list_num = [120, 45, 68, 250, 176]
random_list_num = merge_sort(random_list_num)
print(random_list_num)

# ___________________________________________________________________________________

# Стандартная сортировка

st_sort = [1, 2, 3, 2, 3, 5, 1, 2]
st_sort = sorted(st_sort)
print(st_sort)
# ___________________________________________________________________________________

# Сортируем кортеж(неизменяемый список  tuple)

tuple_list = ('zane', 'bob', 'fred')
tuple_list = sorted(tuple_list)
print(tuple_list)
# ___________________________________________________________________________________
# Сортировка словаря

vocab = {1:'a', 8:'b', 7:'t', 6:'z'}
vocab = sorted(vocab)
print(vocab)
# ___________________________________________________________________________________
# 
# Сортировка сложных структур с использованием ключа

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
#   Функция __repr__ является специальной функцией,которая используется для переопределения того,как объект будет представлен в интерпретаторе
    # def __repr__(self):
        # return str(self.age)
    def __repr__(self):
        return self.name
jack = Person('Jack', 19)
adam = Person('Adam',23)
becky = Person('Becky', 22)
# Сделаем переменную которая отправит все три переменные в список.
people = [jack, adam, becky]


# Функция отвечающая по какому параметру будет произведена сортировка
def byName_key(Person):
    return Person.name
# def byName_key_2(Person):
#     return Person.name
a = sorted(people, key=byName_key)
# b = sorted(people, key=byName_key_2)
print(a)

# ___________________________________________________________________________________


