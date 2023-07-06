import pytest

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message('hello world', '5')
    with pytest.raises(TypeError):
        encrypt_message(5, 5)
    assert encrypt_message('hello world', 20) == 'dlrow olleh'
    assert encrypt_message('hello world', 5) == 'olleh_dlrow '
    assert encrypt_message('hello world', 4) == 'dlrow o_lleh'
