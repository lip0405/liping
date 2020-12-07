#-*- coding: UTF-8 -*-
'''
Created on 2019-8-20
@author: liping
'''


import os,sys
from xml.dom import minidom
global DOC,CONN

class DataOperations(object):   
    '''
    数据读取相关操作
    '''
    def __init__(self,filename):

        '''
        初始化xml文档
        '''

        global DOC,CONN
        #本地执行
#         DOC = minidom.parse("../TestData/"+filename) 
        
        #Jenkins  
        DOC = minidom.parse(sys.path[1]+"\src\TestData\\"+filename)

    def readxml(self,tagnamefirst,tagNamesecond):
        '''
        从指定的文件中中读取指定节点的值
        @param tagnamefirst:起始节点的名称，如：project
        @param tagNamesecond: 起始节点下的二级节点
        @return: 返回二级节点的值
        '''          

        root = DOC.documentElement
        message=root.getElementsByTagName(tagnamefirst)[0]
        return message.getElementsByTagName(tagNamesecond)[0].childNodes[0].nodeValue
    
    
    
if __name__ == "__main__":
        print(sys.path[1])
        do=DataOperations("RechargeTest.xml")
