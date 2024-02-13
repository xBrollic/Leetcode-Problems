class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            return "paramihente"


solution = Solution()

print(solution.missingNumber([3,0,1]))

inputs = [[3,0,1],[0,1],[9,6,4,2,3,5,7,0,1]]
outputs = [2,2,8]

# Hello

def answerChecker():
    for i in range(len(inputs)):
        if solution.missingNumber(inputs[i]) == outputs[i]:
            print(solution.missingNumber(inputs[i]),outputs[i])

