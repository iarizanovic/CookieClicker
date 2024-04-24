from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()

time.sleep(1)
langSelect = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
langSelect.click()

time.sleep(3)
bigCookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

prod_num = 1
while True:
    bigCookie.click()

    # Click on the upgrade (first available)
    try:
        upgrade = driver.find_element(By.XPATH, f'//*[@id="upgrade0" and @class="crate upgrade enabled"]')
    except:
        pass
    else:
        # if upgrade.get_attribute("class") == "crate upgrade enabled":
        upgrade.click()
        print(f"upgrade clicked")

    # Click on the product (Allways wait for available product with the biggest number)
    for i in range(prod_num)[::-1]:
        try:
            product = driver.find_element(By.XPATH, f'//*[@id="product{i}"]')
        except:
            pass
        else:
            if product.get_attribute("class") == "product unlocked disabled":
                prod_num = i + 2
                break
            elif product.get_attribute("class") == "product unlocked enabled":
                product.click()
                print(f"product{i} clicked")
                break
