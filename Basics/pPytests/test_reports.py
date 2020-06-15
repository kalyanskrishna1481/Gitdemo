import pytest

from pPytests.Baseclass import BaseClass


@pytest.mark.usefixtures("reports90")
class TestReport(BaseClass):

    def test_reports(self, reports90):
        log = self.getblogger()
        log.info(reports90[3])
        log.info(reports90[4])
        print(reports90[1])


