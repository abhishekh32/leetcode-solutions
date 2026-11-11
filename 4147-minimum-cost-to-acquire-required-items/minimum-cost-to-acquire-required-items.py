class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int,
                    need1: int, need2: int) -> int:

        # Option 1: Buy items separately
        option1 = need1 * cost1 + need2 * cost2

        # Option 2: Buy type 3 items for the common requirement
        common = min(need1, need2)
        option2 = common * costBoth
        option2 += (need1 - common) * cost1
        option2 += (need2 - common) * cost2

        # Option 3: Buy only type 3 items, even if some contribution is extra
        option3 = max(need1, need2) * costBoth

        return min(option1, option2, option3)