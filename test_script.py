import pytest
from script import main_def


def test_main_def():
	a = 2
	assert a+1 == main_def(a)

