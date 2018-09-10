# -*- coding : utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from time import sleep

drivers = webdriver.Chrome()
arealist = open("checkarea.dict","r") # 打开文件读取所需检查地区
urls =eval(arealist.read()) # 转换为字典
# urls = {'www.baidu.com' : 'baidu'}
develop_bth = "//*[@id=\"btn_dev\"]/span/span[1]" # 开发者模式按钮
receive_bth = "/html/body/div/div[1]/div/div[3]/a/span/span" # 接收按钮
sure_bth = "/html/body/div[2]/div[2]/div[4]/a/span/span" # 确认接收成功按钮

def openhtml(url):
    driver = drivers
    driver.set_page_load_timeout(5) # 超时即抛出异常
    try:
        driver.get("http://."+urls[url]+"/cztdataexchange-war/index.action")
        WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, develop_bth))).click()
        sleep(0.5)
        driver.get("http://" + urls[url] + "/cztdataexchange-war/cztdataexchange/intoMyTest.action")
        WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, receive_bth))).click()
        try:
            WebDriverWait(driver, 4, 0.5).until(EC.presence_of_element_located((By.XPATH, sure_bth))).click()
            driver.save_screenshot(url + ".png")
            # driver.get_screenshot_as_file(url+".png")
            print(url + " 检查通过")
        except NoSuchElementException :
            driver.save_screenshot("error" + url + ".png")
            print(url + "检查不通过，请手动检查服务   http://" + urls[url] + "/cztdataexchange-war/cztdataexchange/intoMyTest.action")
        finally:
            print("----------------------------")
    except TimeoutException:
        print(url+"拒绝访问地址，请检查网络")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")


for url in urls:
    openhtml(url)

arealist.close()   
drivers.quit()

