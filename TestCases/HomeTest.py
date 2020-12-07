#-*- coding: UTF-8 -*-
'''
Created on 2020-1-20

@author: LiPing
'''

from src.CommonFunctions.WangCaiOperations import WangCaiOperations
from src.CommonFunctions.DataOperations import DataOperations
from src.CommonFunctions.LogOperations import LogOperations
import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


global driver,dbopr,logopr,action

class HomeTest(unittest.TestCase):
    '''
          测试首页
    '''
    
    @classmethod
    def setUpClass(cls):
        print("开始测试首页心")
                
        cls.dbopr=DataOperations("HomeTest.xml")        
        cls.driver=WangCaiOperations()
        cls.driver.OpenWangCai()
        cls.logopr=LogOperations()
      
    @classmethod
    def tearDownClass(cls):
        print("首页测试结束")
        cls.driver.QuitWangCai()

          
    def test_bankdepository(self):
        u"点击首页的银行存管"
          
        driver = self.driver
        dbopr = self.dbopr
        logopr = self.logopr
        assertEqual = self.assertEqual
               
        WebDriverWait(driver,10).until(lambda x:x.driver.WangcaiElemClick((dbopr.readxml("method", "xpath"), dbopr.readxml("button", "bank"))))

#         
#         driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("tab", "second"))
#         time.sleep(2)
#          
#         title = driver.GetWangcaiText(dbopr.readxml("method", "css"), dbopr.readxml("tab", "second"))
#          
#         exptitle = driver.GetWangcaiText(dbopr.readxml("method", "css"), dbopr.readxml("message", "mes1"))
#         print(exptitle)
#          
#         if (title == exptitle):
#                       
#             logopr.setInfo(u"点击帮助中心第二个导航测试成功")
#             assertEqual(title, exptitle, "帮助中心,测试通过")
#                             
#         else:
#                
#             logopr.setError(u"点击帮助中心第二个导航测试失败")
#             assertEqual(title, exptitle, "帮助中心,测试不通过") 
                     
    
        
if __name__ == "__main__":
    unittest.main()