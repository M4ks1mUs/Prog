from task import is_palindrom, is_palindrom_rec, get_x, get_x_rec

def test_is_palindrom():
    assert is_palindrom("12321")
    assert is_palindrom("stats")
    assert not is_palindrom([1,2,3,4,5])
    assert not is_palindrom("start")

def test_is_palindrom_rec():
    assert is_palindrom_rec("12321")
    assert is_palindrom_rec("stats")
    assert not is_palindrom_rec([1,2,3,4,5])
    assert not is_palindrom_rec("start")

def test_get_x():
    assert get_x(12)
    assert get_x(3)

def test_get_x_rec():
    assert get_x_rec(12)
    assert get_x_rec(3)
