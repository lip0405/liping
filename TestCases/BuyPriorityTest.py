#-*- coding: UTF-8 -*-
'''
Created on 2019-7-28

@author: LiPing
'''

from decimal import Decimal
from src.CommonFunctions.WangCaiOperations import WangCaiOperations
from src.CommonFunctions.DataOperations import DataOperations
from src.CommonFunctions.LogOperations import LogOperations
import unittest
import time

global priority,dbopr,logopr

class BuypriorityTest(unittest.TestCase):
    '''
          测试加入优先出借功能
    '''
    
    @classmethod
    def setUpClass(cls):
        print("开始测试加入优先出借")
        cls.dbopr=DataOperations("BuyPriorityTest.xml")
        cls.logopr=LogOperations()
        cls.priority=WangCaiOperations()
        cls.priority.OpenWangCai()
        
    @classmethod
    def tearDownClass(cls):
        print("加入优先出借测试结束")
        cls.priority.QuitWangCai()
       
    def test_buy_priority_success(self):
        u"加入优先出借1000元"
          
        #进入项目列表页
        self.priority.ClickProductList()        
        priority_list_name =self.priority.GetWangcaiText(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "name"))       
 
        if (priority_list_name == "优先出借"):
             
            self.logopr.setInfo(u"跳转到优先出借列表成功")
            self.assertEqual(priority_list_name, "优先出借", "跳转到优先出借列表成功")
             
        else:
 
            self.logopr.setError(u"跳转到优先出借列表失败")
            self.assertEqual(priority_list_name, "优先出借", "跳转到优先出借列表失败")
                                    
        self.priority.ScrollWangCaiPage(self.dbopr.readxml("priority", "scroll"))
          
        #点击优先出借
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "priority"))
          
        #输入购买金额，并确定
        self.priority.WangcaiSendKeys(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "input"), self.dbopr.readxml("priority", "price"))
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("less", "button"))
 
         
        #点击下一步，并确定
        self.priority.ClickNext()
        self.priority.ComfirmButton()
          
        #判断是否购买成功
        resault = self.priority.GetWangcaiText(self.dbopr.readxml("overflow", "method"), self.dbopr.readxml("priority", "message"))
 
        if (resault == "加入成功!"):
             
            self.logopr.setInfo(u"购买1000元优先出借，测试通过")
            self.assertEqual(resault, "加入成功!", "购买1000元优先出借，测试通过")
             
        else:
 
            self.logopr.setError(u"优先出借1000元加入，测试不通过")
            self.assertEqual(resault, "加入成功!", "优先出借1000元加入，测试不通过")             

    def test_buy_priority_award(self):
        u"加入优先出借时使用红包"
          
        #进入项目列表页
        self.priority.ClickProductList()        
        priority_list_name = self.priority.GetWangcaiText(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "name")) 
 
        if (priority_list_name == "优先出借"):
              
            self.logopr.setInfo(u"跳转到优先出借列表成功")
            self.assertEqual(priority_list_name, "优先出借", "跳转到优先出借列表成功")
              
        else:
  
            self.logopr.setError(u"跳转到优先出借列表失败")
            self.assertEqual(priority_list_name, "优先出借", "跳转到优先出借列表失败")
            
        self.priority.ScrollWangCaiPage(self.dbopr.readxml("priority", "scroll"))
          
        #点击优先出借
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "priority"))
          
        #输入购买金额，并确定
        self.priority.WangcaiSendKeys(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "input"), self.dbopr.readxml("priority", "price"))
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("less", "button"))
          
        #勾选红包
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("award", "award"))
        time.sleep(1)
        self.priority.ScrollWangCaiPage(self.dbopr.readxml("coupon", "scroll"))
          
        #点击下一步，并确定
        self.priority.ClickNext()
        self.priority.ComfirmButton()
          
        #判断是否购买成功
        resault = self.priority.GetWangcaiText(self.dbopr.readxml("overflow", "method"), self.dbopr.readxml("priority", "message"))
 
        if (resault == "加入成功!"):
              
            self.logopr.setInfo(u"使用红包加入优先出借，测试通过")
            self.assertEqual(resault, "加入成功!", "使用红包加入优先出借，测试通过")
              
        else:
  
            self.logopr.setError(u"使用红包加入优先出借，测试不通过")
            self.assertEqual(resault, "加入成功!", "使用红包加入优先出借，测试不通过") 
       
    def test_buy_priority_coupon(self):
        u"加入优先出借时使用加息券"
          
        #进入项目列表页
        self.priority.ClickProductList()        
        priority_list_name = self.priority.GetWangcaiText(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "name"))       
 
        if (priority_list_name == "优先出借"):
               
            self.logopr.setInfo(u"跳转到优先出借列表成功")
            self.assertEqual(priority_list_name, "优先出借", "跳转到优先出借列表成功")
               
        else:
   
            self.logopr.setError(u"跳转到优先出借列表失败")
            self.assertEqual(priority_list_name, "优先出借", "跳转到优先出借列表失败")
            
        self.priority.ScrollWangCaiPage(self.dbopr.readxml("priority", "scroll"))
          
        #点击优先出借
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "priority"))
          
        #输入购买金额，并确定
        self.priority.WangcaiSendKeys(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "input"), self.dbopr.readxml("priority", "price"))
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("less", "button"))
          
        #选择加息券
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("coupon", "coupon"))
        time.sleep(1)
        self.priority.ScrollWangCaiPage(self.dbopr.readxml("coupon", "scroll"))
          
        #点击下一步，并确定
        self.priority.ClickNext()
        self.priority.ComfirmButton()
          
        #判断是否购买成功
        resault = self.priority.GetWangcaiText(self.dbopr.readxml("overflow", "method"), self.dbopr.readxml("priority", "message"))
 
        if (resault == "加入成功!"):
              
            self.logopr.setInfo(u"使用加息券加入优先出借，测试通过")
            self.assertEqual(resault, "加入成功!", "使用加息券加入优先出借，测试通过")
              
        else:
  
            self.logopr.setError(u"使用加息券加入优先出借，测试不通过")
            self.assertEqual(resault, "加入成功!", "使用加息券加入优先出借，测试不通过") 
    
    def test_buy_priority_less(self):
        u"加入优先出借时金额填写小于1000元"
          
        #进入项目列表页
        self.priority.ClickProductList()        
        priority_list_name = self.priority.GetWangcaiText(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "name"))   
 
        if (priority_list_name == "优先出借"):
              
            self.logopr.setInfo(u"跳转到优先出借列表成功")
            self.assertEqual(priority_list_name, "优先出借", "跳转到优先出借列表成功")
              
        else:
  
            self.logopr.setError(u"跳转到优先出借列表失败")
            self.assertEqual(priority_list_name, "优先出借", "跳转到优先出借列表失败")
            
        self.priority.ScrollWangCaiPage(self.dbopr.readxml("priority", "scroll"))
          
        #点击优先出借
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "priority"))
          
        #输入购买金额
        self.priority.WangcaiSendKeys(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "input"), self.dbopr.readxml("less", "price"))
          
        #判断按钮状态
        addbtn = self.priority.GetBtnStatus(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("less", "button"))

        if (addbtn == False):
              
            self.logopr.setInfo(u"金额小于1000元，测试通过")
            self.assertEqual(addbtn, False, "金额小于1000元，测试通过")
              
        else:
  
            self.logopr.setError(u"金额小于1000元，测试不通过")
            self.assertEqual(addbtn, False, "金额小于1000元，测试不通过")
            
    def test_buy_priority_decimal(self):
        u"加入优先出借金额带有小数"
         
        #进入项目列表页
        self.priority.ClickProductList()        
        priority_list_name =self.priority.GetWangcaiText(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "name"))

        if (priority_list_name == "优先出借"):
              
            self.logopr.setInfo(u"跳转到优先出借列表成功")
            self.assertEqual(priority_list_name, "优先出借", "跳转到优先出借列表成功")
              
        else:
  
            self.logopr.setError(u"跳转到优先出借列表失败")
            self.assertEqual(priority_list_name, "优先出借", "跳转到优先出借列表失败")
           
        self.priority.ScrollWangCaiPage(self.dbopr.readxml("priority", "scroll"))
         
        #点击优先出借
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "priority"))
         
        #输入购买金额，并确定
        self.priority.WangcaiSendKeys(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "input"), self.dbopr.readxml("decimal", "price"))
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("less", "button"))
         
        #点击下一步，并确定
        self.priority.ClickNext()
        self.priority.ComfirmButton()
         
        #判断是否购买成功
        resault = self.priority.GetWangcaiText(self.dbopr.readxml("overflow", "method"), self.dbopr.readxml("priority", "message"))
        
        if (resault == "加入成功!"):
              
            self.logopr.setInfo(u"金额带有小数，测试通过")
            self.assertEqual(resault, "加入成功!", "金额带有小数，测试通过")
              
        else:
  
            self.logopr.setError(u"金额带有小数，测试不通过")
            self.assertEqual(resault, "加入成功!", "金额带有小数，测试不通过")

            
    def test_buy_priority_overflow(self):
        u"加入优先出借金额超出可出借金额"
        
        #进入项目列表页
        self.priority.ClickProductList()        
        priority_list_name = self.priority.GetWangcaiText(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "name"))     

        if (priority_list_name == "优先出借"):
              
            self.logopr.setInfo(u"跳转到优先出借列表成功")
            self.assertEqual(priority_list_name, "优先出借", "跳转到优先出借列表成功")
              
        else:
  
            self.logopr.setError(u"跳转到优先出借列表失败")
            self.assertEqual(priority_list_name, "优先出借", "跳转到优先出借列表失败")
                       
        self.priority.ScrollWangCaiPage(self.dbopr.readxml("priority", "scroll"))
        
        #点击优先出借
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "priority"))
        
        #获取当前可出借金额
        remprice=self.priority.GetWangcaiText(self.dbopr.readxml("overflow", "method"), self.dbopr.readxml("overflow", "price")) 
        remprice=remprice[:-1]
        remprice = Decimal(remprice).quantize(Decimal('0.00'))+1
        remprice = str(remprice)
        
        #输入购买金额，并确定
        self.priority.WangcaiSendKeys(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("priority", "input"), remprice)
        self.priority.WangcaiElemClick(self.dbopr.readxml("priority", "method"), self.dbopr.readxml("less", "button"))       
        self.priority.ClickNext()
        
        #判断弹窗提示是否正确
        ovflowmes = self.priority.GetWangcaiText(self.dbopr.readxml("overflow", "method"), self.dbopr.readxml("overflow", "message"))
        
        if (ovflowmes == "剩余出借金额不足，请重新加入", "优先出借加入金额超出限额测试失败"):
              
            self.logopr.setInfo(u"超出可出借金额，测试通过")
            self.assertEqual(ovflowmes, "剩余出借金额不足，请重新加入", "超出可出借金额，测试通过")
              
        else:
  
            self.logopr.setError(u"超出可出借金额，测试不通过")
            self.assertEqual(ovflowmes, "剩余出借金额不足，请重新加入", "超出可出借金额，测试不通过")
        self.priority.ComfirmButton()




if __name__ == "__main__":
    unittest.main()