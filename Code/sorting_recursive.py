#!python

import random


def merge(items1, items2):

    left_index, right_index = 0, 0
    result = []
    while left_index < len(items1) and right_index < len(items2):
        if items1[left_index] < items2[right_index]:
            result.append(items1[left_index])
            left_index += 1
        else:
            result.append(items2[right_index])
            right_index += 1

    result += items1[left_index:]
    result += items2[right_index:]
    print(result)
    return result

def merge_sort(items):

    if len(items) <= 1:  # base case
        return items

    # divide array in half and merge sort recursively
    half = len(items) // 2
    left = merge_sort(items[:half])
    right = merge_sort(items[half:])

    return merge(left, right)


def partition(items, low, high):

    i = (low-1)
    pivot = items[high]
    
    for j in range(low, high):
        if items[j] <= pivot:
            i += 1
    
    items[i+1], items[high] = items[high], items[i+1]
    
    return (i+1)



def quick_sort(items, low=None, high=None):
    
    if low < high:
        partition_index = partition(items, low, high)
        quick_sort(items, low, partition_index-1)
        quick_sort(items, partition_index+1, high)
    return items



items = [2,2,1,4,7,6]
high = len(items)-1

print(quick_sort(items, 0, high))
print(merge_sort(items))
