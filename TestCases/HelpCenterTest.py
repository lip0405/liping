#-*- coding: UTF-8 -*-
'''
Created on 2020-1-17

@author: LiPing
'''

from src.CommonFunctions.WangCaiOperations import WangCaiOperations
from src.CommonFunctions.DataOperations import DataOperations
from src.CommonFunctions.LogOperations import LogOperations
import unittest
import time



global driver,dbopr,logopr,action

class HelpCenterTest(unittest.TestCase):
    '''
          测试帮助中心
    '''
    
    @classmethod
    def setUpClass(cls):
        print("开始测试帮助中心")
                
        cls.dbopr=DataOperations("HelpCenterTest.xml")        
        cls.driver=WangCaiOperations()
        cls.driver.OpenWangCai()
        cls.logopr=LogOperations()
      
    @classmethod
    def tearDownClass(cls):
        print("帮助中心测试结束")
        cls.driver.QuitWangCai()

          
    def test_helpcenter(self):
        u"帮助中心的第二个导航"
          
        driver = self.driver
        dbopr = self.dbopr
        logopr = self.logopr
        assertEqual = self.assertEqual
        
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("tab", "help"))
        time.sleep(2)
        
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("tab", "second"))
        time.sleep(2)
         
        title = driver.GetWangcaiText(dbopr.readxml("method", "css"), dbopr.readxml("tab", "second"))
         
        exptitle = driver.GetWangcaiText(dbopr.readxml("method", "css"), dbopr.readxml("message", "mes1"))
        print(exptitle)
         
        if (title == exptitle):
                      
            logopr.setInfo(u"点击帮助中心第二个导航测试成功")
            assertEqual(title, exptitle, "帮助中心,测试通过")
                            
        else:
               
            logopr.setError(u"点击帮助中心第二个导航测试失败")
            assertEqual(title, exptitle, "帮助中心,测试不通过") 
                     
    
        
if __name__ == "__main__":
    unittest.main()