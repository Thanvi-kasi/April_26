class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        # Build mapping from nums2
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Remaining elements have no greater element
        while stack:
            next_greater[stack.pop()] = -1

        # Build result for nums1
        return [next_greater[num] for num in nums1]
