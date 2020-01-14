class Solution(object):
    def maxSubArrayLen(self, nums, k):


        ## brute force
        ## have start and end point of i and j and sum everything in between
        ## it will be O(n^3)

        ## plan a grid
        ##grid = [[0 for x in range(len(nums))] for y in range(len(nums))]
        maxLength = 0

        ## Starting the cumulative sum from ith element to j.
        ## O(n^2) Time
        ## Continuously updating maxLength whenever rowICumSum == k
        for i in range(len(nums)):
            rowICumSum = 0
            for j in range(i, len(nums)):
                rowICumSum += nums[j]
                if rowICumSum == k:
                    maxLength = max(maxLength, j - i + 1)

        return maxLength
