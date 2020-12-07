# -*- coding: UTF-8 -*-
'''
Created on 2019-08-05

@author: LiPing
'''

import HTMLTestRunner
import unittest, os
from src.Reports.mail import MailUtils
from src.TestCases.BuyPriorityTest import BuypriorityTest
from src.TestCases.BuyProductTest import BuyProductTest
from src.TestCases.RechargeTest import RechargeTest
from src.TestCases.WithdrawTest import WithdrawTest
from src.TestCases.AccountSetupTest import AccountSetupTest
from src.TestCases.ContactUsTest import ContactUsTest
from src.TestCases.ChangeLoginpwdTest import ChangeLoginpwdTest
from src.TestCases.HelpCenterTest import HelpCenterTest


#创建测试集合   
def create_suite():
    print("测试开始")
    suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(BuypriorityTest))      #测试加入优先出借
#     suite.addTest(unittest.makeSuite(RechargeTest))         #测试充值功能
#     suite.addTest(unittest.makeSuite(WithdrawTest))         #测试提现功能
#     suite.addTest(unittest.makeSuite(BuyProductTest))       #测试购买散标
#     suite.addTest(unittest.makeSuite(AccountSetupTest))     #测试账户设置    
    suite.addTest(unittest.makeSuite(ContactUsTest))        #测试联系我们侧边栏
#     suite.addTest(unittest.makeSuite(ChangeLoginpwdTest))   #测试修改登录密码功能
#     suite.addTest(unittest.makeSuite(HelpCenterTest))       #测试帮助中心
    return suite 

if __name__ == '__main__':
    suite = create_suite()
    
    #本地执行
#     fp = open("./result.html","wb")   

    #Jenkins    
    fp = open(os.getcwd()+"/result.html","wb")
    
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"旺财web自动化测试报告",description=u"测试用例执行情况",verbosity=2)
    runner.run(suite)
    fp.close()
    MailUtils.send_test_report()


   
