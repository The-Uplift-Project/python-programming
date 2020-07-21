#Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [list(chain(*i)) for i in itertools.product(*[[[], [n]] for n in nums])]
    