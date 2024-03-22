import time, json, asyncio
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(username, password, driver):
    try:
        driver.get("https://dolar.set-icap.com/auth/login/")

        user_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="username"]'))
        )
        user_input.send_keys(username)

        pwd_input = driver.find_element(By.XPATH, '(//input[@name="password"])')
        pwd_input.send_keys(password)

        login_button = driver.find_element(
            By.XPATH,
            '(//button[@class="btn btn-lg btn-block Button__btnPrimary__29Ht"])',
        )
        login_button.click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@class="mar-no text-semibold Home__content__ebQk"]')
            )
        )
        return True

    except Exception as e:
        print(e)
        return False


async def main(driver):
    try:
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
            await asyncio.sleep(30)  # Sleep for 30 seconds
    except (asyncio.exceptions.CancelledError, KeyboardInterrupt):
        driver.quit()
        print("Task was cancelled")
    except Exception as e:
        print(f"Error in main function: {e}")
