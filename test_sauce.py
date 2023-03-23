from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class testClass:

    def noUserNameAndNoPassword(self):
          driver = webdriver.Chrome(ChromeDriverManager().install())
          driver.get("https://www.saucedemo.com/")
          driver.maximize_window()
          sleep(2)
          inputUsername = driver.find_element(By.ID,"user-name")
          inputUsername.send_keys("")
          sleep(2)
          inputPassword = driver.find_element(By.ID,"password")
          inputPassword.send_keys("")
          sleep(2)
          button = driver.find_element(By.NAME, "login-button")
          button.click()
          
         
          
          
    def noPassword(self):
           driver = webdriver.Chrome(ChromeDriverManager().install())
           driver.get("https://www.saucedemo.com/")
           driver.maximize_window()
           sleep(2)
       
           inputUsername = driver.find_element(By.ID,"user-name")
           inputUsername.send_keys("standard_user")
           sleep(2)
           inputPassword = driver.find_element(By.ID,"password")
           inputPassword.send_keys("")
           sleep(2)
           button = driver.find_element(By.NAME, "login-button")
           button.click()

           
    def lockedOutUser(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(2)
        inputUsername = driver.find_element(By.ID,"user-name")
        inputUsername.send_keys("locked_out_user")
        sleep(2)
        inputPassword = driver.find_element(By.ID,"password")
        inputPassword.send_keys("secret_sauce")
        sleep(2)
        button = driver.find_element(By.NAME, "login-button")
        button.click()

        
    def xIcon(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(2)
        inputUsername = driver.find_element(By.ID,"user-name")
        inputUsername.send_keys("")
        sleep(2)
        inputPassword = driver.find_element(By.ID,"password")
        inputPassword.send_keys("")
        sleep(2)
        button = driver.find_element(By.NAME, "login-button")
        button.click()
        sleep(2)
        iconButton = driver.find_element(By.CLASS_NAME,"error-button")  
        iconButton.click()
        sleep(5)

        

    def standartUser(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(2)
        inputUsername = driver.find_element(By.ID,"user-name")
        inputUsername.send_keys("standard_user")
        sleep(2)
        inputPassword = driver.find_element(By.ID,"password")
        inputPassword.send_keys("secret_sauce")
        sleep(2)
        button = driver.find_element(By.NAME, "login-button")
        button.click()
        sleep(2)
        productList = driver.find_elements(By.CLASS_NAME,"inventory_item")
        numberOfProduct = f"Girilen ekranda tam olarak {len(productList)} kadar ürün gözükmektedir"
        print(numberOfProduct)  

        





test = testClass()
test.noUserNameAndNoPassword()
test.noPassword()
test.lockedOutUser()
test.xIcon()
test.standartUser()
while True:
    continue