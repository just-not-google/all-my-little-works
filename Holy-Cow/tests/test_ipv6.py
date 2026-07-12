from Holy_Cow.functions.ipv6.ipv6 import is_valid_ipv6


def test_is_valid_ipv6():
    assert is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == True
    assert is_valid_ipv6("2001:db8:85a3::8a2e:370:7334") == True
    assert is_valid_ipv6("::1") == True
    assert is_valid_ipv6("::") == True
    assert is_valid_ipv6("2001:db8::1") == True
    assert is_valid_ipv6("fe80::1") == True
    assert is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334:1234") == False
    assert is_valid_ipv6("2001:db8:85a3::8a2e:370") == False
    assert is_valid_ipv6("2001::85a3::8a2e") == False
    assert is_valid_ipv6(":::1") == False
    assert is_valid_ipv6("2001:0gb8:85a3:0000:0000:8a2e:0370:7334") == False
    assert is_valid_ipv6("2001:db8:85a3::8a2e:370:733g") == False
    assert is_valid_ipv6("2001:db8:85a3::8a2e:370:7334/64") == False
    assert is_valid_ipv6("") == False
    assert is_valid_ipv6(None) == False
    assert is_valid_ipv6(123) == False
    assert is_valid_ipv6(["2001:db8::1"]) == False
    assert is_valid_ipv6(" 2001:db8::1 ") == True