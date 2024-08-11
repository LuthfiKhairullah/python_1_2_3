class Main:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in temp:
                return [temp[diff], i]
            temp[num] = i

main = Main()
nums = [2,7,11,15]
target = 17
result = main.twoSum(nums, target)
print(result)