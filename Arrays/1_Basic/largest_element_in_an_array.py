# Problem Statement: Given an array, we have to find the largest element in the array.


def largest_element(arr: list[int]) -> int:
    """
   Finds the largest element in a list of integers.

   Args:
       arr (list[int]): A list of integers.

   Returns:
       int: The largest integer in the list.

   Example:
       largest_element([2, 5, 1, 3, 0])
       returns 5
   """

    largest = float('-inf')

    for num in arr:
        if num > largest:
            largest = num

    return largest


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 0]

    print(largest_element(nums))
