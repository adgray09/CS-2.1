#!python

import random


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
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

    


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) <= 1:  # base case
        return items

    # divide array in half and merge sort recursively
    half = len(items) // 2
    left = merge_sort(items[:half])
    right = merge_sort(items[half:])

    return merge(left, right)

# worst case O(n log n)

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    
    i = (low-1)
    pivot = items[high]
    
    for j in range(low, high):
        if items[j] <= pivot:
            i += 1
    
    items[i+1], items[high] = items[high], items[i+1]
    
    return (i+1)



def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort  
    
    # best case # worst case O(n log n)
    
    if low < high:
        partition_index = partition(items, low, high)
        quick_sort(items, low, partition_index-1)
        quick_sort(items, partition_index+1, high)
    return items



items = [2,2,1,4,7,6]
high = len(items)-1

print(quick_sort(items, 0, high))
print(merge_sort(items))
