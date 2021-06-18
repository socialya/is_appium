import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
class TestParametrize():
    def setup_class(self):
        disire_cap = {
            "platformName": "ANDROID",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            # "appPackage": "cn.kmob.screenfingermovelock",
            # "appActivity": "com.samsung.ui.MainActivity",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "true",
            # "dontStopAppOnReset": True,
            "skipDeviceInitialization": "true",
            "unicodeKeyboard":True,
            'resetKeyboard':True
            # 不会停止app
        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",disire_cap)
        self.driver.implicitly_wait(10)
    @pytest.mark.parametrize("name,value",[("阿里巴巴","BABA"),("京东","JD")])
    def test_params(self,name,value):
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(f"{name}")
        self.driver.find_element(MobileBy.XPATH,f"//*[@text='{value}']").click()
        self.driver.find_element(MobileBy.XPATH,f"//*[@text='{value}']/../../..//*[@text='加自选']").click()
        # eles=self.driver.find_elements(MobileBy.XPATH,f"//*[@text='`{value}']/../../..//*[@text='已添加']")
        # print(eles)
        # current_price=self.driver.find_element(MobileBy.XPATH,f"//*[@text='{value}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        # current_price=float(current_price)
        # assert_that(current_price,close_to(current_price,current_price*0.1))
    def teardown(self):
        self.driver.back()
    def teardown_class(self):
        self.driver.quit()
    # def teardown_class(self):
    #     self.driver.quit()