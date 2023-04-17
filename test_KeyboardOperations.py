from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test_mycase():
    path="Drivers/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.find_element(By.NAME,"fld_username").send_keys("Hello")

    act = ActionChains(driver)
    act.send_keys(Keys.CONTROL).send_keys("a").perform()
