#-*- coding: UTF-8 -*-
'''
Created on 2019-9-9

@author: LiPing
'''

from src.CommonFunctions.WangCaiOperations import WangCaiOperations
from src.CommonFunctions.DataOperations import DataOperations
from src.CommonFunctions.LogOperations import LogOperations
import unittest
import time


global driver,dbopr,logopr

class RiskTest(unittest.TestCase):
    '''
          测试风险测评
    '''
    
    @classmethod
    def setUpClass(cls):
        print("开始测试风险测评")
                
        cls.dbopr=DataOperations("RiskTest.xml")        
        cls.driver=WangCaiOperations()
        cls.driver.OpenWangCai()
        cls.logopr=LogOperations()
        
        #通过优先出借的充值按钮，进入我的账户页面 
        cls.driver.ToMyAccount()
        cls.driver.ScrollWangCaiPage(130)
        #点击风险测评
        cls.driver.WangcaiElemClick(cls.dbopr.readxml("method", "css"), cls.dbopr.readxml("button", "risk"))
        time.sleep(2)
        
      
    @classmethod
    def tearDownClass(cls):
        print("风险测评模块测试结束")
        cls.driver.QuitWangCai()

          
    def test_risk(self):
        u"选择风险测评选项"
          
        driver = self.driver
        dbopr = self.dbopr
        logopr = self.logopr
        assertEqual = self.assertEqual
        
        time.sleep(1)
        driver.ScrollWangCaiPage(100)
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "reset"))
        time.sleep(2)

               
        #选择风险测评选项
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "q1"))
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "q2"))
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "q3"))
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "q4"))
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "q5"))
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "q6"))
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "q7"))
        time.sleep(2)        
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "q8"))
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "q9"))
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "q10"))
        time.sleep(2)
        
               
        #点击提交按钮
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "commit"))
        time.sleep(2)     
        driver.ScrollWangCaiPage(80)
        time.sleep(4)
               
        #获取提示文案
        mes = driver.GetWangcaiText(dbopr.readxml("method", "css"), dbopr.readxml("message", "resault"))
                 
        #期待正确文案
        expmes = dbopr.readxml("message", "expres")
                  
        if (mes == expmes):
                  
            logopr.setInfo(u"风险测评重新测试成功")
            assertEqual(mes, expmes, "风险测评重新测试,测试通过")
                        
        else:
           
            logopr.setError(u"风险测评重新测试失败")
            assertEqual(mes, expmes, "风险测评重新测试,测试不通过")   
  
 
        
    
       
        
if __name__ == "__main__":
    unittest.main()