def linearSearch(arr, num):
    for i in range(0, len(arr)):
        if num == arr[i]:
            return i
    return -1


def binarySearch(arr, left, right, num):
    if left <= right:
        mid = (left + right) // 2 #mid index
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            binarySearch(arr, left, mid - 1, num) #search in left part
        elif arr[mid] < num:
            binarySearch(arr, mid + 1, right, num) # search in right part
    else:
        return -1 # not found num


if __name__ == "__main__":
    arr = [11, 23, 23, 55, 74, 100]
    x = 55
    y = 5
    print(binarySearch(arr, 0, len(arr), x))
    print(binarySearch(arr, 0, len(arr) , y))
