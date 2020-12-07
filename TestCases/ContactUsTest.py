#-*- coding: UTF-8 -*-
'''
Created on 2019-11-20

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
          测试侧边栏的联系我们
    '''
    
    @classmethod
    def setUpClass(cls):
        print("开始测试侧边栏的联系我们")
                
        cls.dbopr=DataOperations("ContactUsTest.xml")        
        cls.driver=WangCaiOperations()
        cls.driver.OpenWangCai()
        cls.logopr=LogOperations()
        
      
    @classmethod
    def tearDownClass(cls):
        print("侧边栏的联系我们测试结束")
        cls.driver.QuitWangCai()

          
    def test_help(self):
        u"联系我们-帮助中心"
           
        driver = self.driver
        dbopr = self.dbopr
        logopr = self.logopr
        assertEqual = self.assertEqual 

        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "help"))
        time.sleep(5)
         
               
        #获取页面标题      
        driver.WcSwitchHandles(-2)
        title = driver.WangcaiBrowserTitle()
                           
        #期待正确标题
        exptitle = dbopr.readxml("message", "exptitle")
                     
        if (title == exptitle):
                     
            logopr.setInfo(u"点击联系我们中帮助中心测试成功")
            assertEqual(title, exptitle, "点击联系我们中帮助中心,测试通过")
                           
        else:
              
            logopr.setError(u"点击联系我们中帮助中心测试失败")
            assertEqual(title, exptitle, "点击联系我们中帮助中心,测试不通过")   
           
            
    def test_consult(self):
        u"联系我们-点击咨询"
           
        driver = self.driver
        dbopr = self.dbopr
        logopr = self.logopr
        assertEqual = self.assertEqual
 
        contact = driver.FindWangcaiElement(dbopr.readxml("method", "css"),dbopr.readxml("button", "contact"))
        driver.WangcaiActionChains(contact)
        time.sleep(2)
         
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "consult"))
        time.sleep(5)
         
               
        #获取页面标题    
        driver.SwitchWangCaiHandle()
        time.sleep(5)
        title = driver.WangcaiBrowserTitle()
                           
        #期待正确标题
        exptitle = dbopr.readxml("message", "exptitle2")
                      
        if (title == exptitle):
                      
            logopr.setInfo(u"点击咨询测试成功")
            assertEqual(title, exptitle, "点击咨询,测试通过")
                            
        else:
               
            logopr.setError(u"点击咨询测试失败")
            assertEqual(title, exptitle, "点击咨询,测试不通过")   
            
        driver.WcSwitchHandles(0)
        time.sleep(2)
 
        
if __name__ == "__main__":
    unittest.main()