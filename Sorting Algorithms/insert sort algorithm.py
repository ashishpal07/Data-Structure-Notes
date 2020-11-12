# insert Sort Algorithms

def insertSort(arr):

    for i in range(1, len(arr)):

        key_element = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key_element:
            
            arr[j + 1] = arr[j]

            j -= 1


        arr[j+1] = key_element

    return arr

# Deriver code
array = list(map(int, input("Enter element of list : ").split(",")))

print(insertSort(array))

run_sorting_algorithm(algorithm="insertSort", array=array)
