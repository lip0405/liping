#-*- coding: UTF-8 -*-
'''
Created on 2019-11-29

@author: LiPing
'''

from src.CommonFunctions.WangCaiOperations import WangCaiOperations
from src.CommonFunctions.DataOperations import DataOperations
from src.CommonFunctions.LogOperations import LogOperations
import unittest
import time



global driver,dbopr,logopr,action

class ContactUsTest(unittest.TestCase):
    '''
          测试旺财记事
    '''
    
    @classmethod
    def setUpClass(cls):
        print("开始测试旺财记事")
                
        cls.dbopr=DataOperations("DiaryTest.xml")        
        cls.driver=WangCaiOperations()
        cls.driver.OpenWangCai()
        cls.logopr=LogOperations()
      
    @classmethod
    def tearDownClass(cls):
        print("旺财记事测试结束")
        cls.driver.QuitWangCai()

          
    def test_diary(self):
        u"旺财日记"
          
        driver = self.driver
        dbopr = self.dbopr
        logopr = self.logopr
        assertEqual = self.assertEqual
        
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("tab", "diary"))
        time.sleep(2)
        
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("tab", "diarydate"))
        time.sleep(2)
        
        diarydate = driver.GetWangcaiText(dbopr.readxml("method", "xpath"), dbopr.readxml("tab", "diarydate"))
        
        titledate = driver.GetWangcaiText(dbopr.readxml("method", "css"), dbopr.readxml("message", "mes1"))
        titledate = titledate[0:4]
        
        if (diarydate == titledate):
                     
            logopr.setInfo(u"点击旺财日记及二级tab测试成功")
            assertEqual(diarydate, titledate, "旺财日记,测试通过")
                           
        else:
              
            logopr.setError(u"点击旺财日记及二级tab测试失败")
            assertEqual(diarydate, titledate, "旺财日记,测试不通过") 
                     

    def test_richman(self):
        u"财主见面会"
          
        driver = self.driver
        dbopr = self.dbopr
        logopr = self.logopr
        assertEqual = self.assertEqual
        
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("tab", "richman"))
        time.sleep(2)
        
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("tab", "richdata"))
        time.sleep(2)
              
        richdate = driver.GetWangcaiText(dbopr.readxml("method", "xpath"), dbopr.readxml("tab", "richdata"))
        
        titledate = driver.GetWangcaiText(dbopr.readxml("method", "css"), dbopr.readxml("message", "mes2"))
        titledate = titledate[0:4]
        
        if (richdate == titledate):
                     
            logopr.setInfo(u"点击财主见面会及二级tab测试成功")
            assertEqual(richdate, titledate, "财主见面会,测试通过")
                           
        else:
              
            logopr.setError(u"点击财主见面会及二级tab测试失败")
            assertEqual(richdate, titledate, "财主见面会,测试不通过")
   
    
        
if __name__ == "__main__":
    unittest.main()