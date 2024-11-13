from my_scr.main import Calculator
import pytest

@pytest.mark.calc
def test_sum():
    assert Calculator().sum(3, 2) == 5
@pytest.mark.calc
def test_sub():
    assert Calculator().sub(10, 3) == 7
@pytest.mark.calc
def test_multiply():
    assert Calculator().multiply(5, 5) == 25
@pytest.mark.calc
def test_div():
    assert Calculator().div(45, 5) == 9
@pytest.mark.skip('ne rabotaet')
def test_invisible():
    assert 33 == 5