import random

def partition(arr, left, right):
    pivot_idx = random.randint(left, right)
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    pivot = arr[right]
    
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def quick_sort_random(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quick_sort_random(arr, left, pi - 1)
        quick_sort_random(arr, pi + 1, right)