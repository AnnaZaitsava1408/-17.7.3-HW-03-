
def merge_twy_list(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
def merge_sort(array):
    if len(array) == 1:
        return array
    middle = len(array)//2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge_twy_list(left, right)

def binary_search(array, number, left, rigth):
    if left > rigth:
        return -1
    middle = (left + rigth)//2
    if array[middle] == number:
        return middle
    elif number < array[middle]:
        return binary_search(array, number, left, middle-1)
    else:
        return binary_search(array, number, middle + 1, rigth)

def showResult(arr,index, value):
    lessValueIndex = index
    while lessValueIndex > 0:
        if arr[lessValueIndex] < number:
            break
        lessValueIndex -= 1
    if arr[lessValueIndex] >= value and lessValueIndex >= 0 and index < len(arr):
        return f"Позиции меньше искомого значения нет\n Искомое значение на позиции {index}\n Следующее значение на позиции {index + 1}"
    if lessValueIndex >= 0 and index == len(arr):
        return f"Позиции меньше искомого значения {lessValueIndex}\n Искомое значение на позиции {index}\n Следующее значение на позиции нет"
    return f"Позиции меньше искомого значения {lessValueIndex}\n Искомое значение на позиции {index}\n Следующее значение на позиции {index + 1}"

try:
    array = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
    number = int(input('Введите любое число: '))
except (ValueError, TypeError) as error:
    print(error)
    print("Неправильный формат ввода")
else:
    sorted_arr = merge_sort(array)
    if min(sorted_arr) > number or number > max(sorted_arr):
         raise ValueError("Число вне диапазона")
    ind = binary_search(sorted_arr, number,0, len(sorted_arr)-1)
    print(sorted_arr)

    if ind != -1:
         res = showResult(sorted_arr, ind, number)
         print(res)
    else:
         print('Число не найдено!')
