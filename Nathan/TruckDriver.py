class Solution:
    def maxNumber(self, nums1, nums2, k):
        def maxSubsequence(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(nums1, nums2):
            res = []
            while nums1 or nums2:
                if nums1 > nums2:
                    res.append(nums1.pop(0))
                else:
                    res.append(nums2.pop(0))
            return res

        max_result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            part1 = maxSubsequence(nums1, i)
            part2 = maxSubsequence(nums2, k - i)
            merged = merge(part1[:], part2[:])  # copy para evitar modificar
            max_result = max(max_result, merged)
        return max_result
