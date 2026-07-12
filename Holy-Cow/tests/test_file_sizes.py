from Holy_Cow.functions.file_sizes.file_sizes import is_valid_file_sizes


def test_is_valid_file_sizes():
    assert is_valid_file_sizes(1, "KB", 1024, "B") == True
    assert is_valid_file_sizes(1, "MB", 1024, "KB") == True
    assert is_valid_file_sizes(1, "GB", 1024, "MB") == True
    assert is_valid_file_sizes(1, "TB", 1024, "GB") == True
    assert is_valid_file_sizes(1024, "B", 1, "KB") == True
    assert is_valid_file_sizes(1, "KB", 1000, "B") == False
    assert is_valid_file_sizes(1, "MB", 1000, "KB") == False
    assert is_valid_file_sizes(2, "KB", 2049, "B") == False
    assert is_valid_file_sizes(-1, "KB", 1024, "B") == False
    assert is_valid_file_sizes(1, "KB", -1024, "B") == False
    assert is_valid_file_sizes(1, "invalid", 1024, "B") == False
    assert is_valid_file_sizes(1, "KB", 1024, "invalid") == False
    assert is_valid_file_sizes("1", "KB", 1024, "B") == False
    assert is_valid_file_sizes(1, 123, 1024, "B") == False
    assert is_valid_file_sizes(1, "KB", "1024", "B") == False
    assert is_valid_file_sizes(None, "KB", 1024, "B") == False