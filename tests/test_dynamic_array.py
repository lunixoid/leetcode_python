from neetcode.basics.dynamic_array import DynamicArray


def test_case_1():
    array = DynamicArray(1)
    assert array.getSize() == 0
    assert array.getCapacity() == 1
