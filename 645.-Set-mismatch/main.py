class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
            result = []
            nums.sort()
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1] and nums[0] == 1 and nums[i]-nums[i-1] <= 1:
                    result.append(nums[i])
                    result.append(nums[i]+1)
                if nums[i] == nums[i+1] and nums[0] == 1 and nums[i]-nums[i-1] > 1:
                    result.append(nums[i])
                    result.append(nums[i]-1)
                if nums[i] == nums[i+1] and nums[0]!=1:
                    result.append(nums[i])
                    result.append(nums[i]-1)
            return result
            
#Hello

list = [3,2,3,4,6,5]
list.sort()
print(list)

solution = Solution()
print(solution.findErrorNums([1,2,2,4]), [2,3])
print(solution.findErrorNums([1,1]),[1,2])
print(solution.findErrorNums([3,2,2]),[2,1])
print(solution.findErrorNums([2,3,2]),[2,1])
print(solution.findErrorNums([1,3,3]),[3,2])
print(solution.findErrorNums([3,2,3,4,6,5]),[3,1])
