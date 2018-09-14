from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("http://47.97.63.111:28082/secure/Dashboard.jspa")

username = 'XXX'
password = 'XXX'
username_bth = "//*[@id=\"login-form-username\"]"
password_bth = "//*[@id=\"login-form-password\"]"
login = "//*[@id=\"login\"]"

driver.find_element_by_xpath(username_bth).send_keys(username)
sleep(0.5)
driver.find_element_by_xpath(password_bth).send_keys(password)
driver.find_element_by_xpath(login).click()

sleep(2)
newadd = "//*[@id=\"create_link\"]"

driver.find_element_by_xpath(newadd).click()

item = "//*[@id=\"project-field\"]"
title = "//*[@id=\"summary\"]"
date = "//*[@id=\"duedate\"]"
date1 = "//*[@id=\"duedate-trigger\"]/span"
description = "//*[@id=\"description\"]"
doing = "//*[@id=\"assign-to-me-trigger\"]"
labels = "//*[@id=\"labels-textarea\"]"
submit = "//*[@id=\"create-issue-submit\"]"

#driver.find_element_by_xpath(item).send_keys("公文小助手及OA (GWOA)",Keys.ENTER)
sleep(1)
driver.find_element_by_xpath(title).click()
driver.find_element_by_xpath(title).send_keys('小助手自动检查')
sleep(1)
#driver.find_element_by_xpath(date).send_keys("12/九月/18")
driver.find_element_by_xpath(date1).click()
driver.find_element_by_xpath(date).send_keys(Keys.ENTER)
tmp = open('gongwen.log','r')
driver.find_element_by_xpath(description).send_keys(tmp.read())
driver.find_element_by_xpath(doing).click()
driver.find_element_by_xpath(labels).click()
driver.find_element_by_xpath(labels).send_keys("例行检查")
driver.find_element_by_xpath(labels).send_keys(Keys.ENTER)
tmp.close()



