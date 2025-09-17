def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


def insertion_sort_2(arr):
    for i in range(1, len(arr)):
        val = arr[i]

        j = i
        while j - 1 >= 0 and val < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val
    return arr


a = [12, 8, 4, 1]
res = insertion_sort_2(a)
print(res)
insertion_sort(a)
