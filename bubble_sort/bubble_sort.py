def bubble_sort(unsorted_list):
    # For loop to iterate through the list
    for i in range (len(unsorted_list) - 1):
        # Iterate through the list again for each element
        for j in range (len(unsorted_list) - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                # Swap the elements if the current is greater than the next
                temp_element = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j + 1]
                unsorted_list[j + 1] = temp_element
            else:
                # If the current element is less than or equal to the next, do nothing
                pass

    return unsorted_list

# Something I learnt from C is that you can swap two variables without using a temporary variable by using a bitwise XOR operation.
# unsorted_list[j] = unsorted_list[j] ^ unsorted_list[j + 1]
# unsorted_list[j + 1] = unsorted_list[j] ^ unsorted_list[j + 1]
# unsorted_list[j] = unsorted_list[j] ^ unsorted_list[j + 1]
