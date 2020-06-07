import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner




class RunAllCases(object):
    @staticmethod
    def all_case():
        # 测试用例的路径
        # case_path = os.path.split(os.path.realpath(__file__))[0]
        # print('case path',case_path)
        discover = unittest.defaultTestLoader.discover('./',
                                                       pattern='Test*.py',
                                                       top_level_dir=None)
        return discover


if __name__ == "__main__":
    # 创建报告的路径
    report_path = os.path.split(os.path.realpath(__file__))[0] + "\\report"
    if os.path.exists(report_path):
        pass
    else:
        # 创建多层级的文件夹
        os.makedirs(report_path)
    report_path = report_path + "\TestCRM_report.html"
    runner = HTMLTestRunner(title="简信CRM", description="自动化测试", stream=open(report_path, "wb"),
                            verbosity=2, retry=0, save_last_try=True)
    runner.run(RunAllCases.all_case())
