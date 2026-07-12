from Holy_Cow.functions.swift_bic.swift_bic import is_valid_swift_bic


def test_is_valid_swift_bic():
    assert is_valid_swift_bic("DEUTDEFF") == True
    assert is_valid_swift_bic("DEUTDEFF500") == True
    assert is_valid_swift_bic("BNPAFRPP") == True
    assert is_valid_swift_bic("BNPAFRPPXXX") == True
    assert is_valid_swift_bic("DEUTDEFF5") == False
    assert is_valid_swift_bic("DEUTDEFF5000") == False
    assert is_valid_swift_bic("DEUTDE") == False
    assert is_valid_swift_bic("deutdeff") == False
    assert is_valid_swift_bic("DEUTdeff") == False
    assert is_valid_swift_bic("DEUTDEff") == False
    assert is_valid_swift_bic("DEU!DEFF") == False
    assert is_valid_swift_bic("DEUT@EFF") == False
    assert is_valid_swift_bic("DEUTDE#F") == False
    assert is_valid_swift_bic("DEUTXXFF") == False
    assert is_valid_swift_bic("DEUTZZFF") == False
    assert is_valid_swift_bic("DEUT DEFF") == True
    assert is_valid_swift_bic("DEUT DEFF 500") == True
    assert is_valid_swift_bic("") == False
    assert is_valid_swift_bic(None) == False
    assert is_valid_swift_bic(12345678) == False
    assert is_valid_swift_bic(["DEUTDEFF"]) == False