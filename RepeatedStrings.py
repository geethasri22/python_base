class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        n = len(s)
        if n % k != 0:   # must divide evenly
            return False

        # Split into chunks of length k
        chunks = [s[i:i+k] for i in range(0, n, k)]

        # Count frequency of each chunk
        from collections import Counter
        freq = Counter(chunks)

        # If only one unique chunk → already repetition
        if len(freq) == 1:
            return True

        # If more than 2 unique chunks → cannot fix with one replacement
        if len(freq) > 2:
            return False

        # If exactly 2 unique chunks → check if one occurs only once
        return 1 in freq.values()
