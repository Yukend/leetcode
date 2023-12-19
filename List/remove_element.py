from typing import List


def removeElement(nums: List[int], val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if nums[i - count] == val:
            nums.remove(val)
            count += 1
    return len(nums)


if __name__ == '__main__':
    nums = [0, 2, 3, 4, 2, 2, 4, 1]
    val = 2
    out = removeElement(nums, val)
    print(out)