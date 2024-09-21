class Summarizer:

    def __init__(self, a):
        self.a = a
        self.n = len(a)
        self.pre_computed = self.pre_compute()

    def pre_compute(self):
        pre_computed = [0] * (self.n + 1)
        acc = 0
        for i in range(self.n):
            acc += self.a[i]
            pre_computed[i + 1] = acc
        return pre_computed

    def find_sum(self, start, end):
        """
        Calculate the sum of elements in the array from index 'start' to 'end' (inclusive).

        This method uses pre-computed cumulative sums to efficiently calculate
        the sum of a range of elements in the array.

        Parameters:
        start (int): The starting index of the range (inclusive).
        end (int): The ending index of the range (inclusive).

        Returns:
        int: The sum of elements from index 'start' to 'end'.

        Raises:
        ValueError: If 'start' is less than 0 or 'end' is greater than or equal to
                    the length of the array.

        Examples:
        >>> s = Summarizer([1, 2, 3, 4, 5])
        >>> s.find_sum(1, 3)
        9
        >>> s.find_sum(0, 4)
        15
        >>> s.find_sum(2, 2)
        3
        """
        if start < 0:
            raise ValueError("start must be >= 0")
        if end >= self.n:
            raise ValueError(f"end must be < {self.n}")
        if start == end:
            return self.a[start]
        return self.pre_computed[end + 1] - self.pre_computed[start]
