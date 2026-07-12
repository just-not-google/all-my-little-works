from Holy_Cow.functions.file_extension.file_extension import is_valid_file_extension


def test_is_valid_file_extension():
    assert is_valid_file_extension(["file.txt", "image.jpg", "data.pdf"]) == [True, True, True]
    assert is_valid_file_extension(["file.txt"]) == [True]
    assert is_valid_file_extension(["file.TXT"]) == [False]
    assert is_valid_file_extension(["file"]) == [False]
    assert is_valid_file_extension(["file."]) == [False]
    assert is_valid_file_extension([".txt"]) == [False]
    assert is_valid_file_extension(["file.unknown"]) == [False]
    assert is_valid_file_extension(["file.txt", "file.unknown"]) == [True, False]
    assert is_valid_file_extension([]) == []
    assert is_valid_file_extension(["", "file.txt"]) == [False, True]
    assert is_valid_file_extension([123]) == [False]
    assert is_valid_file_extension([None]) == [False]
    assert is_valid_file_extension([True]) == [False]