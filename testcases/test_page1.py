import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageobject.login_page import LoginPage
from config.config import url, driver_path
from data.data import ReadWrite
from log.log import logger
from time import sleep

class LoginCases():
    def test_1(self,login):
        '''
        验证有效的用户民和密码
        '''
        self.driver = login
        self.loginpage = LoginPage(self.driver)
        user_list = ReadWrite.excelread('login')
        username = user_list[0][0]
        password = user_list[0][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        sleep(2)
        self.loginpage.click_login()
        sleep(2)
        #断言，判断错误
        assert'禅道' in self.driver.title
        self.loginpage.click_logout()
        logger.info('有效输入用户名和密码')

    @pytest.skip('不执行测试用例')
    def test_2(self):
        pass