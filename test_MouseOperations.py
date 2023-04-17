from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test_mouseOperations():

    path="Drivers/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/")
    act = ActionChains(driver)

    # Click operation
    #act.click().perform()
    #act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    # Context Click(Right Click)
    #act.context_click().perform()
    #act.context_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    #act.double_click().perform()
    #act.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    act.move_to_element(driver.find_element(By.XPATH,"//span[contains(text(),'TUTORIAL')]")).perform()

