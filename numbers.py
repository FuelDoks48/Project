# for value in range(5):
#     print(value)


# rm_list = [1, 4, 6, 2, 5, 7, 2]

# def merge_sort(rm_list):
#     if len(rm_list) <= 1:
#         return rm_list
#     middle = len(rm_list) / 2

array = [33, 42, 9, 37, 8, 47, 5, 29]


def merge_sort(array,left_index,right_index):
    if left_index > right_index:
        return

# # Делим подмассивы пополам и сортируем их рекурсивно, пока не получим подмассивы, которые имеют только один элемент
#     middle = (left_index + right_index) // 2
#     merge_sort(array, left_index, middle)
#     merge_sort(array, middle + 1, right_index)
#     merge(array, left_index, right_index, middle)

# def merge(array, left_index, right_index, middle):
# # копии двух массивов
#     left_copy = array[left_index:middle + 1]
#     right_copy = array[middle:right_index + 1]

#     # начальные значения переменных,используемых для хранения
#     left_copy_index = 0
#     right_copy_index = 0
#     # Курсор где мы находимся в массиве
#     sorted_index = left_index

#     # Прохождение обоих копий, пока у нас не закончились элементы
#     while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

#         if left_copy[left_copy_index] < right_copy[right_copy_index]:
#             array[sorted_index] = left_copy[left_copy_index]
#             left_copy_index = left_copy_index + 1
#         else:
#             array[sorted_index] = right_copy[right_copy_index]
#             right_copy_index = right_copy_index + 1

#         sorted_index = sorted_index + 1

#         while left_copy_index < len(left_copy):
#             array[sorted_index] = left_copy[left_copy_index]
#             left_copy_index = left_copy_index + 1
#             sorted_index = sorted_index + 1

#         while right_copy_index < len(right_copy):
#             array[sorted_index] = right_copy[right_copy_index]
#             right_copy_index = right_copy_index + 1
#             sorted_index = sorted_index + 1

# merge_sort(array, 0, len(array) -1)
# print(array)

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длинна списков часто использкется,создаём переменные
    left_list_length, right_list_length = len(left_list), len(right_list)


    for x in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка 
            # Если первый элемент левого подсписка меньше,добавляем его в отсортированный массив 
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его в отсортированный массив
            else: 
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        # Если достигнут конец левого списка, элементы правого списка добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    # ВОзвращаем список если он состоит из одного элемента 
    if len(nums) <= 1:
        return nums
    # Для того что бы найти середину списка,используем деление без остатка
    # Индексы должны быть integer 
    mid = len(nums) // 2
    # Сортируем и обьеденяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    # Обьеденяем отсортированные списки в результирующий 
    return merge(right_list, left_list)

# Проверка кода.
random_list_num = [120, 45, 68, 250, 176]
random_list_num = merge_sort(random_list_num)
print(random_list_num)