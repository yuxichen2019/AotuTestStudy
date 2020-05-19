# -*- coding: utf-8 -*- 
# 2020/4/24 23:01 
# seleniumStudy
# TestBuyApple.py 
# company

from testCase.jd_shopping.BaseCase import BaseCase

class TestBuyApple(BaseCase):
    def testbuy_apple(self):
        self.login('15112342277','yb0922261')
        dr = self.driver
        #搜索栏输入苹果1
        dr.send_keys('xpath=//input[@clstag="h|keycount|head|search_c"]',"苹果")
        #点击搜索按钮
        dr.click('xpath=//button[@clstag="h|keycount|head|search_a"]')
        #点击商品A
        #self.driver.click('xpath=//a[@herf="//item.jd.com/100012686076.html"]')
        dr.click('id=J_AD_100008348542')

        #切换到第二个窗口
        dr.open_new_window()

        #选择红色
        dr.click('xpath=//a[@clstag="shangpin|keycount|product|yanse-黑色"]')
        #选择256G
        dr.click('xpath=//a[@clstag="shangpin|keycount|product|yanse-256GB"]')
        #点击加入购物车
        dr.click('id=InitCartUrl')
        #点击去购物车结算
        dr.click('id=GotoShoppingCart')




if __name__ == '__main__':
    t = TestBuyApple()
    t.testbuy_apple()