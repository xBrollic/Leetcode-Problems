class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()
        dupe = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j:
                    dupe = nums[i]
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return [dupe, i+1]
            
solution = Solution()

list1 = [1,5,3,2,2,7,6,4,8,9]
list1.sort()
newset = set(list1)
newlist = list(newset)
print(newlist)

print(list1)

print(solution.findErrorNums([1,5,3,2,2,7,6,4,8,9]),[2,10])

#print(solution.findErrorNums([1,2,2,4]), [2,3])
#print(solution.findErrorNums([1,1]),[1,2])
#print(solution.findErrorNums([3,2,2]),[2,1])
#print(solution.findErrorNums([2,3,2]),[2,1])
#print(solution.findErrorNums([1,3,3]),[3,2])
#print(solution.findErrorNums([3,2,3,4,6,5]),[3,1])


