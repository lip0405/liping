#-*- coding: UTF-8 -*-
'''
Created on 2020-1-15

@author: LiPing
'''

from src.CommonFunctions.WangCaiOperations import WangCaiOperations
from src.CommonFunctions.DataOperations import DataOperations
from src.CommonFunctions.LogOperations import LogOperations
import unittest
import time


global driver,dbopr,logopr

class ChangeLoginpwdTest(unittest.TestCase):
    '''
          测试账户设置模块
    '''
    
    @classmethod
    def setUpClass(cls):
        print("开始测试账户设置-修改登录密码")
                
        cls.dbopr=DataOperations("ChangeLoginpwdTest.xml")        
        cls.driver=WangCaiOperations()
        cls.driver.OpenWangCai()
        cls.logopr=LogOperations()
        
        #通过优先出借的充值按钮，进入我的账户页面 
        cls.driver.ToMyAccount()
        cls.driver.ScrollWangCaiPage(130)
        #点击账户设置
        cls.driver.WangcaiElemClick(cls.dbopr.readxml("method", "css"), cls.dbopr.readxml("button", "account"))
        time.sleep(2)
        
      
    @classmethod
    def tearDownClass(cls):
        print("账户设置-修改登录密码测试结束")
        cls.driver.QuitWangCai()



    def test_loginpwd_edit(self):
        u"修改登录密码"
  
        driver = self.driver
        dbopr = self.dbopr
        logopr = self.logopr
        assertEqual = self.assertEqual
              
        #点击登录密码的修改按钮
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "loginedit"))
        time.sleep(2)

        #处理iframe
        iframe = driver.FindWangcaiElement(dbopr.readxml("method", "css"), dbopr.readxml("iframe", "frame"))
        driver.SwitchtoWcFrame(iframe)
        
        #输入旧密码
        oldpwd = dbopr.readxml("pwd", "oldloginpwd")
        driver.WangcaiSendKeys(dbopr.readxml("method", "xpath"), dbopr.readxml("input", "oldpwd"), oldpwd)
        #输入新密码
        newpwd = dbopr.readxml("pwd", "newloginpwd")
        driver.WangcaiSendKeys(dbopr.readxml("method", "xpath"), dbopr.readxml("input", "newpwd"), newpwd)
        time.sleep(1)
              
        #点击确认按钮
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "confirm"))
        time.sleep(8)
              
        #获取弹窗提示文案
        mes = driver.GetWangcaiText(dbopr.readxml("method", "xpath"), dbopr.readxml("message", "mes1"))
              
        #期待正确文案
        expmes = dbopr.readxml("message", "mes2")
              
        if (mes == expmes):
              
            logopr.setInfo(u"登录密码修改成功")
            assertEqual(mes, expmes, "修改登录密码,测试通过")
                    
        else:
       
            logopr.setError(u"登录密码修改失败")
            assertEqual(mes, expmes, "修改登录密码,测试不通过")         
       
        
    
       
        
if __name__ == "__main__":
    unittest.main()