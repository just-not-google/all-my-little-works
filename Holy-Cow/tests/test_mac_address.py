from Holy_Cow.functions.mac_address.mac_address import is_valid_mac_address


def test_is_valid_mac_address():
    assert is_valid_mac_address("00:1A:2B:3C:4D:5E") == True
    assert is_valid_mac_address("00-1A-2B-3C-4D-5E") == True
    assert is_valid_mac_address("001A.2B3C.4D5E") == True
    assert is_valid_mac_address("001A2B3C4D5E") == True
    assert is_valid_mac_address("FF:FF:FF:FF:FF:FF") == True
    assert is_valid_mac_address("aa:bb:cc:dd:ee:ff") == True
    assert is_valid_mac_address("00:1A:2B:3C:4D") == False
    assert is_valid_mac_address("00:1A:2B:3C:4D:5E:6F") == False
    assert is_valid_mac_address("001A2B3C4D5") == False
    assert is_valid_mac_address("001A2B3C4D5E6F") == False
    assert is_valid_mac_address("00:1A:2B:3C:4D:5G") == False
    assert is_valid_mac_address("00:1A:2B:3C:4D:5 ") == False
    assert is_valid_mac_address("00:1A:2B:3C:4D:5!") == False
    assert is_valid_mac_address("") == False
    assert is_valid_mac_address(None) == False
    assert is_valid_mac_address(123) == False
    assert is_valid_mac_address(["00:1A:2B:3C:4D:5E"]) == False