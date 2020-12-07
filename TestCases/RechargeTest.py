#-*- coding: UTF-8 -*-
'''
Created on 2019-8-13

@author: LiPing
'''

from src.CommonFunctions.WangCaiOperations import WangCaiOperations
from src.CommonFunctions.DataOperations import DataOperations
from src.CommonFunctions.LogOperations import LogOperations
import unittest
import time

global recharge,dbopr,logopr

class RechargeTest(unittest.TestCase):
    '''
          测试充值功能
    '''
    
    @classmethod
    def setUpClass(cls):
        print("开始测试充值功能")
                
        cls.dbopr=DataOperations("RechargeTest.xml")        
        cls.recharge=WangCaiOperations()
        cls.recharge.OpenWangCai()
        cls.logopr=LogOperations()
        
        #通过优先出借，进入充值页面 
        cls.recharge.ToMyAccount()
      
    @classmethod
    def tearDownClass(cls):
        print("充值功能测试结束")
        cls.recharge.QuitWangCai()


    def test_recharge_fastpaymet(self):
        u"快捷支付充值1000元"
                     
        #输入充值金额
        money = self.dbopr.readxml("res", "price")
        self.recharge.WangcaiSendKeys(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("bank", "input"), money)
        time.sleep(2)
            
        #判断页面上充值后余额计算是否正确
        recprice = self.recharge.BalanceAdd()[0]
        balanceadd = self.recharge.BalanceAdd()[1]
    
        if (recprice == money):
   
            self.logopr.setInfo(u"快捷支付，充值后余额计算正确")
            self.assertEqual(recprice, money, "快捷支付，充值后余额计算正确")
                
        else:
   
            self.logopr.setError(u"快捷支付，充值后余额计算不正确")
            self.assertEqual(recprice, money, "快捷支付，充值后余额计算不正确")            
            
        #点击充值按钮
        self.recharge.ClickRecharge()
        self.recharge.SwitchWangCaiHandle()
            
        #存管验密页面
        self.recharge.GatewayRecevice()
        self.recharge.GatewayRecharge(self.dbopr.readxml("res","verification"))
        self.recharge.RechargePassward(self.dbopr.readxml("res","password"))
   
        #再次进入充值页面，查看最新余额，判断是否充值成功
        balancenew = self.recharge.BalanceNew()
    
        if (balancenew == balanceadd):
   
            self.logopr.setInfo(u"快捷支付，测试通过")
            self.assertEqual(balancenew, balanceadd, "快捷支付，测试通过")
               
        else:
   
            self.logopr.setError(u"快捷支付，测试不通过")
            self.assertEqual(balancenew, balanceadd, "快捷支付，测试不通过")
              
           
         
    def test_recharge_less(self):
        u"输入充值金额小于5元"
                     
        #输入充值金额
        money = self.dbopr.readxml("less", "price")
        self.recharge.WangcaiSendKeys(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("bank", "input"), money)
        time.sleep(2)
             
        #判断页面上充值后余额计算是否正确
        recprice = self.recharge.BalanceAdd()[0]                 
    
        if (recprice == money):
   
            self.logopr.setInfo(u"金额小于5元，充值后余额计算正确")
            self.assertEqual(recprice, money, "金额小于5元，充值后余额计算正确")
                
        else:
   
            self.logopr.setError(u"金额小于5元，充值后余额计算不正确")
            self.assertEqual(recprice, money, "金额小于5元，充值后余额计算不正确")    
             
        #点击充值按钮    
        self.recharge.ClickRecharge()
             
        #判断提示是否正确
        rechargemes = self.recharge.GetWangcaiText(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("less", "mes"))       
        
        if (rechargemes == "充值金额不能小于5元或大于等于一千万"):
   
            self.logopr.setInfo(u"金额小于5元，测试通过")
            self.assertEqual(rechargemes, "充值金额不能小于5元或大于等于一千万", "金额小于5元，提示文案正确")
               
        else:
   
            self.logopr.setInfo(u"金额小于5元，测试不通过")
            self.assertEqual(rechargemes, "充值金额不能小于5元或大于等于一千万", "金额小于5元，提示文案不正确") 
              
        self.recharge.WangcaiElemClick(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("setup", "btn"))           
      
                  
    def test_recharge_ecurrency(self):
        u"网银支付充值100元"
                    
        money = self.dbopr.readxml("bank", "price")
            
        #选择网银充值
        self.recharge.EcurrencyPayment()
            
        #输入充值金额
        self.recharge.WangcaiSendKeys(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("bank", "input"), self.dbopr.readxml("bank", "price"))
        time.sleep(2)
            
        #判断页面上充值后余额计算是否正确
        recprice = self.recharge.BalanceAdd()[0]
        balanceadd = self.recharge.BalanceAdd()[1]
   
        if (recprice == money):
   
            self.logopr.setInfo(u"网银支付，充值后余额计算正确")
            self.assertEqual(recprice, money, "网银支付，充值后余额计算正确")
               
        else:
   
            self.logopr.setError(u"网银支付，充值后余额计算不正确")
            self.assertEqual(recprice, money, "网银支付，充值后余额计算不正确")
            
        #点击充值按钮
        self.recharge.ClickRecharge()
        self.recharge.SwitchWangCaiHandle()
            
        #点击模拟支付成功
        self.recharge.SimulatedPayment()
              
        #再次进入充值页面，查看最新余额，判断是否充值成功
        balancenew = self.recharge.BalanceNew()
   
        if (balancenew == balanceadd):
   
            self.logopr.setInfo(u"网银支付，测试通过")
            self.assertEqual(balancenew, balanceadd, "网银支付，测试通过")
               
        else:
   
            self.logopr.setError(u"网银支付，测试不通过")
            self.assertEqual(balancenew, balanceadd, "网银支付，测试不通过")   
             
    def test_recharge_overlimit(self):
        u"输入充值金额超出单笔限额"
  
          
        #获取当前单笔限额
        overlimit = self.recharge.GetWangcaiText(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("overlimit", "money"))
        print(overlimit)
        overlimit = float(overlimit.split("值")[1].split("元")[0])
        print(overlimit)
        
        #输入充值金额
        money = str(overlimit + 1)
        self.recharge.WangcaiSendKeys(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("bank", "input"), money)
        time.sleep(2)
             
        #判断页面上充值后余额计算是否正确
        recprice = self.recharge.BalanceAdd()[0]  
        recprice = round(float(recprice), 2)
        recprice = str(recprice)       
    
        if (recprice == money):
   
            self.logopr.setInfo(u"金额超出单笔限额，充值后余额计算正确")
            self.assertEqual(recprice, money, "金额超出单笔限额，充值后余额计算正确")
                
        else:
   
            self.logopr.setError(u"金额超出单笔限额，充值后余额计算不正确")
            self.assertEqual(recprice, money, "金额超出单笔限额，充值后余额计算不正确")    
             
        #点击充值按钮    
        self.recharge.ClickRecharge()
             
        #判断提示是否正确
        rechargemes = self.recharge.GetWangcaiText(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("less", "mes"))       
        
        if (rechargemes == "超出单笔限额" or rechargemes == "超出单天限额"):
   
            self.logopr.setInfo(u"超出单笔限额，测试通过")
            self.assertEqual(1, 1, "超出单笔限额，提示文案正确")
               
        else:
   
            self.logopr.setInfo(u"超出单笔限额，测试不通过")
            self.assertEqual(1, 1, "超出单笔限额，提示文案不正确")  
             
        self.recharge.WangcaiElemClick(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("setup", "btn"))   

    def test_recharge_ovdaylimit(self):
        u"输入充值金额超出单天限额"
 
         
        #获取当前单天限额
        overlimit = self.recharge.GetWangcaiText(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("overlimit", "money"))
        print(overlimit)
        overlimit = float(overlimit.split("值")[-1].split("元")[0])
        print(overlimit)
                                   
        #输入充值金额
        money = str(overlimit + 1)
        self.recharge.WangcaiSendKeys(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("bank", "input"), money)
        time.sleep(2)
             
        #判断页面上充值后余额计算是否正确
        recprice = self.recharge.BalanceAdd()[0]    
        recprice = round(float(recprice), 2)
        recprice = str(recprice)     
    
        if (recprice == money):
   
            self.logopr.setInfo(u"金额超出单天限额，充值后余额计算正确")
            self.assertEqual(recprice, money, "金额超出单天限额，充值后余额计算正确")
                
        else:
   
            self.logopr.setError(u"金额超出单天限额，充值后余额计算不正确")
            self.assertEqual(recprice, money, "金额超出单天限额，充值后余额计算不正确")    
             
        #点击充值按钮    
        self.recharge.ClickRecharge()
             
        #判断提示是否正确
        rechargemes = self.recharge.GetWangcaiText(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("less", "mes"))       
        
        if (rechargemes == "超出单笔限额" or rechargemes == "超出单天限额"):
   
            self.logopr.setInfo(u"超出单天限额，测试通过")
            self.assertEqual(1, 1, "超出单天限额，提示文案正确")
               
        else:
   
            self.logopr.setInfo(u"超出单天限额，测试不通过")
            self.assertEqual(1, 1, "超出单天限额，提示文案不正确")
            
        self.recharge.WangcaiElemClick(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("setup", "btn"))

    def test_recharge_decimal(self):
        u"充值金额带有小数"
           
        #输入充值金额
        money = self.dbopr.readxml("decimal", "money")
        self.recharge.WangcaiSendKeys(self.dbopr.readxml("setup", "method"), self.dbopr.readxml("bank", "input"), money)
        time.sleep(2)
            
        #判断页面上充值后余额计算是否正确
        recprice = self.recharge.BalanceAdd()[0]
        recprice = round(float(recprice), 2)
        recprice = str(recprice)
        balanceadd = self.recharge.BalanceAdd()[1]
    
        if (recprice == money):
   
            self.logopr.setInfo(u"小数充值后余额计算正确")
            self.assertEqual(recprice, money, "小数充值后余额计算正确")
                
        else:
   
            self.logopr.setError(u"小数充值后余额计算不正确")
            self.assertEqual(recprice, money, "小数充值后余额计算不正确")            
            
        #点击充值按钮
        self.recharge.ClickRecharge()
        self.recharge.SwitchWangCaiHandle()
            
        #存管验密页面
        self.recharge.GatewayRecevice()
        self.recharge.GatewayRecharge(self.dbopr.readxml("res","verification"))
        self.recharge.RechargePassward(self.dbopr.readxml("res","password"))
        time.sleep(4)
   
        #再次进入充值页面，查看最新余额，判断是否充值成功
        balancenew = self.recharge.BalanceNew()
    
        if (balancenew == balanceadd):
   
            self.logopr.setInfo(u"充值小数，测试通过")
            self.assertEqual(balancenew, balanceadd, "充值小数，测试通过")
               
        else:
   
            self.logopr.setError(u"充值小数，测试不通过")
            self.assertEqual(balancenew, balanceadd, "充值小数，测试不通过")



if __name__ == "__main__":
    unittest.main()