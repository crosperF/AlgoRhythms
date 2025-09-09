a = [20, 3, 1, 59]



def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        print(i)
        swaps = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps = True
        if not swaps:
            break
    return arr

print(bubble_sort(a))
