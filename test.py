def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# ans = bubble_sort([12, 8, 31, 1, 47])
# print(ans)


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        smallest = i

        for j in range(i, n):
            if arr[smallest] > arr[j]:
                smallest = j

        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]

    return arr


# ans = selection_sort([12, 8, 31, 1, 47])
# print(ans)


def insertion_sort(arr):
    n = len(arr)
    
    for i in range(n):
        j = i
        val = arr[j]
    
        while j > 0 and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = val
    return arr

# ans = insertion_sort([12, 8, 31, 1, 47])
# print(ans)