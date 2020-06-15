import pytest


@pytest.mark.usefixtures("tupleddata")
class Test2:

    def test_2(self, tupleddata):
        print("Tupled data")
        print(tupleddata[1])
        print(tupleddata[3])
