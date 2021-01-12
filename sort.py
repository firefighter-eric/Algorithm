def merge(arr1: list, arr2: list) -> list:
    arr = []
    i1 = i2 = 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] <= arr2[i2]:
            arr.append(arr1[i1])
            i1 += 1
        else:
            arr.append(arr2[i2])
            i2 += 1
    arr += arr1[i1:]
    arr += arr2[i2:]
    return arr


def merge_sort(array) -> list:
    l = len(array)
    if l == 0 or l == 1:
        return array
    return merge(merge_sort(array[:l//2]), merge_sort(array[l//2:]))


if __name__ == '__main__':
    array = [2, 3, 45, 653, 26, 2, 4, 6, 7]
    print(merge_sort(array))
