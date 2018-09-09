# -*- coding : utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

drivers = webdriver.Chrome()
arealist = open("checkarea.json","r") # 打开文件读取所需检查地区
urls =eval(arealist.read()) # 转换为字典格式
# urls = {'www.baidu.com' : 'baidu'}
develop_bth = "//*[@id=\"u1\"]/a[6]" # 开发者模式按钮
receive_bth = "//*[@id=\"s_btn_wr\"]" # 接收按钮
sure_bth = "//*[@id=\"2\"]/h3/a" # 确认接收成功按钮

def openhtml(url):
    driver = drivers
    driver.get("https://www."+urls[url]+".com")
    #driver.maximize_window()
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, develop_bth ))).click()
    sleep(2)
    driver.get("https://news."+urls[url]+".com")
    sleep(2)
    search = driver.find_element_by_xpath("//*[@id=\"ww\"]") #delete
    search.send_keys("范冰冰") #delte
    driver.find_element_by_xpath(receive_bth).click()
    try:
        element = WebDriverWait(driver, 15, 0.5).until(
            EC.presence_of_element_located((By.XPATH, sure_bth ))
        )
        element.click()
        driver.save_screenshot("/home/deepin/"+url+".png")
        #driver.get_screenshot_as_file("/home/deepin/"+url+".png")
        print(url+" 检查通过")
    except:
        driver.save_screenshot("/home/deepin/error"+url+".png")
        print(url+"检查不通过，请手动检查服务")
        print("https://news."+urls[url]+".com")
    finally:
        print("----------------------------")

for url in urls:
    openhtml(url)
    drivers.quit()
    arealist.close()
