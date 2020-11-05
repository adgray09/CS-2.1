def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(0, len(items)-1):
        if len(items) == 0:
            return True
        elif items[i] == items[i+1]:
            continue
        elif items[i] > items[i+1]:
            return False
        else:
            return True
        
        '''
        average case: 0(n) 
        worst case:  0(n)
        '''


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    
    for i in range(0, len(items)-1):
        for j in range(0, len(items)-1):
            if items[j] > items[j+1]:
                items[i], items[j+1] = items[j+1], items[i]
                
    return items

    # recursive solution
    # for i in range(0, len(items)-1):
    #     swapped = False
    #     if items[i] > items[i+1]:
    #         items[i], items[i+1] = items[i+1], items[i]
    #         swapped = True 
    # return items   
                
    # recursive solution
    # if swapped == True:
    #     bubble_sort(items)
    

    '''
    average case: 0(n^2) 
    worst case: 0(n^2)
    '''
def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(len(items)):
        min_index = i
        for j in range(i+1, len(items)-1):
            if items[j] < items[i]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    
    return items

# average is O(n^2)
# worst 0(n^2)


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    
    for i in range(1,len(items)):
        
        #  current index value 
        index_value = items[i]
        
        # equals index to left of current
        j = i-1
        
        while j >= 0 and index_value < items[j]:
            items[j+1] = items[j]
            j -= 1
        
        items[j+1] = index_value
        
    return items

# Average 0(n^2)
# Worst 0(n^2)

items = [3,2,2,3,4,5]
print(is_sorted(items))
print(bubble_sort(items))
print(insertion_sort(items))
print(selection_sort(items))