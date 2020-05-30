# -*- coding: utf-8 -*- 
# 2020/5/30 14:54 
# appiumTraining
# BaseCase.py 
# company


import unittest
from framework.SunFlower import SunFlower



class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = SunFlower("K6T6R17124002359", "7", "com.tencent.mm",
                                "com.tencent.mm.ui.LauncherUI")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

