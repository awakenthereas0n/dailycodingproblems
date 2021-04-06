# April 6, 2021
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

nums = [10, 15, 3, 7]
k = 17

class Solution:
    def solve(self, nums, k):
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(k - num)
        return False

ob = Solution()
print(ob.solve(nums, k))
