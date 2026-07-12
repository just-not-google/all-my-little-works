from Holy_Cow.functions.http_status_code.http_status_code import is_valid_http_status_code


def test_is_valid_http_status_code():
    assert is_valid_http_status_code(200) == True
    assert is_valid_http_status_code(404) == True
    assert is_valid_http_status_code(500) == True
    assert is_valid_http_status_code(301) == True
    assert is_valid_http_status_code(403) == True
    assert is_valid_http_status_code(0) == False
    assert is_valid_http_status_code(99) == False
    assert is_valid_http_status_code(600) == False
    assert is_valid_http_status_code(1000) == False
    assert is_valid_http_status_code(-1) == False
    assert is_valid_http_status_code("200") == False
    assert is_valid_http_status_code(200.5) == False
    assert is_valid_http_status_code(None) == False
    assert is_valid_http_status_code([200]) == False
    assert is_valid_http_status_code({"code": 200}) == False