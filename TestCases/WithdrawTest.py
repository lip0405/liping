#-*- coding: UTF-8 -*-
'''
Created on 2019-8-26

@author: LiPing
'''

from src.CommonFunctions.WangCaiOperations import WangCaiOperations
from src.CommonFunctions.DataOperations import DataOperations
from src.CommonFunctions.LogOperations import LogOperations
import unittest
import time

global withdraw,dbopr,logopr

class WithdrawTest(unittest.TestCase):
    '''
          测试提现功能
    '''
    
    @classmethod
    def setUpClass(cls):
        print("开始测试提现功能")
                
        cls.dbopr=DataOperations("WithdrawTest.xml")        
        cls.withdraw=WangCaiOperations()
        cls.withdraw.OpenWangCai()
        cls.logopr=LogOperations()
        
        #通过优先出借的充值按钮，进入我的账户页面 
        cls.withdraw.ToMyAccount()
      
    @classmethod
    def tearDownClass(cls):
        print("提现功能测试结束")
        cls.withdraw.QuitWangCai()


    def test_withdraw_less(self):
        u"提现金额小于等于2元"
           
        #点击提现按钮
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "css"), self.dbopr.readxml("button", "withdraw"))
               
        #输入提现金额
        money = self.dbopr.readxml("money", "less")
        self.withdraw.WangcaiSendKeys(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("input", "inputmoney"), money)
        time.sleep(1)
           
        #点击确认提现
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("button", "confirm"))
        time.sleep(1)
           
        #获取弹窗提示文案
        mes = self.withdraw.GetWangcaiText(self.dbopr.readxml("method", "css"), self.dbopr.readxml("message", "mes1"))
           
        #期待正确文案
        expmes = self.dbopr.readxml("message", "mes2")
           
        if (mes == expmes):
           
            self.logopr.setInfo(u"提现金额小于等于2元,提示正确")
            self.assertEqual(mes, expmes, "提现金额小于等于2元,测试通过")
                 
        else:
    
            self.logopr.setError(u"提现金额小于等于2元,提示不正确")
            self.assertEqual(mes, expmes, "提现金额小于等于2元,测试不通过")            
            
        #点击弹窗上的确定按钮
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "css"), self.dbopr.readxml("button", "confirm2"))
        time.sleep(1)
        
    def test_withdraw_sucess(self):
        u"提现金额大于2元，小于账户余额"
          
        #点击提现按钮
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "css"), self.dbopr.readxml("button", "withdraw"))
          
        balance = self.withdraw.GetWangcaiText(self.dbopr.readxml("method", "css"), self.dbopr.readxml("message", "mes4"))
        balance = float(balance)
              
        #输入提现金额
        money = self.dbopr.readxml("money", "sucess")
        self.withdraw.WangcaiSendKeys(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("input", "inputmoney"), money)
        time.sleep(1)
          
        #点击确认提现
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("button", "confirm"))
        time.sleep(1)
          
        #获取确认提现金额弹窗中的申请提现金额
        mes = self.withdraw.GetWangcaiText(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("message", "mes3"))
           
        if (mes == money):
           
            self.logopr.setInfo(u"提现金额大于2元，小于账户余额,确认提现金额正确")
            self.assertEqual(mes, money, "提现金额大于2元，小于账户余额,确认提现金额正确")
                 
        else:
    
            self.logopr.setError(u"提现金额大于2元，小于账户余额,确认提现金额有误")
            self.assertEqual(mes, money, "提现金额大于2元，小于账户余额,确认提现金额有误")            
            
        #点击弹窗上的确定按钮
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "css"), self.dbopr.readxml("button", "confirm3"))
        time.sleep(1)
          
        #进入存管验密页面
        self.withdraw.SwitchWangCaiHandle()
        self.withdraw.WangcaiSendKeys(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("input", "password"), self.dbopr.readxml("pwd", "pwd"))       
        time.sleep(1)
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("button", "confirm4"))
        time.sleep(6)
          
        #判断提现后账户余额是否正确
        balancenew = self.withdraw.GetWangcaiText(self.dbopr.readxml("method", "css"), self.dbopr.readxml("message", "mes4"))
        balancenew = float(balancenew)
        money = round(float(money), 1)
        diff = balance - balancenew
          
        if (diff == money):
              
            self.logopr.setInfo(u"提现金额大于2元，小于账户余额,提现申请成功")
            self.assertEqual(diff, money, "提现金额大于2元，小于账户余额,测试通过")
                 
        else:
    
            self.logopr.setError(u"提现金额大于2元，小于账户余额,提现申请未成功")
            self.assertEqual(diff, money, "提现金额大于2元，小于账户余额,测试不通过")            
         
    def test_withdraw_zsucess(self):
        u"提现金额等于账户余额"
            
        #点击提现按钮
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "css"), self.dbopr.readxml("button", "withdraw"))
            
        balance = self.withdraw.GetWangcaiText(self.dbopr.readxml("method", "css"), self.dbopr.readxml("message", "mes4"))
                
        #输入提现金额
        self.withdraw.WangcaiSendKeys(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("input", "inputmoney"), balance)
        time.sleep(1)
            
        #点击确认提现
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("button", "confirm"))
        time.sleep(1)
            
        #获取确认提现金额弹窗中的申请提现金额
        mes = self.withdraw.GetWangcaiText(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("message", "mes3"))
             
        if (mes == balance):
             
            self.logopr.setInfo(u"提现金额等于账户余额,确认提现金额正确")
            self.assertEqual(mes, balance, "提现金额等于账户余额,确认提现金额正确")
                   
        else:
      
            self.logopr.setError(u"提现金额等于账户余额,确认提现金额有误")
            self.assertEqual(mes, balance, "提现金额等于账户余额,确认提现金额有误")            
              
        #点击弹窗上的确定按钮
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "css"), self.dbopr.readxml("button", "confirm3"))
        time.sleep(1)
            
        #进入存管验密页面
        self.withdraw.SwitchWangCaiHandle()
        self.withdraw.WangcaiSendKeys(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("input", "password"), self.dbopr.readxml("pwd", "pwd"))       
        time.sleep(1)
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("button", "confirm4"))
        time.sleep(6)
            
        #判断提现后账户余额是否正确
        balancenew = self.withdraw.GetWangcaiText(self.dbopr.readxml("method", "css"), self.dbopr.readxml("message", "mes4"))
        balancenew = float(balancenew)
            
        if (balancenew == 0 ):
                
            self.logopr.setInfo(u"提现金额等于账户余额,提现申请成功")
            self.assertEqual(balancenew, 0, "提现金额等于账户余额,测试通过")
                   
        else:
      
            self.logopr.setError(u"提现金额等于账户余额,提现申请未成功")
            self.assertEqual(balancenew, 0, "提现金额等于账户余额,测试不通过") 
 
 
    def test_withdraw_exceed(self):
        u"提现金额大于账户余额"
           
        #点击提现按钮
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "css"), self.dbopr.readxml("button", "withdraw"))
           
        balance = self.withdraw.GetWangcaiText(self.dbopr.readxml("method", "css"), self.dbopr.readxml("message", "mes4"))
        money = float(balance)+1
        money = str(money)
               
        #输入提现金额
        minput = self.withdraw.FindWangcaiElement(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("input", "inputmoney"))
        self.withdraw.WangcaiSendKeys(self.dbopr.readxml("method", "xpath"), self.dbopr.readxml("input", "inputmoney"), money)
        time.sleep(1)
           
        #获取弹窗提示文案
        mes = self.withdraw.GetWangcaiText(self.dbopr.readxml("method", "css"), self.dbopr.readxml("message", "mes1"))
          
        #期待正确文案
        expmes = self.dbopr.readxml("message", "mes5")
          
        if (mes == expmes):
          
            self.logopr.setInfo(u"提现金额超出账户余额,提示正确")
            self.assertEqual(mes, expmes, "提现金额超出账户余额,,测试通过")
                
        else:
   
            self.logopr.setError(u"提现金额超出账户余额,,提示不正确")
            self.assertEqual(mes, expmes, "提现金额超出账户余额,,测试不通过")            
           
        #点击弹窗上的确定按钮
        self.withdraw.WangcaiElemClick(self.dbopr.readxml("method", "css"), self.dbopr.readxml("button", "confirm2"))
        minput.clear()
        time.sleep(1)
        
        
        
if __name__ == "__main__":
    unittest.main()