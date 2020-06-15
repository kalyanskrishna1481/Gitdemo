import pytest


@pytest.mark.usefixtures("chmesetup")
def test_first():
    print("hello welcome to pytest conftest")

