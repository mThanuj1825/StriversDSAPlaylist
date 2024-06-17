# Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that
# single one.

def single(arr: list[int]) -> int:
    """
    Finds the single element in an array where every other element appears twice.

    Args:
        arr (list[int]): A list of integers where every element appears twice except for one.

    Returns:
        int: The single element that does not appear twice.

    Example:
        arr = [1, 8, 4, 2, 1, 8, 4]
        single(arr)
        returns 2
    """
    xor = 0  # Initialize the XOR accumulator
    for n in arr:
        xor ^= n  # XOR each element with the accumulator

    return xor  # The result is the single element that does not appear twice


if __name__ == '__main__':
    arr = [1, 8, 4, 2, 1, 8, 4]  # Example array

    print(single(arr))  # Print the single element
