def binary_search(arr, target) -> int:
    l, r = 0, len(arr) - 1

    while l <= r:
        # m = (l + r) // 2
        m = ((r - l) // 2) + l

        if arr[m] == target:
            return m

        if arr[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1


print(binary_search([1, 2, 3, 4, 5], 3), "== 2 ->", binary_search([1, 2, 3, 4, 5], 3) == 2)
print(binary_search([1, 2, 3, 4, 5], 1), "== 0 ->", binary_search([1, 2, 3, 4, 5], 1) == 0)
print(binary_search([1, 2, 3, 4, 5], 5), "== 4 ->", binary_search([1, 2, 3, 4, 5], 5) == 4)
print(binary_search([1, 2, 3, 4, 5], 6), "== -1 ->", binary_search([1, 2, 3, 4, 5], 6) == -1)
print(binary_search([5], 5), "== 0 ->", binary_search([5], 5) == 0)
print(binary_search([5], 7), "== -1 ->", binary_search([5], 7) == -1)
