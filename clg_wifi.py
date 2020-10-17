from selenium import webdriver
driver = webdriver.Firefox(executable_path='/home/khole/Downloads/gk/geckodriver')
driver.get('http://172.16.1.1:8090/httpclient.html')
name = "z"
passwd = "vv"
usrbox = driver.find_element_by_name('username')
passbox = driver.find_element_by_name('password')
usrbox.send_keys(name)
passbox.send_keys(passwd)
button = driver.find_element_by_id('logincaption')
button.click()

