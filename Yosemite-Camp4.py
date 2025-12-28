import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


def human_sleep(a=0.2, b=0.5):
    time.sleep(random.uniform(a, b))


def run(driver):
    try:
        driver.get("https://www.recreation.gov/camping/campgrounds/10004152")
        wait = WebDriverWait(driver, 10)
        lang_button = wait.until(EC.presence_of_element_located((By.ID, "ga-global-nav-log-in-link")))
        lang_button.click()

        email = driver.find_element(By.ID, "email")
        email.send_keys("pranshu.jain22@gmail.com")

        password = driver.find_element(By.ID, "rec-acct-sign-in-password")
        password.send_keys("Jarvis@1997")
        human_sleep()

        login_button = driver.find_element(By.XPATH, "//button[.//span[text()='Log In']]")
        login_button.click()

        human_sleep(1.0, 2.0)

        driver.get("https://www.recreation.gov/camping/campgrounds/10004152")
        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.presence_of_element_located((By.ID, "availability-table")))

        # next_btn = driver.find_element(By.XPATH, '//button[@aria-label="Go Forward 5 Days"]')
        # next_btn.click()
        # human_sleep()
        # next_btn.click()

        camp_site = driver.find_element(By.XPATH,
                                        '//button[contains(@aria-label, "Sep 13, 2025 - Site Camp 4 is available")]')
        driver.execute_script("arguments[0].click();", camp_site)

        human_sleep()

        add_to_cart = driver.find_element(By.XPATH, '//button[.//span[text()="Add to Cart"]]')
        driver.execute_script("arguments[0].click();", add_to_cart)

        group_size = driver.find_element(By.XPATH, '//input[contains(@id, "per-person-number-field-10046502")]')
        driver.execute_script("arguments[0].value = '';", group_size)
        group_size.send_keys("5")

        book_button = driver.find_element(By.XPATH, "//button[.//span[text()='Book']]")
        book_button.click()

        # wait = WebDriverWait(driver, 10)
        # postal_code = wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "postal_code")]')))
        # driver.execute_script("arguments[0].value = '';", postal_code)
        # postal_code.send_keys("75039")

        human_sleep()

        wait = WebDriverWait(driver, 10)
        info_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "camp-camper-information-form")))

        url = driver.current_url
        booking_id = url.split("id=")[-1]

        first_name_map = {
            1: "Shyamal",
            2: "Vishal",
            3: "Minni",
            4: "Kashish",
            5: "Fnu"
        }

        last_name_map = {
            1: "Jadav",
            2: "Upadhyay",
            3: "Jajodia",
            4: "Yadav",
            5: "Akhil",
        }

        human_sleep()

        for index in range(1, 5):
            wait = WebDriverWait(driver, 10)
            first_name = wait.until(EC.element_to_be_clickable((By.ID, f'first_name-{booking_id}-{index}')))
            driver.execute_script("arguments[0].scrollIntoView(true);", first_name)
            first_name.send_keys(first_name_map[index])

            last_name = driver.find_element(By.ID, f'last_name-{booking_id}-{index}')
            # driver.execute_script("arguments[0].value = '" + last_name_map[index] + "';", last_name)
            last_name.send_keys(last_name_map[index])

            postal_code = driver.find_element(By.ID, f'postal_code-{booking_id}-{index}')
            # driver.execute_script("arguments[0].value = '75039';", postal_code)
            postal_code.send_keys("75039")

            human_sleep()

        tent_checkbox = driver.find_element(By.XPATH, '//input[contains(@id, "equip_tent_checkbox-")]')
        if not tent_checkbox.is_selected():
            tent_checkbox.click()

        human_sleep()

        num_vehicles = driver.find_element(By.XPATH, '//input[contains(@id, "num_vehicles-")]')
        driver.execute_script("arguments[0].value = '';", num_vehicles)
        num_vehicles.send_keys("1")

        human_sleep()

        vehicle_make = driver.find_element(By.XPATH, '//input[contains(@id, "make-")]')
        vehicle_make.send_keys("Nissan")

        vehicle_model = driver.find_element(By.XPATH, '//input[contains(@id, "model-")]')
        vehicle_model.send_keys("Rogue")

        vehicle_color = driver.find_element(By.XPATH, '//input[contains(@id, "color-")]')
        vehicle_color.send_keys("Silver")

        vehicle_license = driver.find_element(By.XPATH, '//input[contains(@id, "license_plate_number-")]')
        vehicle_license.send_keys("9RRK788")

        human_sleep()

        vehicle_state = Select(driver.find_element(By.XPATH, '//select[contains(@id, "license_plate_state-")]'))
        vehicle_state.select_by_value("CA")

        human_sleep()

        vehicle_is_awd = driver.find_element(By.XPATH, '//input[contains(@id, "is_awd_checkbox-")]')
        if not vehicle_is_awd.is_selected():
            vehicle_is_awd.click()

        human_sleep()

        # vehicle_high_clearance = driver.find_element(By.XPATH, '//input[contains(@id, "is_high_clearance_checkbox-")]')
        # if not vehicle_high_clearance.is_selected():
        #     vehicle_high_clearance.click()

        # human_sleep()

        tnc = driver.find_element(By.XPATH, '//input[contains(@id, "need-to-know-checkbox")]')
        if not tnc.is_selected():
            tnc.click()

        human_sleep()

        proceed = driver.find_element(By.ID, "test-hook-submit")
        proceed.click()

        wait = WebDriverWait(driver, 10)
        first_name = wait.until(EC.element_to_be_clickable((By.ID, f'first_name-{booking_id}-5')))
        driver.execute_script("arguments[0].scrollIntoView(true);", first_name)
        driver.execute_script("arguments[0].value = '" + first_name_map[5] + "';", first_name)
        first_name.send_keys(Keys.DELETE)
        first_name.send_keys(Keys.BACKSPACE)

        last_name = driver.find_element(By.ID, f'last_name-{booking_id}-5')
        driver.execute_script("arguments[0].value = '" + last_name_map[5] + "';", last_name)
        last_name.send_keys(Keys.DELETE)
        last_name.send_keys(Keys.BACKSPACE)

        postal_code = driver.find_element(By.ID, f'postal_code-{booking_id}-5')
        driver.execute_script("arguments[0].value = '75039';", postal_code)
        postal_code.send_keys(Keys.DELETE)
        postal_code.send_keys(Keys.BACKSPACE)

        proceed = driver.find_element(By.ID, "test-hook-submit")
        driver.execute_script("arguments[0].click();", proceed)

        wait = WebDriverWait(driver, 10)
        proceed_to_payment = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[.//span[text()='Proceed to Payment']]")))
        proceed_to_payment.click()

    except Exception as ex:
        print(ex)


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--start-fullscreen")
chrome_driver = webdriver.Chrome(options=chrome_options)
run(chrome_driver)
print("Execution completed")
if input("Do you want to quit the window? (Y/n): ").upper() == 'Y':
    chrome_driver.quit()
