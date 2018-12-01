def test_f_strings():
    # A-A-A
    # Arrange - подготовка (входные данные)
    name = 'Ivan'
    age = 30

    # Act
    result = f'My name is {name}. I\'m {age} years old'

    # Assert
    assert 'My name is Ivan. I\'m 30 years old' == result


def test_in_operator_for_seq():
    seq = [8, 'Data', True]
    search = 'Data'

    # result = search in seq
    # assert  result == True

    assert (search in seq)