def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr



def insertion_sort_2 (arr):
    for i in range(1, len(arr)):
        j = i
        val = arr[j]
        idx_to_swap = j
        while True:
            if j == 0 or arr[j - 1] < val:
                idx_to_swap = j - 1
                break
            j -= 1
        arr[idx_to_swap], arr[j] = arr[j], arr[idx_to_swap]
    return arr

a = [12, 8, 4, 1]
res = insertion_sort_2(a)
print(res)
insertion_sort(a)
