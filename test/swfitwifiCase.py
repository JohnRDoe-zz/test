import sys
import os
import HTMLTestRunner
import unittest
from appium import webdriver
from time import sleep
# from a
from selenium.common.exceptions import NoSuchElementException,WebDriverException
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p)
)

# return windowSize

class SwfitWifiCase(unittest.TestCase):
    def setUp(self):
        self.

    def startApp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'GT-I9300'
        desired_caps['browserName'] = ''
        desired_caps['version'] = '4.3'
        desired_caps['app'] = 'D:\\adb\\tool.apk'
        desired_caps['appPackage'] = 'mobi.wifi.toolbox'
        desired_caps['appActivity'] = 'mobi.wifi.abc.ui.activity.SplashActivity'
        desired_caps['unicodeKeyboard']='True'
        desired_caps['resetKeyboard']='True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

        global window_size,width,height
        # self.driver = self.self.driver
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")


    def test_sliding(self):

        #引导页滑动
        sleep(7)
        self.driver.swipe(width*8/9, height/2, width/8, height/2,1300)
        sleep(2)
        self.driver.swipe(width*8/9, height/2, width/8, height/2,1300)
        sleep(2)
        self.driver.swipe(width*8/9, height/2, width/8, height/2,1300)


    def test_accept_continue(self):
        sleep(3)
        el = self.driver.find_element_by_id("mobi.wifi.toolbox:id/button1")
        el.click()#接受&继续
        sleep(2)#上划
        self.driver.swipe(width/2, height*3/4,width/2, height/4)


    def test_conaction(self):

        sleep(3)
        ell= self.driver.find_element_by_name( '315WiFi')
        ell.click()
        # if not ell:
        # self.driver.swipe(width/2, height*2/3,width/2, height/3)
        # else:

        password = self.driver.find_element_by_id('mobi.wifi.toolbox:id/etConnectPassword')
        password.send_keys("01234567")#输入密码

        con = self.driver.find_element_by_id('mobi.wifi.toolbox:id/btnConnect')
        con.click()#点击链接
        # if (self.self.driver.find_element_by_class_name("android.widget.LinearLayout")):
        #     print("PASS")

    # def check(self):
    #     sleep(3)
    #     self.self.driver.find_element_by_name("检查")
    def quit(self):
        self.driver.quit()
    # def __init__(self):
    #     pass
if __name__ == '__main__':
    SW = SwfitWifiCase()
    SW.startApp()
    SW.test_sliding()
    SW.test_accept_continue()
    SW.test_conaction()
    # SW.quit()
    # 定义一个测试容器
    testunit = unittest.TestSuite()
    testunit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(SwfitWifiCase))
    testunit.addTest(SwfitWifiCase("test_sliding"))
    # SW.test_sliding()
    testunit.addTest(SwfitWifiCase("test_accept_continue"))
    # SW.test_accept_continue()
    testunit.addTest(SwfitWifiCase("test_accept_conaction"))
    # suite = unittest.makeSuite(testCaseClass = 'SwfitWifiCase')
    #定义报告目录
    filename = 'D:\\report\\report.html'
    # SW.test_conaction()
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = u'自动化测试报告',description= u'自动化测试报告')
    runner.run(testunit)






