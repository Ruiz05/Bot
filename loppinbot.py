import time
from selenium import webdriver
Username = 'ISI username opl'
Passwd = 'Isi passwd mu'
driver = webdriver.Chrome('chromedriver')
driver.get('https://umkt.ucm.ac.id/courses/internet-of-things-iot-/')
cih = driver.find_element_by_class_name('top-bar-menu-login-link')
cih.click()
userinput = driver.find_element_by_name('email')
userinput.send_keys(Username)
passinput = driver.find_element_by_xpath('//*[@id="6"]')
passinput.send_keys(Passwd)
tombol = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div[3]/div/form/button')
tombol.click()
time.sleep(5)
driver.get('https://umkt.ucm.ac.id/courses/internet-of-things-iot-/a_1/')
time.sleep(5)
while True :
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="page-traversal"]/a[2]').click()
