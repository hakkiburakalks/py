from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date   



class Test_demoClass:
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok = True)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    
    def test_noUserNameAndNoPassword(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-noUserNameAndNoPassword.png")    
        assert errorMessage.text == "Epic sadface: Username is required"

    @pytest.mark.parametrize("username,password",[("standard_user",""),("locked_out_user","")] ) 
    def test_noPassword(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-noPassword.png")    
        assert errorMessage.text == "Epic sadface: Password is required"

    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_lockedOutUser(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-lockedOutUser.png")    
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

   
    def test_standartUser(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        usernameInput.send_keys("standart_user")
        passwordInput.send_keys("secret_sauce")
        sleep(5)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        productList = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.execute_script("window.scrollTo(0,500)")
        self.driver.save_screenshot(f"{self.folderPath}/number-of-products-{len(productList)}.png")
        assert True


            










  