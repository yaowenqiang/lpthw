import myprogram
import pytest

def test_doubleit():
    assert myprogram.doubleit(10) == 20


def test_doubleit_type():
    with pytest.raises(TypeError):
        myprogram.doubleit('hello')
