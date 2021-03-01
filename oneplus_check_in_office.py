#imports
from selenium import webdriver

#setup logins
ID = "winston.huang@oneplus.com"
PassWord = "P@ssw0rd"

#setup path to chromedriver.exe
driver = webdriver.Chrome('/Users/pooh7/Downloads/chromedriver')

#setup waiting time
driver.implicitly_wait(10)

#setup webpage
webpage = 'https://auth.mayohr.com/HRM/Account/Login'

#open webpage
driver.get(webpage)

#enter username
driver.find_element_by_name('userName').send_keys(ID)

#enter password
driver.find_element_by_name('password').send_keys(PassWord)

#click enter
driver.find_element_by_xpath('//span[contains(text(),"登入")]').click()

#click checkin
driver.find_element_by_link_text('我要打卡').click()

#click onduty
driver.find_element_by_xpath('//span[contains(text(),"上班")]').click()

#check feedback
elements = driver.find_elements_by_tag_name('h4')
for element in elements:
    print(element.text)