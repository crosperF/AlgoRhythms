a = [20, 3, 1, 59]



def bubble_sort(arr):
    for i in range(len(arr), -1, -1):
        for j in range(i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print(bubble_sort(a))
