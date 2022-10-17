from functools import lru_cache
from math import inf


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        # Get length of s
        n = len(s)

        # Return the minimum length of the run-length encoded version of s
        # k: the number of skip remaining
        # i: pointer to the current character
        # j: pointer to the previously picked character 
        # c: the count of previously picked character
        @lru_cache(None)
        def counts(k, i, j, c):

            # If we skip more than allowed, return infinity
            if k < 0:
                return inf

            # If we reach the end of s, return 0
            if i >= n:
                return 0

            # If the current character is the same as the previously picked character, we pick it and increment the minimum length if the count of previously picked character is at 1, 9, or 99
            if 0 <= j < n and s[i] == s[j]:

                return int(c == 1 or c == 9 or c == 99) + counts(k, i + 1, i, c + 1)

            # Else, take the minimum between picking the current character or skipping the current character
            return min(1 + counts(k, i + 1, i, 1), counts(k - 1, i + 1, j, c))

        return counts(k, 0, -1, 0)
