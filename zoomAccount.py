from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def createZoom(userEmail, userDepartment, userType = 'Basic'):
    driver = webdriver.Chrome()
    driver.get("https://zoom.us/signin")
    driver.find_element_by_id("email").send_keys("") #Enter your username here
    driver.find_element_by_id("password").send_keys("")#in password manager
    driver.find_element_by_id("password").send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    driver.find_element_by_link_text("Users").click()
    driver.find_element_by_id("tab_add_users").click()
    driver.find_element_by_id("add_user_emails").send_keys(userEmail)
    driver.find_element_by_id("add_user_emails").clear()
    driver.find_element_by_id("add_user_emails").send_keys(userEmail)
    if(userType == 'Basic'):
        #can't find the way to isolate radio button, use keyboard keys instead, maybe in future
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.LEFT)
        actions.perform()
    driver.find_element_by_id("add_user_dept").send_keys(userDepartment)
    driver.find_element_by_id("add_user_btn").click() #add user
    return driver #for testing

#Test
#driver = createZoom(userEmail = 'somer.random@oneildata.com', userType = 'Basic', userDepartment = 'IBD')
