class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low=1
        high=max(nums)
        penalty=high
        while(low<=high):
            mid = low+(high-low)//2
            Ops=0
            for n in nums:
                Ops+=(n-1)//mid
            if Ops<=maxOperations:
                penalty=mid
                high=mid-1
            else:
                low=mid+1
        return penalty
