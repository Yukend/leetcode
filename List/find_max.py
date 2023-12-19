from typing import List


def majorityElement(nums: List[int]) -> int:    
    max = 0 
    i = 0
    while len(nums) > 1:
            if nums[i] <= nums[i+1]:
                max = nums[i+1]
                nums.remove(nums[i])
            else:
                max = nums[i]
                nums.remove(nums[i+1])
    else:
        max = nums[0]
    return max


if __name__ == "__main__":
    max = majorityElement([1,2,3,4,5,6,7])
    print(max)