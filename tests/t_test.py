from arabic_pronounce import phonetise

def test_1():
    actual = phonetise('ثٌمَّ')
    expected = ['^ u0 n mm a']
    assert actual == expected

def test_2():
    actual = phonetise('ثٌمّ')
    expected = ['^ u0 n mm']
    assert actual == expected

def test_3():
    actual = phonetise('ثكمّ')
    expected = ['^ k mm']
    assert actual == expected