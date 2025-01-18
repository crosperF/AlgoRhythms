def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        swaps = False
        for i in range(n):
            if arr[i] > arr[i + 1]:
                swaps = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        if swaps == False:
            break

    return arr


test_cases = [
    ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([42], [42]),
    ([], []),
    ([-5, -2, -9, 1, 0], [-9, -5, -2, 0, 1]),
]

for idx, (arr, expected) in enumerate(test_cases):
    result = bubble_sort(arr)
    print(f"Test case {idx + 1}: {'Passed' if result == expected else 'Failed'}")
