from selenium import webdriver
import time
import random
import tkinter.messagebox

time_tuple = time.localtime(time.time())
try:
    f = open("data.txt", "r")
    data = f.readlines()
    id=data[0].split('\n')[0]
    pw=data[1]
    f.close()
except:
    tkinter.messagebox.showwarning("未找到txt","请将一卡通号和密码的txt文件置于同一文件夹下")

if(time_tuple[3]<1 or time_tuple[3]>14):
    tkinter.messagebox.showwarning("时间错误","当前时间不能打卡")
else:
    option = webdriver.ChromeOptions()
    #option.add_argument('headless')
    #time.sleep(10)
    driver=webdriver.Chrome("chromedriver.exe")#,chrome_options=option)
    url="http://ehall.seu.edu.cn/new/index.html"

    driver.get(url)
    time.sleep(1)
    driver.find_element_by_class_name("amp-no-login-zh").click()
    time.sleep(1)
    driver.find_element_by_class_name("auth_input").send_keys("220205287")
    driver.find_element_by_id("password").send_keys("732206wang")
    time.sleep(1)
    try:
        driver.find_element_by_id("xsfw").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/div/div/div/div/div[3]/div[2]/a[1]").click()
    except:
        tkinter.messagebox.showwarning("请检查用户名密码")
        driver.quit()
    #driver.close()
    try:
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        time.sleep(10)
        driver.find_element_by_xpath("//div[contains(text(),'新增')]").click()
        #driver.find_element_by_xpath("//div[contains(text(),'新增')]").click()
        temp=36+random.randint(0,9)/10
        tmp=str(temp)
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.find_element_by_name("DZ_JSDTCJTW").click()
        driver.find_element_by_name("DZ_JSDTCJTW").send_keys(tmp)
        driver.find_element_by_xpath("//*[@id='save']").click()
        time.sleep(1)
        driver.find_element_by_link_text("确认").click()
    except:
        tkinter.messagebox.showwarning("检查填报信息")
        driver.quit()
    driver.quit()

