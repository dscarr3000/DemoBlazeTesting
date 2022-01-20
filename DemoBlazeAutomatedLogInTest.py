from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.demoblaze.com/index.html')
wait = WebDriverWait(driver, 10)
log_in_button = driver.find_element(By.ID, 'login2')
log_in_button.click()
username_field = driver.find_element(By.ID, 'loginusername')
password_field = driver.find_element(By.ID, 'loginpassword')
wait.until(EC.element_to_be_clickable((By.ID, 'loginusername')))
username_field.click()
username_field.send_keys('testUser')
password_field.click()
password_field.send_keys('testPassword')
log_in_submit = driver.find_element(By.CSS_SELECTOR, '#logInModal > div > div > div.modal-footer > button.btn.btn-primary')
log_in_submit.click()
wait.until(EC.visibility_of_element_located((By.ID, 'nameofuser')))
driver.quit()