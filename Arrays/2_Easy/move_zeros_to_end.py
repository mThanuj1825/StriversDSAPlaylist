# Problem Statement: You are given an array of integers. Your task is to move all the zeros in the array to the end of
# the array and move non-zero integers to the front while maintaining their order.

def move_zeros(arr: list[int]) -> None:
    """
    Moves all the zeros in the array to the end while maintaining the order of non-zero elements.

    Args:
        arr (list[int]): A list of integers.

    Returns:
        None: The array is modified in place.

    Example:
        arr = [1, 0, 2, 3, 0, 4, 0, 1]
        move_zeros(arr)
        arr becomes [1, 2, 3, 4, 1, 0, 0, 0]
    """
    left = -1  # Pointer to track the position of the last non-zero element
    right = 0  # Pointer to traverse the array

    while right < len(arr):
        if arr[right] != 0:  # When a non-zero element is found
            left += 1  # Increment the position of the last non-zero element
            arr[left], arr[right] = arr[right], arr[
                left]  # Swap the non-zero element with the element at the left pointer
        right += 1  # Move the right pointer to the next element


if __name__ == '__main__':
    arr = [1, 0, 2, 3, 0, 4, 0, 1]  # Example array

    move_zeros(arr)  # Call the function to move zeros to the end

    print(arr)  # Print the modified array
