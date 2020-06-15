import json
import os
import unittest
from HTMLTestRunner_cn import HTMLTestRunner

from framework.BlueRose import BlueRose
from framework.UtilsRandom import UtilsRandom


class TestSpringBootAdd(unittest.TestCase):
    def setUp(self):
        self.requests = BlueRose()
        self.baseURL = "http://127.0.0.1:9090/api/"

    def test_springBootAdd(self):
        url = self.baseURL + "notes"
        header = {"Content-Type": "application/json"}
        chineseName = UtilsRandom.getChineseName()
        keys = ['title', 'content']
        values = [chineseName, chineseName]
        dictionary = dict(zip(keys, values))
        data = json.dumps(dictionary)
        response = self.requests.sendRequests(url=url, method="post",data=data, headers=header)
        title = self.requests.getJsonFilesValue(response,"title")
        # print(json.loads(response.content)["id"])
        id = self.requests.getJsonFilesValue(response,"id")
        print(id)
        self.assertEqual(title, chineseName)


if __name__ == "__main__":
    report_path = os.path.dirname(__file__) + "/report/" + "TestSpringBootAdd.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSpringBootAdd)
    runer = HTMLTestRunner(title="简信CRM", description="创建客户", stream=open(report_path, "wb"),
                           verbosity=2, retry=0, save_last_try=True)
    runer.run(suite)
