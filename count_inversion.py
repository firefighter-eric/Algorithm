def merge(arr1: list, arr2: list) -> (int, list):
    """count inversions between arrays and merge sorted arrays

    Args:
        arr1 (list): array 1
        arr2 (list): array 2

    Returns:
        int, list: inversions, merged array
    """
    arr = []
    i1 = i2 = 0
    count = 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] <= arr2[i2]:
            arr.append(arr1[i1])
            i1 += 1
        else:
            arr.append(arr2[i2])
            i2 += 1
            count += len(arr1) - i1
    arr += arr1[i1:]
    arr += arr2[i2:]
    return count, arr

def count_inversion(array: list) -> (int, list):
    l = len(array)
    if l == 1:
        return 0, array

    count1, arr1 = count_inversion(array[:l // 2])
    count2, arr2 = count_inversion(array[l // 2:])
    count12, arr  = merge(arr1, arr2)

    return count1 + count2 + count12, arr


if __name__ == '__main__':
    arr = [2, 3, 8, 6, 1]
    print(count_inversion(arr))
