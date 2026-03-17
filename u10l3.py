def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

data=[11,12,22,23,25,34,64,90]
target=25
result=binary_search(data,target)
print("Binary search: Element found at index", result)