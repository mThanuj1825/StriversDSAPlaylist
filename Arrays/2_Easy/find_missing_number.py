# Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the
# number (between 1 to N) that is not present in the given array.

def find_missing(arr: list[int]) -> int:
    """
    Finds the missing number in an array of size N-1 containing numbers from 1 to N.

    Args:
        arr (list[int]): A list of integers containing N-1 numbers from 1 to N.

    Returns:
        int: The missing number in the array.

    Example:
        arr = [1, 2, 4, 5]
        find_missing(arr)
        returns 3
    """
    n = len(arr) + 1  # Calculate N from the size of the array (N-1)
    required_sum = (n * (n + 1)) // 2  # Calculate the sum of the first N natural numbers

    for num in arr:  # Subtract each number in the array from the required sum
        required_sum -= num

    return required_sum  # The remaining value is the missing number


if __name__ == '__main__':
    arr = [1, 2, 4, 5]  # Example array

    print(find_missing(arr))  # Print the missing number
