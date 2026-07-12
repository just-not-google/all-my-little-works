from Holy_Cow.functions.port.port import is_valid_port


def test_is_valid_port():
    assert is_valid_port(80, True) == True
    assert is_valid_port(443, True) == True
    assert is_valid_port(22, True) == True
    assert is_valid_port(1023, True) == True
    assert is_valid_port(0, True) == True
    assert is_valid_port(1024, False) == True
    assert is_valid_port(3000, False) == True
    assert is_valid_port(8080, False) == True
    assert is_valid_port(65535, False) == True
    assert is_valid_port(1024, True) == False
    assert is_valid_port(3000, True) == False
    assert is_valid_port(65535, True) == False
    assert is_valid_port(1023, False) == False
    assert is_valid_port(0, False) == False
    assert is_valid_port(-1, True) == False
    assert is_valid_port(-1, False) == False
    assert is_valid_port(65536, False) == False
    assert is_valid_port(70000, False) == False
    assert is_valid_port("80", True) == False
    assert is_valid_port(80.5, True) == False
    assert is_valid_port(None, True) == False
    assert is_valid_port([80], True) == False