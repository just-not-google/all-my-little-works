from Holy_Cow.functions.url.url import is_valid_url


def test_is_valid_url():
    assert is_valid_url("https://example.com") == True
    assert is_valid_url("http://example.com") == True
    assert is_valid_url("https://www.example.com") == True
    assert is_valid_url("https://example.com/path") == True
    assert is_valid_url("https://example.com:8080") == True
    assert is_valid_url("https://example.com:3000/path") == True
    assert is_valid_url("example.com") == False
    assert is_valid_url("://example.com") == False
    assert is_valid_url("https//example.com") == False
    assert is_valid_url("ftp://example.com") == False
    assert is_valid_url("invalid://example.com") == False
    assert is_valid_url("https://") == False
    assert is_valid_url("https://..") == False
    assert is_valid_url("https://example..com") == False
    assert is_valid_url("https://-example.com") == False
    assert is_valid_url("https://example-.com") == False
    assert is_valid_url("https://example.com:80") == False
    assert is_valid_url("https://example.com:1023") == False
    assert is_valid_url("https://example.com:65536") == False
    assert is_valid_url("https://example.com:abc") == False
    assert is_valid_url("") == False
    assert is_valid_url(None) == False
    assert is_valid_url(123) == False
    assert is_valid_url(["https://example.com"]) == False