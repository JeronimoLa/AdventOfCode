import time 

"""
quicksort: 

    best case: O(nlogn) - if partitioning is always in the middle
    worst case: O(n)2 - if partition keeps happening at the start of a list 
"""

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(items:list, low=0, high=None):
    if high is None:
        high = len(items) - 1
    
    if low < high:
        pivot_index = partition(items, low, high)
        quicksort(items, low, pivot_index-1)
        quicksort(items, pivot_index+1, high)

def main():

    start_time = time.perf_counter()

    first_list = []
    second_list = []

    with open("data/1.txt") as file:
        for item in file:
            line = item.strip().split()
            first_list.append(line[0])
            second_list.append(line[1])

    quicksort(first_list)
    quicksort(second_list)

    occurences = {}
    for i in range(len(second_list)):
        if second_list[i] not in occurences:
            occurences[second_list[i]] = []
            occurences.update({second_list[i]: 1})
            continue
        current_value = occurences.get(second_list[i])
        occurences.update({second_list[i]: current_value+1})
    
    similarity_score_sum = 0
    for item in first_list:
        if item in occurences:
            value = occurences.get(item)
            similarity_score = int(item) * value
            similarity_score_sum += similarity_score

    print(f"similarity_score: {similarity_score_sum}")

    
    total = 0
    list_length = len(first_list) - 1
    while list_length >= 0:
        first, second = int(first_list[list_length]), int(second_list[list_length])

        if first > second:
            sum_num = first - second
            total += sum_num
        else:
            sum_num = second - first 
            total += sum_num

        list_length -= 1

    elapsed_time = time.perf_counter() - start_time
    print(f"sum: {total}")
    print(f"Elapsed time: {elapsed_time:.4f}")


if __name__ == "__main__":
    main()