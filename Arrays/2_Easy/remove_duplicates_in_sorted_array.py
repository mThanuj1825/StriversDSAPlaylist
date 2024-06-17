# Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that
# each unique element appears only once. The relative order of the elements should be kept the same.
#
# If there are k elements after removing the duplicates, then the first k elements of the array should hold the final
# result. It does not matter what you leave beyond the first k elements.
#
# Note: Return k after placing the final result in the first k slots of the array.

def remove_duplicates(arr: list[int]) -> int:
    """
    Removes duplicates from the sorted array in place, ensuring each unique element appears only once.

    Args:
        arr (list[int]): A sorted list of integers.

    Returns:
        int: The number of unique elements in the array.

    Example:
        arr = [1, 1, 2, 2, 3]
        k = remove_duplicates(arr)
        arr becomes [1, 2, 3, _, _]
        returns 2
    """
    if len(arr) == 1:
        return 0  # If there's only one element, no duplicates to remove

    left = 0  # Pointer to track the position of the last unique element
    right = 1  # Pointer to traverse the array

    while right < len(arr):
        if arr[left] != arr[right]:  # When a new unique element is found
            left += 1  # Move the left pointer to the next position for unique element
            arr[left] = arr[right]  # Place the unique element at the left pointer position
        right += 1  # Move the right pointer to the next element

    return left  # Return the index of the last unique element


if __name__ == '__main__':
    arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]  # Example array

    k = remove_duplicates(arr)  # Call the function to remove duplicates

    print(arr[:k + 1])  # Print the array up to the k+1 elements
