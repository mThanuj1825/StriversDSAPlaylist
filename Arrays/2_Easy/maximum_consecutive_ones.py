# Problem Statement: Given an array that contains only 1 and 0, return the count of maximum consecutive ones in the
# array.

def max_consecutive_ones(arr: list[int]) -> int:
    """
    Finds the maximum number of consecutive 1s in the given array.

    Args:
        arr (list[int]): A list of integers containing only 0s and 1s.

    Returns:
        int: The count of the maximum number of consecutive 1s in the array.

    Example:
        max_consecutive_ones([1, 1, 0, 1, 1, 1])
        returns 3
    """
    max_count = 0  # Variable to store the maximum count of consecutive 1s found
    count = 0  # Variable to count the current sequence of consecutive 1s

    for n in arr:
        if n == 0:  # When a 0 is encountered
            max_count = max(max_count, count)  # Update max_count if current count is greater
            count = 0  # Reset count for the next sequence of 1s
        else:
            count += 1  # Increment count for the current sequence of 1s

    return max(max_count, count)  # Return the maximum count found, considering the end of the array


if __name__ == '__main__':
    arr = [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1]  # Example array

    print(max_consecutive_ones(arr))  # Print the result of the function
