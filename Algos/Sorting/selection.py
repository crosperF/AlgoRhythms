
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        if min_idx != i:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]

    return arr

res = selection_sort([18, 39, 41, 2, 90, 1])
print(res)
