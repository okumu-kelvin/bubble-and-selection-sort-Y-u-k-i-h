def selection_sort(arr):
    for i in range(len(arr) - 1):
        # Assume the first element is the minimum
        min_index = i
        # Iterate through the array again to find the minimum element
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the minimum element with the first element
        temp_element = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp_element

    return arr
