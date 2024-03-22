import time, json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .config import username, password


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://dolar.set-icap.com/auth/login/")
wait = WebDriverWait(driver, 20)

user_input = driver.find_element(By.XPATH, '(//input[@name="username"])')
user_input.send_keys(username)

pwd_input = driver.find_element(By.XPATH, '(//input[@name="password"])')
pwd_input.send_keys(password)

login_button = driver.find_element(
    By.XPATH, '(//button[@class="btn btn-lg btn-block Button__btnPrimary__29Ht"])'
)
login_button.click()

wait.until(
    EC.presence_of_element_located(
        (By.XPATH, '//div[@class="mar-no text-semibold Home__content__ebQk"]')
    )
)

while True:
    value = driver.find_element(
        By.XPATH, '(//div[@class="mar-no text-semibold Home__content__ebQk"])'
    ).text

    data = {"time_stamp": time.ctime(time.time()), "value": value}
    print(data)

    # Open the JSON file for writing
    with open("data.json", "w") as file:
        # Write JSON data to the file
        json.dump(data, file)

    time.sleep(30)
