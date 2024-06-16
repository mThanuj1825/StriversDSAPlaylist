# Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending /
# Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False. Note: Two
# consecutive equal values are considered to be sorted.


def check(arr: list[int]) -> bool:
    """
   Checks if the array is sorted in a list of integers.

   Args:
       arr (list[int]): A list of integers.

   Returns:
       bool: true or false.

   Example:
       check([2, 5, 1, 3, 0])
       returns false
   """

    is_increasing = arr[0] <= arr[-1]

    for i in range(len(arr) - 1):
        if is_increasing:
            if arr[i] > arr[i + 1]:
                return False
        else:
            if arr[i] < arr[i + 1]:
                return False

    return True


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 4, 5, 6, 7, 8]

    print("Sorted" if check(nums) else "Not Sorted")
