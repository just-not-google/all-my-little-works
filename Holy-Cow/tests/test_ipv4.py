from Holy_Cow.functions.ipv4.ipv4 import is_valid_ipv4


def test_is_valid_ipv4():
    assert is_valid_ipv4("192.168.1.1") == True
    assert is_valid_ipv4("10.0.0.1") == True
    assert is_valid_ipv4("255.255.255.255") == True
    assert is_valid_ipv4("0.0.0.0") == True
    assert is_valid_ipv4("127.0.0.1") == True
    assert is_valid_ipv4("192 168 1 1") == True
    assert is_valid_ipv4("10 0 0 1") == True
    assert is_valid_ipv4("192.168.1") == False
    assert is_valid_ipv4("192.168.1.1.1") == False
    assert is_valid_ipv4("192.168.1.") == False
    assert is_valid_ipv4(".192.168.1") == False
    assert is_valid_ipv4("256.168.1.1") == False
    assert is_valid_ipv4("192.300.1.1") == False
    assert is_valid_ipv4("192.168.-1.1") == False
    assert is_valid_ipv4("192.168.1.256") == False
    assert is_valid_ipv4("192.168.01.1") == False
    assert is_valid_ipv4("192.168.001.1") == False
    assert is_valid_ipv4("010.0.0.1") == False
    assert is_valid_ipv4("abc.168.1.1") == False
    assert is_valid_ipv4("192.abc.1.1") == False
    assert is_valid_ipv4("192.168.abc.1") == False
    assert is_valid_ipv4("") == False
    assert is_valid_ipv4(None) == False
    assert is_valid_ipv4(123) == False