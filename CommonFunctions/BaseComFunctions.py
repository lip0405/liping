#-*- coding: UTF-8 -*-
'''
Created on 2019-08-05

@author: LiPing
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

global driver

class BaseComFunctions(object):
    '''
    Web自动化测试基础类
    '''


    def __init__(self):
        '''
        构造函数
        '''

        
    def OpenBrowser(self,base_url):
        '''
        打开浏览器
        '''
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.get(base_url)
        
             
    def QuitBrowser(self):
        '''
        退出浏览器
        '''
        self.driver.quit()
        
    def FindElement(self,locmethods,location):
        '''
        查找一个元素
        @param locmethods:定位方法 
        @param location:定位数据 
        @return: 查找到的元素
        '''
        if locmethods=="ID":
            felem=self.driver.find_element_by_id(location)
        if locmethods=="Xpath":
            felem=self.driver.find_element_by_xpath(location)
        if locmethods=="Css":
            felem=self.driver.find_element_by_css_selector(location)
        return felem
            
    def ElemClick(self,locmethods,location):
        '''
        单击元素
        @param locmethods:定位方法 
        @param location:定位数据 
        '''
        felem=self.FindElement(locmethods, location) 
        felem.click()
        
    
    def SendKeysToText(self,locmethods,location,skey):
        '''
        向输入框中输入指定的内容
        @param locmethods:定位方法 
        @param location:定位数据 
        @param  skey:要输出 的内容 
        '''
        felem=self.FindElement(locmethods, location)
        #清除输入框的内容
        felem.clear()
        #输入关键字
        felem.send_keys(skey)
        
    def GetElemText(self,locmethods,location):
        '''
        获取元素显示内容
        @param locmethods:定位方法 
        @param location:定位数据 
        @return: 元素内容
        '''
        felem=self.FindElement(locmethods, location)
        return felem.text
    
    def AddCookie(self,name,token):
        '''
        添加cookie信息
        '''
        self.driver.add_cookie({"name":name,"value":token})
        
    def ScrollPage(self,num):
        '''
        滚动屏幕
        '''
        self.driver.execute_script('document.documentElement.scrollTop={0}'.format(num))
        
    def SwitchHandle(self):
        '''
        切换到当前窗口
        '''
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        
    def ActionChains(self, menu):
        '''
        鼠标移动到元素
        '''
        ActionChains(self.driver).move_to_element(menu).perform()
        
    def GetBrowserTitle(self):
        '''
        获取页面title
        '''
        title = self.driver.title
        return title
    
    def GetCurrentUrl(self):
        '''
        获取当前页面的url
        '''
        url = self.driver.current_url
        return url
        
    def CurrentHandle(self):
        '''
        获取当前窗口的句柄
        '''
        current = self.driver.current_window_handle
        return current
    
    def AllHandles(self):
        '''
        获取所有窗口的句柄
        '''
        allhandles = self.driver.window_handles
        return allhandles
    
    def SwitchHandles(self, i):
        '''
        切换到指定窗口
        '''
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[i])
        
    def SwitchtoFrame(self, iframe):
        '''
        切换到弹窗
        '''
        self.driver.switch_to.frame(iframe)
        
    def SwitchtoDefault(self):
        '''
        切换回主文档
        '''        
        driver.switch_to.default_content()
        
        
        