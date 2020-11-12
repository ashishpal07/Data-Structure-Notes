# Dividing the input list is referred to as partitioning the list.
# Quicksort first selects a pivot element and partitions the list
# around the pivot, putting every smaller element into a low array
# and every larger element into a high array.

# Putting every element from the low list to the left of the pivot
# and every element from the high list to the right positions the
# pivot precisely where it needs to be in the final sorted list.
# This means that the function can now recursively apply the same
# procedure to low and then high until the entire list is sorted.


# implementing Quick sort algorithms

from random import randint

def quick_sort(array):

    # if array contains only one element
    # return itself
    if len(array) < 2:
        return array


    low, same, high = [], [], []

    # select pivot(middle) element randomly
    pivot = array[randint(0, len(array)-1)]


    for item in array:

        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item > pivot:
            high.append(item)
        elif item == pivot:
            same.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quick_sort(low) + same + quick_sort(high)

# main program
arr = list(map(int, input("Enter list element : ").split(",")))

# finction call
print(quick_sort(arr))



                  
    
