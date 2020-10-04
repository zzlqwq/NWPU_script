from selenium import webdriver
import time


def open_browser():
    # global browser
    browser = webdriver.Chrome("C:\\Users\\11706\\Desktop\\chromedriver.exe")  # 设置Chrome为selenium的浏览器驱动
    browser.get("https://uis.nwpu.edu.cn/cas/login")
    browser.maximize_window()
    browser.implicitly_wait(10)
    username = "username"
    password = "password"

    browser.find_element_by_id("username").send_keys(username)
    browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_name("submit").click()
    time.sleep(4)
    browser.find_element_by_link_text("疫情每日填报").click()
    time.sleep(2)

    browser.get("http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp")
    browser.find_element_by_xpath("/html/body/div[3]/form/div[5]/div[24]/div/a").click()
    browser.find_element_by_xpath("/html/body/div[3]/form/div[6]/div[2]/div[25]/label/div[1]/i").click()
    browser.find_element_by_xpath("/html/body/div[3]/form/div[6]/div[3]/a[2]").click()
    time.sleep(4)


open_browser()
