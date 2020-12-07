#-*- coding: UTF-8 -*-
'''
Created on 2019-8-8

@author: LiPing
'''
from src.CommonFunctions.WangCaiOperations import WangCaiOperations
from src.CommonFunctions.DataOperations import DataOperations
import unittest

global product,dbopr

class BuyProductTest(unittest.TestCase):
    '''
    测试购买散标功能
    '''
    
    @classmethod
    def setUpClass(cls):
        print("开始测试购买散标")
        cls.dbopr=DataOperations("BuyProductTest.xml")
        cls.product=WangCaiOperations()
        cls.product.OpenWangCai()
#         print(cls.dbopr.readxml("product", "price"))
        
    @classmethod
    def tearDownClass(cls):
        print("购买散标测试结束")
        cls.product.QuitWangCai()
        

    def test_buy_product_sucess(self):
        u"购买100元散标"
        self.product.ClickProductList()
        self.product.ClickProduct()
        self.product.SelectProduct(self.dbopr.readxml("product", "price"))
        self.product.WalletBuyProduct(self.dbopr.readxml("product", "password"))
                

if __name__ == "__main__":
    unittest.main()