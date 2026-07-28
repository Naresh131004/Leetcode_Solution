class Solution:
	def ContainsDuplicate(self, nums: List[int]) -> bool:
		seen = set()
		
		for num in nums:
			if num in seen:
				return True
			seen.add(num)
		return False