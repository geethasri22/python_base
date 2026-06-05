class Solution:
    def lexicographicallySmallest(self, s, k):
        n = len(s)

        # Correct k
        if (n & (n - 1)) == 0:   # power of 2
            k //= 2
        else:
            k *= 2

        # Not possible
        if k < 0 or k >= n:   # allow k == 0
            return -1

        stack = []
        for ch in s:
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # If still removals left, cut from end
        result = "".join(stack[:-k] if k else stack)
        return result if result else -1
