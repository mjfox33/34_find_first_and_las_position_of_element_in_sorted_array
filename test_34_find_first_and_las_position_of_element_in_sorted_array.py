from code_34_find_first_and_las_position_of_element_in_sorted_array import Solution

def test_example_1():
    s = Solution()
    assert s.searchRange([5,7,7,8,8,10], 8) == [3,4]

def test_example_2():
    s = Solution()
    assert s.searchRange([5,7,7,8,8,10], 6) == [-1,-1]

def test_example_3():
    s = Solution()
    assert s.searchRange([], 0) == [-1,-1]