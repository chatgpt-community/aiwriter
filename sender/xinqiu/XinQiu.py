from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class XinQiu:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir=/Users/ljma/Library/Application Support/Google/Chrome/Profile 2")
        self.driver = webdriver.Chrome(options=chrome_options)

    def send(self, event):
        if not event['content']:
            print('Error: event content is null')
            return

        self.driver.get('https://wx.zsxq.com/dweb2/index/group/48884842581428')

        # wait for the page to load
        time.sleep(1)
        wait = WebDriverWait(self.driver, 1000)

        # find the text box and enter the event content
        tip_div = self.driver.find_element(By.XPATH, "//div[contains(text(), '点击发表主题...')]")
        tip_div.click()
        editor_div = self.driver.find_element(By.CSS_SELECTOR, 'div.ql-editor.ql-blank')
        p_element = editor_div.find_element(By.CSS_SELECTOR, "p")
        p_element.send_keys(event['content'])

        # click the submit button
        submit_button = self.driver.find_element(By.CLASS_NAME, 'submit-btn')
        submit_button.click()

        # print a success message
        print('Message sent successfully')

        time.sleep(1)
        # close the browser
        self.driver.quit()
