import random
def three_way_quick_sort(arr, left, right):
    if left >= right:
        return
    
    pivot_idx = random.randint(left, right)
    arr[pivot_idx], arr[left] = arr[left], arr[pivot_idx]
    pivot = arr[left]
    
    
    lt = left
    gt = right
    i = left + 1
    
    while i <= gt:
        if arr[i] < pivot:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:  
            i += 1
    
    three_way_quick_sort(arr, left, lt - 1)
    three_way_quick_sort(arr, gt + 1, right)