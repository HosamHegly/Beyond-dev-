def merge(arr, left, mid, right):
    x = mid - left + 1  # left part size
    y = right - mid  # right part size

    # tmp arrays
    l1 = [0] * x
    l2 = [0] * y

    # copy elements from original array to tmp arrays

    for i in range(0, x):
        l1[i] = arr[i + left]

    for j in range(0, y):
        l2[j] = arr[j + mid + 1]

    i = 0
    j = 0
    z = left
    # merge the temp arrays sorted back in the original
    while i < x and j < y:
        if l1[i] <= l2[j]:
            arr[z] = l1[i]
            z += 1
            i += 1
        else:
            arr[z] = l2[j]
            j += 1
            z += 1
    # copy remaining elements

    while i < x:
        arr[z] = l1[i]
        i += 1
        z += 1

    while j < y:
        arr[z] = l2[j]
        j += 1
        z += 1


def mergeSort(arr, left, right):
    if left < right:
        m = (right + left) // 2  # mid index
        mergeSort(arr, left, m)
        mergeSort(arr, m + 1, right)
        merge(arr, left, m, right)


def quickSort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quickSort(arr, left, p - 1)
        quickSort(arr, p + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    leftBound = left - 1
    for i in range(left, right):
        if arr[i] <= pivot:
            leftBound += 1
            arr[i], arr[leftBound] = arr[leftBound], arr[i]

    arr[leftBound + 1], arr[right] = arr[right], arr[leftBound + 1] #swap pivot with leftbound
    return leftBound + 1


def bubbleSort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":

    arr = [55, 1, 4, 10, -2, 100]
    mergeSort(arr, 0, len(arr) - 1)
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

    print()

    arr = [55, 1, 4, 10, -2, 100]
    bubbleSort(arr)
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

    print()

    arr = [55, 1, 4, 10, -2, 100]
    quickSort(arr, 0 , len(arr)-1)
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
