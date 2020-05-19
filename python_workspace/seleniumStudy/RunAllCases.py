import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner


class RunAllCases(object):
    @staticmethod
    def all_case():
        # 测试用例的路径
        case_path = os.path.split(os.path.realpath(__file__))[0] + '/testCase/crm/'
        discover = unittest.defaultTestLoader.discover(case_path,
                                                       pattern='Test*.py',
                                                       top_level_dir=None)
        return discover
if __name__ == "__main__":
    # 测试报告的路径
    report_path = os.path.split(os.path.realpath(__file__))[0] + "\\report"
    if os.path.exists(report_path):
        pass
    else:
        os.makedirs(report_path)
    report_path = report_path + "\TestCRM_report.html"
    runner = HTMLTestRunner(title="[简信CRM]测试报告", description="CRM系统", stream=open(report_path, "wb"),
                            verbosity=2, retry=0, save_last_try=True)
    runner.run(RunAllCases.all_case())