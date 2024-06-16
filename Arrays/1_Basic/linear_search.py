# Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not.
# If present print the index of the element or print -1.


def search(arr: list[int], key: int) -> int:
    """
    Checks if the target is present in a list of integers.

    Args:
       arr (list[int]): A list of integers.
       key: integer

    Returns:
       int: index of target if present, else -1

    Example:
       search([2, 5, 1, 3, 0], 1)
       returns 2
    """

    for i, n in enumerate(nums):
        if n == key:
            return i

    return -1


if __name__ == '__main__':
    nums = [2, 5, 1, 0, 3, 7, 4]
    target = 0

    print(search(nums, target))
