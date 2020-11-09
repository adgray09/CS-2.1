#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def bubble_sort(numbers):
    for i in range(0, len(numbers)-1):
        for j in range(0 , len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[i], numbers[j+1] = numbers[j+1], numbers[i]
    return numbers

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output lis
    
    max_value = max(numbers)
    bucket_list = []
    size = max_value/len(numbers)
    result = []
    
    for i in range(num_buckets):
        bucket_list.append([])
        
    for i in range(len(numbers)):
        j = int(numbers[i] / size)
        
        if j != len(numbers):
            bucket_list[j].append(numbers[i])
        else:
            bucket_list[len(numbers)-1].append(numbers[i])
            
    for z in range(len(numbers)):
        bubble_sort(bucket_list[z])
        
    for x in range(len(numbers)):
        result = result + bucket_list[x]
    return result

items = [4,3,6,9,8,1,2]

print(bucket_sort(items)) 

def bucket_sort(numbesr, num_buckets=10):
    max_value = max(numbers)
    size = max_size/len(numbers)
    result = []
    bucket_list = []
    
    for i in range(num_buckets):
        bucket_list.append([])
        
    for i in range(len(numbers)):
        j = int(numbers[i]/size)
        
        if j != len(numbers):
            bucket_list[j].append(numbers[i])          
