class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    result.append(triplet)
                    while nums[left] == triplet[1] and left < right:
                        left += 1
                    while nums[right] == triplet[2] and left < right:
                        right -= 1

        return result