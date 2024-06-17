# Problem Statement: Given an array of N integers, left rotate the array by one place.

def rotate_left(nums: list[int], k: int) -> list[int]:
    """
    Rotates the given array by k steps to the left

    Args:
        nums (list[int]): A list of integers.
        k: integer

    Returns:
        list[int]: A rotated list of integers.

    Example:
        rotate_left([1, 2, 3, 4, 5], 2)
        returns [3, 4, 5, 1, 2]
    """

    def reverse(nums: list[int], left=0, right=len(nums) - 1) -> None:
        """
         Reverses the given array from left to right

         Args:
            nums (list[int]): A list of integers.
            left: integer
            right: integer

         Returns:
            None: Reverses the array in-place

         Example:
            reverse([1, 2, 3, 4, 5])
            returns [5, 4, 3, 2, 1]
        """
        while left < right:  # whenever we cross paths with the other pointer, we dont have to reverse any more elements
            nums[left], nums[right] = nums[right], nums[left]  # swap every pair form left and right
            left += 1
            right -= 1

    k %= len(nums)  # normalize 'k' value to be in the range of [0, len(nums) - 1]
    k = len(nums) - k  # do this in order to convert this problem into rotate 'k' times to the right

    reverse(nums)

    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)

    return nums


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    k = 1

    print(rotate_left(arr.copy(), k))
