# Bubble sort Algorithm Implementation

# Bubble Sort is one of the most straightforward sorting algorithms. Its name comes from the way
# the algorithm works: With every new pass, the largest element in the list “bubbles up” toward
# its correct position.

# Bubble sort consists of making multiple passes through a list, comparing elements one by one, and
# swapping adjacent items that are out of order.


def BubbleSort(arr):

    n = len(arr)

    for i in range(n):

        # set a flag to stop sorting
        # if array is already sorted
        already_sorted = True

        # comparing items with its adjecent
        # elements
        for j in range(n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # since you have to swap only two
                # element
                already_sorted = False

        if already_sorted:
            break

    return array


# main Driver program
array = list(map(int, input("Enter element of list : ").split(",")))

# Function call
print(BubbleSort(array))


