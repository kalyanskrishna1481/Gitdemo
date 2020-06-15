import pytest


@pytest.mark.usefixtures("baseframe")
class TestFrames:
    def test_frames(self, baseframe):
        print("Hello")
        baseframe.find_element_by_link_text("Shop").click()

