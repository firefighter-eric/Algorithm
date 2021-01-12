def count_inversion(array: list) -> int:
    l = len(array)
    if l == 1:
        return 0
    arr1 = array[:l // 2]
    arr2 = array[l // 2:]
    i1 = i2 = 0
    count = 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] <= arr2[i2]:
            i1 += 1
        else:
            print(arr1[i1], arr2[i2])
            count += 1
            i2 += 1
    for i in range(i2, len(arr2)):
        if arr2[i] < arr1[-1]:
            print(arr1[-1], arr2[i2])
            count += 1

    return count_inversion(arr1) + count_inversion(arr2) + count


if __name__ == '__main__':
    arr = [2, 3, 8, 6, 1]
    print(count_inversion(arr))
