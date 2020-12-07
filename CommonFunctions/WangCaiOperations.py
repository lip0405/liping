#-*- coding: UTF-8 -*-
'''
Created on 2019-08-05

@author: LiPing
'''

import time
from src.CommonFunctions.BaseComFunctions import BaseComFunctions


global bcfunc

class WangCaiOperations(object):
    '''
           旺财业务操作
    '''

    def __init__(self):
        '''
        初始化句柄
        '''
        self.bcfunc=BaseComFunctions()
         
    def OpenWangCai(self):
        '''
        打开旺财
        '''
        self.bcfunc.OpenBrowser("http://testwangcai2.91wangcai.com")
        self.bcfunc.AddCookie("wallet_token","edb88225-4d25-3770-91bf-201c564c8820")
                   
    def SwitchWangCaiHandle(self):
        '''
        切换到当前句柄
        '''
        self.bcfunc.SwitchHandle()
        
    def GetWangcaiText(self,locmethods,location):
        '''
        获取旺财页面内容
        '''
        felem = self.bcfunc.GetElemText(locmethods, location)
        return felem
           
    def GetBtnStatus(self,locmethods, location):
        '''
        获取按钮的状态
        '''
        btn=self.bcfunc.FindElement(locmethods, location)
        return btn.is_enabled()
    
    def FindWangcaiElement(self,locmethods, location):
        '''
        查找旺财页面元素
        '''
        felem=self.bcfunc.FindElement(locmethods, location)
        return felem
    
    def WangcaiElemClick(self,locmethods, location):
        '''
        点击旺财页面元素
        '''
        felem=self.bcfunc.ElemClick(locmethods, location)
        return felem
    
    def WangcaiSendKeys(self,locmethods, location, skey):
        '''
        向输入框中输入内容
        '''
        felem=self.bcfunc.SendKeysToText(locmethods, location, skey)
        return felem
    
    def ScrollWangCaiPage(self,num):
        '''
        将页面下滑
        '''
        self.bcfunc.ScrollPage(num)

    def QuitWangCai(self):
        '''
           退出旺财浏览器
        '''
        time.sleep(1)
        self.bcfunc.QuitBrowser()
        
        
    def WangcaiActionChains(self, menu):
        '''
        将鼠标移动到某元素位置
        '''
        self.bcfunc.ActionChains(menu)
        
    def WangcaiBrowserTitle(self):
        '''
        获取当前页面的标题
        '''
        title = self.bcfunc.GetBrowserTitle()
        return title
        
    def WangcaiCurrentUrl(self):
        '''
        获取当前页面的url
        '''
        url = self.bcfunc.GetCurrentUrl()
        return url
    
    def WcCurrentHandle(self):
        '''
        获取当前窗口的句柄
        '''
        current = self.bcfunc.CurrentHandle()
        return current
    
    def WcAllHandles(self):
        '''
        获取所有窗口的句柄
        '''
        allhandels = self.bcfunc.AllHandles()
        return allhandels
    
    def WcSwitchHandles(self, i):
        '''
        切换到指定窗口, i是窗口的索引
        '''
        windows = self.bcfunc.SwitchHandles(i)
        return windows
    
    def SwitchtoWcFrame(self, iframe):
        '''
        切换到iframe弹窗
        '''
        self.bcfunc.SwitchtoFrame(iframe)
        
    def SwitchtoWcDefault(self):
        '''
        切换回主文档
        '''
        self.bcfunc.SwitchtoDefault()
        
        

    def ToMyAccount(self):
        '''
        通过优先出借，进入充值页面
        '''
        self.bcfunc.ElemClick("Xpath", "//a[contains(text(),'项目列表')]")             
        self.bcfunc.ScrollPage(410)
        self.bcfunc.ElemClick("Xpath","//h3[contains(.,'优先出借50天-2020011501')]")
        time.sleep(1)
        self.bcfunc.SendKeysToText("Xpath", "//input[@id='moneyID']", 1000)
        time.sleep(1)
        self.bcfunc.ElemClick("Xpath", "//input[@name='submitBtn']")
        time.sleep(1)
        self.bcfunc.ScrollPage(130)
        time.sleep(1)
        self.bcfunc.ElemClick("Css", ".link")
        time.sleep(1)
        self.bcfunc.SwitchHandle()
        
    def BalanceAdd(self):
        '''
        获取页面上充值后余额
        '''
        balance = self.bcfunc.GetElemText("Xpath", "//span[@id='balance']")
        balance = float(balance)
        balanceadd = self.bcfunc.GetElemText("Css", ".gold_add")
        balanceadd = float(balanceadd)
        recprice = str(balanceadd-balance)

        return recprice, balanceadd
    
    def BalanceNew(self):
        '''
        获取最新账户余额
        '''
        balancenew = self.bcfunc.GetElemText("Xpath", "//span[@id='balance']")
        balancenew = float(balancenew)
        return balancenew
                  
    def ClickProductList(self):
        '''
        点击项目列表
        '''
        self.bcfunc.ElemClick("Xpath", "//a[contains(text(),'项目列表')]")
        time.sleep(1)
                        
    def ClickNext(self):
        '''
        点击加入优先出借的下一步
        '''
        time.sleep(2)
        self.bcfunc.ScrollPage(500)
        time.sleep(1)
        self.bcfunc.ElemClick("Xpath", "//span[@id='nextBtnPriority']")
        time.sleep(2)
        
    def ComfirmButton(self):    
        '''
        点击确定按钮
        '''
        self.bcfunc.ElemClick("Xpath", "//a[contains(text(),'确定')]")
        time.sleep(1)               
        
    def ClickRecharge(self):
        '''
        点击充值按钮
        '''
        self.bcfunc.ElemClick("Xpath", "//input[@id='recharge']")
        time.sleep(2)

    def GatewayRecevice(self):
        '''
        充值存管验密页面，点击我知道了
        '''
        time.sleep(1)
        self.bcfunc.ElemClick("Xpath", "//a[contains(text(),'我知道了')]")
        
    def GatewayRecharge(self,skey):
        '''
        充值存管验密页面，输入验证码
        '''
        self.bcfunc.SendKeysToText("Xpath", "//input[@id='smsCode']", skey)
        
    def RechargePassward(self,skey):
        '''
        输入交易密码，勾选协议，点击支付
        '''
        self.bcfunc.SendKeysToText("Xpath", "//input[@id='password']", skey)
        time.sleep(1)
        self.bcfunc.ElemClick("Xpath", "//input[@id='isAgreeReg']")
        time.sleep(1)
        self.bcfunc.ElemClick("Xpath", "//input[@id='nextButton']")
        time.sleep(10)
        
    def EcurrencyPayment(self):
        '''
        切换支付方式，选择网银充值
        '''
        time.sleep(1)
        self.bcfunc.ElemClick("Xpath", "//div[@data-way='WEB']")
        time.sleep(1)
       
    def SimulatedPayment(self):
        '''
        模拟支付成功
        '''
        time.sleep(1)
        self.bcfunc.ElemClick("Xpath", "//a[contains(text(),'模拟支付成功')]")
        time.sleep(10)
        
    def ClickProduct(self):
        '''
        点击直投项目
        '''
        self.bcfunc.ElemClick("Xpath", "//a[contains(text(),'直投项目')]")
        
    def SelectProduct(self,skey):
        '''
        选择要购买的散标，输入购买金额
        '''
        self.bcfunc.ElemClick("Xpath", "//h3[contains(.,'320190900262')]")
        self.bcfunc.SendKeysToText("Xpath", "//input[@id='moneyID']", skey)
        self.bcfunc.ElemClick("Xpath", "//input[@name='submitBtn']")
        time.sleep(2)
        
    def WalletBuyProduct(self,skey):
        '''
        确认购买散标
        '''
        self.bcfunc.ScrollPage(300)
        self.bcfunc.ElemClick("Xpath", "//span[@id='paySubmitBtn']")
        self.bcfunc.SwitchHandle()
        self.bcfunc.SendKeysToText("Xpath", "//input[@id='password']", skey)
        self.bcfunc.ElemClick("Xpath", "//input[@id='nextButton']")
        time.sleep(2)

        

    
    
    

    