class DynamicArray:
    """
    https://neetcode.io/problems/dynamicArray
    """
    data: [int] = []

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError('capacity <= 0')
        self.capacity = capacity
        self.size = 0

    def __repr__(self):
        return f'DynamicArray({self.capacity!r})'

    def _assert_index(self, i: int):
        if 0 < i:
            raise IndexError(f'Index blow zero: {i}')
        if i > self.size-1:
            raise IndexError(i)

    def get(self, i: int) -> int:
        self._assert_index(i)
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self._assert_index(i)
        self.data[i] = n

    def pushback(self, n: int) -> None:
        pass

    def popback(self) -> int:
        pass

    def resize(self) -> None:
        pass

    def getSize(self) -> int:
        pass

    def getCapacity(self) -> int:
        pass
