# Problem Statement: Given an array, find the second largest element in the array. Print ‘-1’
# in the event that doesn’t exist.

def second_largest(nums: list[int]) -> int:
    """
   Finds the second largest element in a list of integers.

   Args:
       nums (list[int]): A list of integers.

   Returns:
       int: The second largest integer in the list.

   Example:
       second_largest([2, 5, 1, 3, 0])
       returns 3
   """

    max1 = max2 = float("-inf")

    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max2 if max2 != max1 else -1


if __name__ == '__main__':
    arr = [9, 4, 2, 0, 10, 20, 15]

    print(second_largest(arr))
