# -*- coding : utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from time import sleep

drivers = webdriver.Chrome()
jiraurl = "http://47.97.63.111:28082/"

#文件操作
arealist = open("/home/zktx/gongwen/checkarea.dict","r")
refuselist = open("/home/zktx/gongwen/refusearea.dict","r")
emptylist = open("/home/zktx/gongwen/emptyarea.dict","r")
logs = open("/home/zktx/gongwen/gongwen.log","w+",encoding="utf-8")
urls = eval(arealist.read()) # 转换为字典
refuse_urls = eval(refuselist.read())
empty_urls = eval(emptylist.read())

# 小助手按钮
develop_bth = "//*[@id=\"btn_dev\"]/span/span[1]" # 开发者模式按钮
receive_bth = "/html/body/div/div[1]/div/div[3]/a/span/span" # 接收按钮
sure_bth = "/html/body/div[2]/div[2]/div[4]/a/span/span" # 确认接收成功按钮
erro_bth = "/html/body/div[5]/div[2]/div[4]/a/span/span" # 出错确认按钮

# jira按钮
username = 'zhangqk'
password = 'passzqk'
username_bth = "//*[@id=\"login-form-username\"]"
password_bth = "//*[@id=\"login-form-password\"]"
login = "//*[@id=\"login\"]"
create = "//*[@id=\"create_link\"]"
item = "//*[@id=\"project-field\"]"
title = "//*[@id=\"summary\"]"
customer = "//*[@id=\"customfield_10007\"]"
contact = "//*[@id=\"customfield_10008\"]"
date = "//*[@id=\"duedate\"]"
date1 = "//*[@id=\"duedate-trigger\"]/span"
description = "//*[@id=\"description\"]"
doing = "//*[@id=\"assign-to-me-trigger\"]"
labels = "//*[@id=\"labels-textarea\"]"
submit = "//*[@id=\"create-issue-submit\"]"

drivers.set_page_load_timeout(10) # 超时即抛出异常

def check(url):
    driver = drivers
    try:
        driver.get("http://"+urls[url]+"/cztdataexchange-war/index.action")
        WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, develop_bth))).click()
        sleep(0.5)
        driver.get("http://" + urls[url] + "/cztdataexchange-war/cztdataexchange/intoMyTest.action")
        WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, receive_bth))).click()
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, sure_bth))).click()
            print(url + " 检查通过",file=logs)
        except NoSuchElementException :
            print(url+"diiop 服务未启动",file=logs)
        except:
            print(url + "检查不通过，请手动检查服务   http://" + urls[url] + "/cztdataexchange-war/cztdataexchange/intoMyTest.action",file=logs)
        finally:
            print("----------------------------",file=logs)
    except TimeoutException:
        print(url+"拒绝访问地址，请检查网络    http://"+urls[url]+"/cztdataexchange-war/index.action",file=logs)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX",file=logs)

def jira(jiraurl):
    jiradriver = drivers
    try:
        jiradriver.get(jiraurl)
        jiradriver.find_element_by_xpath(username_bth).send_keys(username)
        sleep(0.1)
        jiradriver.find_element_by_xpath(password_bth).send_keys(password)
        jiradriver.find_element_by_xpath(login).click()
        WebDriverWait(jiradriver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, create))).click()
        WebDriverWait(jiradriver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, title))).send_keys('小助手自动检查')
        jiradriver.find_element_by_xpath(customer).send_keys("全省地区")
        jiradriver.find_element_by_xpath(date1).click()
        jiradriver.find_element_by_xpath(date).send_keys(Keys.ENTER)
        jiradriver.find_element_by_xpath(description).send_keys(log)
        jiradriver.find_element_by_xpath(doing).click()
        jiradriver.find_element_by_xpath(labels).send_keys("例行检查")
        jiradriver.find_element_by_xpath(submit).click()
    except TimeoutException:
        print("网络连接超时")



for url in urls:
    check(url)
print("============================",file=logs)
print("=   以下为客户机器限制问题  =",file=logs)
print("============================",file=logs)
for url1 in refuse_urls:
    print(url1+"拒绝访问地址，请检查网络    http://"+refuse_urls[url1]+"/cztdataexchange-war/index.action",file=logs)
for url2 in empty_urls:
    print(url2+"无法进行维护",file=logs)

logs.close()
arealist.close()
arealist.close()
arealist.close()
log = open("/home/zktx/gongwen/gongwen.log","r").read()
print(log)
jira(jiraurl)

drivers.quit()
