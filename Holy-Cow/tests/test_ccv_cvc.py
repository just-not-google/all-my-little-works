from Holy_Cow.functions.ccv_cvc.ccv_cvc import is_valid_ccv_cvc


def test_is_valid_ccv_cvc():
    assert is_valid_ccv_cvc(123) == True
    assert is_valid_ccv_cvc(999) == True
    assert is_valid_ccv_cvc(100) == True
    assert is_valid_ccv_cvc(1000) == True
    assert is_valid_ccv_cvc(9999) == True
    assert is_valid_ccv_cvc(5555) == True
    assert is_valid_ccv_cvc(99) == False
    assert is_valid_ccv_cvc(10000) == False
    assert is_valid_ccv_cvc(0) == False
    assert is_valid_ccv_cvc(-1) == False
    assert is_valid_ccv_cvc(50) == False
    assert is_valid_ccv_cvc("123") == False
    assert is_valid_ccv_cvc(123.5) == False
    assert is_valid_ccv_cvc(None) == False
    assert is_valid_ccv_cvc([123]) == False
    assert is_valid_ccv_cvc({"code": 123}) == False