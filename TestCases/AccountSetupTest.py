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

class AccountSetupTest(unittest.TestCase):
    '''
          测试账户设置模块
    '''
    
    @classmethod
    def setUpClass(cls):
        print("开始测试账户设置模块")
                
        cls.dbopr=DataOperations("AccountSetupTest.xml")        
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
        print("账户设置模块测试结束")
        cls.driver.QuitWangCai()

       
    def test_atradepwd_edit(self):
        u"修改交易密码"
             
        driver = self.driver
        dbopr = self.dbopr
        logopr = self.logopr
        assertEqual = self.assertEqual
                  
        #点击交易密码的修改按钮
        driver.SwitchWangCaiHandle()
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "trade"))
        time.sleep(2)
                      
        #点击我记得原密码
        driver.SwitchWangCaiHandle()
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "remember"))
        #输入原密码
        driver.SwitchWangCaiHandle()
        oldpwd = dbopr.readxml("pwd", "oldtradepwd")
        driver.WangcaiSendKeys(dbopr.readxml("method", "css"),dbopr.readxml("input", "oldtrpwd"), oldpwd)
        time.sleep(1)
                       
        #输入新密码
        newpwd = dbopr.readxml("pwd", "newtradepwd")
        driver.WangcaiSendKeys(dbopr.readxml("method", "css"), dbopr.readxml("input", "newtrpwd"), newpwd)
        time.sleep(1)
               
        #再次输入新密码
        driver.WangcaiSendKeys(dbopr.readxml("method", "css"), dbopr.readxml("input", "agpwd"), newpwd)        
        time.sleep(1)
                  
        #点击确认按钮
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "confirm2"))
        time.sleep(4)
                  
        #获取提示文案
        mes = driver.GetWangcaiText(dbopr.readxml("method", "css"), dbopr.readxml("message", "mes3"))
                   
        #期待正确文案
        expmes = dbopr.readxml("message", "mes4")
                   
        if (mes == expmes):
                   
            logopr.setInfo(u"交易密码修改成功")
            assertEqual(mes, expmes, "修改交易密码,测试通过")
                         
        else:
            
            logopr.setError(u"交易密码修改失败")
            assertEqual(mes, expmes, "修改交易密码,测试不通过")   
     
    def test_bank(self):
        u"点击更换银行卡"
             
        driver = self.driver
        dbopr = self.dbopr
        logopr = self.logopr
        assertEqual = self.assertEqual
                   
        #点击更换银行卡按钮
        time.sleep(1)
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "bank"))
        time.sleep(2)
                   
        #获取提示文案
        mes = driver.GetWangcaiText(dbopr.readxml("method", "css"), dbopr.readxml("message", "mes5"))
                    
        #期待正确文案
        expmes = dbopr.readxml("message", "mes6")
                    
        if (mes == expmes):
                    
            logopr.setInfo(u"点击更换银行卡，弹窗提示正确")
            assertEqual(mes, expmes, "点击更换银行卡,测试通过")
                          
        else:
             
            logopr.setError(u"点击更换银行卡，未弹出正确弹窗提示")
            assertEqual(mes, expmes, "点击更换银行卡,测试不通过")   
                  
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "confirm3"))   
        time.sleep(2)
    
    u"无法写断言，返回文案取不到，账户设置页面上返回的信息是：办理银行卡时预留的手机号,也无法判断"
    def test_phone(self):
        u"更换预留手机号"
             
        driver = self.driver
        dbopr = self.dbopr
                    
        #点击更新按钮
        time.sleep(1)
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "update"))       
        time.sleep(2)
              
        #输入新的手机号
        driver.WangcaiSendKeys(dbopr.readxml("method", "css"), dbopr.readxml("input", "phone"), dbopr.readxml("content", "tel"))
              
        #点击确定按钮
        time.sleep(1)
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "confirm4"))
              
        #点击获取验证码
        time.sleep(2)
        driver.SwitchWangCaiHandle()
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "vercode"))
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "known"))
              
        #输入验证码
        time.sleep(1)
        driver.WangcaiSendKeys(dbopr.readxml("method", "css"), dbopr.readxml("input", "sms"), dbopr.readxml("pwd", "pwd"))
              
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "confirm2"))
        time.sleep(3)  
            
    
    def testauthorize(self):
        u"用户授权"
             
        driver = self.driver
        dbopr = self.dbopr
        logopr = self.logopr
        assertEqual = self.assertEqual
             
        #点击重新授权
        driver.SwitchWangCaiHandle()
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "auth"))
        time.sleep(2)
              
        #存管页面
        driver.SwitchWangCaiHandle()
        pwd = dbopr.readxml("pwd", "pwd")
        driver.WangcaiSendKeys(dbopr.readxml("method", "css"), dbopr.readxml("input", "trapwd"), pwd)
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "agree"))
        time.sleep(2)
        driver.WangcaiElemClick(dbopr.readxml("method", "css"), dbopr.readxml("button", "confrim5"))
        time.sleep(4)
             
        #获取返回文案
        driver.SwitchWangCaiHandle()
        mes = driver.GetWangcaiText(dbopr.readxml("method", "css"), dbopr.readxml("message", "mes9"))
             
        expmes = dbopr.readxml("message", "mes10")
             
        if (mes == expmes):
            logopr.setInfo(u"授权返回文案正确")
            assertEqual(mes, expmes, "用户重新授权测试通过")
                 
        else:
            logopr.setInfo(u"授权返回文案错误")
            assertEqual(mes, expmes, "用户重新授权测试不通过")
    
           
                          
    def testprotocol(self):
        u"查看《91旺财隐私政策》"
            
        driver = self.driver
        dbopr = self.dbopr
        assertEqual = self.assertEqual
        logopr = self.logopr
            
        #点击查看按钮
        time.sleep(3)
        driver.WangcaiElemClick(dbopr.readxml("method", "xpath"), dbopr.readxml("button", "view")) 
        time.sleep(3)      
           
        driver.SwitchWangCaiHandle()
        title = driver.WangcaiBrowserTitle()
           
        exptitle = dbopr.readxml("message", "exptitle")
           
        if (title == exptitle):
            logopr.setInfo(u"《91旺财隐私政策》打开正确")
            assertEqual(title, exptitle, "查看《91旺财隐私政策》测试通过")
                  
        else:
            logopr.setInfo(u"《91旺财隐私政策》打开有误")
            assertEqual(title, exptitle, "查看《91旺财隐私政策》测试不通过")
             
        
            
        
        
       
        
    
       
        
if __name__ == "__main__":
    unittest.main()