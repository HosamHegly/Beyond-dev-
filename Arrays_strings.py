
#Retrun the reverse of a given string
def reverse_string(str):
    return str[::-1]

#return min and max value of array
def max_min_array (arr):
    max = arr[0]
    min = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    return  min, max

# remove duplicates in sorted array
def remove_duplicate(arr):
    n = len(arr)
    temp = list(range(n))  # initialize new list

    if n== 0 or n == 1: # if list is empty or contains one element
        return n
    j = 0
    for i in range(0, n - 1):

        # If current element is not equal to next
        # then store that current element
        if arr[i] != arr[i + 1]:
            temp[j] = arr[i]
            j += 1

    # Store the last element as whether it is unique
    # or repeated, it isn't stored previously
    temp[j] = arr[n - 1]
    j += 1

    # Modify original array
    for i in range(0, j):
        arr[i] = temp[i]

    while len(arr) > j:
        arr.pop(len(arr)-1)

    return  j

if __name__=="__main__":
    print(reverse_string("hello world"))

    arr = [-10, 1 ,5, 99 , 57]
    print(max_min_array(arr))

    arr = [1,1,1,2,2,5,10,11,11]
    remove_duplicate(arr)
    print(arr)



