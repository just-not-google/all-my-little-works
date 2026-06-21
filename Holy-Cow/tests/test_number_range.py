from Holy_Cow.functions.number_range.number_range import is_valid_number_range


def test_is_valid_number_range():
    assert is_valid_number_range([1, 2, 3, 4, 5], 1, 5) == [True, True, True, True, True]
    assert is_valid_number_range([1, 5], 1, 5) == [True, True]
    assert is_valid_number_range([0, 10], 0, 10) == [True, True]
    assert is_valid_number_range([0, 5, 10], 1, 9) == [False, True, False]
    assert is_valid_number_range([-1, 0, 1], 0, 1) == [False, True, True]
    assert is_valid_number_range([10, 11, 12], 1, 10) == [True, False, False]
    assert is_valid_number_range([], 1, 5) == []
    assert is_valid_number_range([1], 1, 1) == [True]
    assert is_valid_number_range([2], 1, 1) == [False]
    assert is_valid_number_range(["1", "2"], 1, 5) == [False, False]
    assert is_valid_number_range([1.5, 2.5], 1, 5) == [False, False]
    assert is_valid_number_range([None, True], 1, 5) == [False, False]