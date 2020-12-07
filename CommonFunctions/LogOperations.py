#-*- coding: UTF-8 -*-
'''
Created on 2018-11-26

@author: growingio
'''
import logging,time,sys


global LoggerOpr
class LogOperations(object):
    '''
    日志操作类
    '''


    def __init__(self):
        '''
        设置日志格式
        '''
        self.LoggerOpr=logging.getLogger()
        self.LoggerOpr.setLevel(level=logging.INFO)
        
        #本地执行
#         handler=logging.FileHandler("../Logs/WcTestLog"+time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) +".log")

        #Jenkins
        handler=logging.FileHandler(sys.path[1]+"\src\Logs\WcTestLog"+time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) +".log")

        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s  %(filename)s#%(funcName)s   %(levelname)s    %(message)s')
        handler.setFormatter(formatter)
        self.LoggerOpr.addHandler(handler)
        
    def setInfo(self,msg):
        '''
        记录info级别日志
        '''
        self.LoggerOpr.info(msg)

    def setError(self,msg):
        '''
        记录error级别日志
        '''
        self.LoggerOpr.error(msg,exc_info=True)
        
    def setWarning(self,msg):
        '''
        记录warning级别日志
        '''
        self.LoggerOpr.warning(msg)