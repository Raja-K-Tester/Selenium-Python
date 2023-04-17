from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import time
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    path = "Drivers/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(environment_setup):
    driver.find_element(By.XPATH,"/html/body/div[4]/section/ul/li[2]/label").click()
    driver.find_element(By.NAME,"_txtUserName").send_keys("abcd123$")
    driver.find_element(By.NAME, "_txtPassword").send_keys("abcd123")
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='tab-content2']/form/div/input[2]").click()
    driver.find_element(By.XPATH, "//*[@id='navbar-brand-centered']/ul/li[2]/a").click()
    driver.find_element(By.XPATH, "//*[@id='navbar-brand-centered']/ul/li[2]/ul/li[7]/a").click()
    time.sleep(10)
    allwindows = driver.window_handles
    mainWin=""
    for win in allwindows:
        driver.switch_to.window(win)
        if(driver.current_url=='https://www.thetestingworld.com/testings/manage_customer.php'):
            driver.find_element(By.XPATH,"//*[@id='downloadButton']").click()
            time.sleep(20)
            driver.close()
        elif(driver.current_url=='https://www.thetestingworld.com/testings/dashboard.php'):
             mainWin=win


    driver.switch_to.window(mainWin)
    print(driver.current_url)

