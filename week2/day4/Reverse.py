def Reverse(arr):
    arr = [10, 20, 30, 40]
    left = 0
    right = len(arr) - 1
    while left<right:
        arr[right],arr[left] = arr [left],arr[right]
        left +=1
        right -=1
        return arr

array=[40,30,20,10]
Reverse(array)