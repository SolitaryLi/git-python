from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browset = webdriver.Chrome('C:\\Users\\Administrator.SC-201808172314\\AppData\Local\\Google\\Chrome\\Application\\chromedriver.exe')
try:
    browset.get('https://www.baidu.com')
    input = browset.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browset, 10)
    wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))  # ?????????????
    print(browset.current_url)
    print(browset.get_cookies())
    print(browset.page_source)
finally:
    browset.close()