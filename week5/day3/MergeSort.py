def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])
    i = 0
    j = 0
    k = 0
    while i<len(left_sorted) and j<len(right_sorted):
        if left_sorted[i]<=right_sorted[j]:
            arr[k] = left_sorted[i]
            i+=1
            
        else:
            arr[k] = right_sorted[j]
            j+=1
        k+=1
    while i<len(left_sorted):
        arr[k] = left_sorted[i]
        i+=1
        k+=1
    while j<len(right_sorted):
        arr[k] = right_sorted[j]
        k+=1
        j+=1
    return arr
    
arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(arr))
    