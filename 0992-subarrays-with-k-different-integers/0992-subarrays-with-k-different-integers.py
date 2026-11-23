class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atmost(k1: int):
            l = r = 0
            count = 0
            mapp = defaultdict(int)
            while r < len(nums):
                mapp[nums[r]] = mapp.get(nums[r], 0) + 1
                while len(mapp.keys()) > k1:
                    mapp[nums[l]] -= 1
                    if mapp[nums[l]] == 0:
                        del mapp[nums[l]]
                    l += 1
                count += (r - l + 1)
                r += 1
            return count
        return atmost(k) - atmost(k - 1)