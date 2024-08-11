class Main:
    def singleNumber(self, nums):
        # nums: List[int]
        result = []
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.append(num)
        return sum(result)
main = Main()
nums = [2,2,1]
print(main.singleNumber(nums))
nums =  [4,1,2,1,2]
print(main.singleNumber(nums))
