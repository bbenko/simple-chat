# FILEPATH: /Users/bb/code/simple-chat/test_app.py
import unittest
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from app import app


def run_app():
    app.run(use_reloader=False)

class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start Flask app in a separate process
        cls.process = Process(target=run_app)
        cls.process.start()
        cls.driver = webdriver.Chrome() 

    def test_chat_post(self):
        self.driver.get('http://127.0.0.1:5000')

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "messageInput"))
            )
        except TimeoutException:
            self.fail("Loading took too much time!")

        # Check if the spinner gif is hidden and send button is visible
        spinner = self.driver.find_element(By.ID, "spinner")
        send_button = self.driver.find_element(By.ID, "sendButton")
        self.assertFalse(spinner.is_displayed())
        self.assertTrue(send_button.is_displayed())

        # Find the message input field
        message_input = self.driver.find_element(By.ID, "messageInput")

        # Type a test message and press enter
        test_message = 'Hello, Server!'
        message_input.send_keys(test_message)
        message_input.send_keys(Keys.RETURN)

        # a new p in #chatOuptut should appear with a class "message" and the text from test_message
        try:
            WebDriverWait(self.driver, 10).until(
               EC.presence_of_element_located((By.XPATH, f"//div[@id='chatOutput']//p[contains(@class, 'message') and contains(text(), '{test_message}')]"))
            )
        except TimeoutException:
            self.fail("There is no message!")

        # Check if the spinner gif is visible
        self.assertTrue(spinner.is_displayed())

        # Check if the send button is hidden
        self.assertFalse(send_button.is_displayed())

        # Wait for the spinner to disappear
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.ID, "spinner"))
            )
        except TimeoutException:
            self.fail("Spinner took too much time to disappear!")
        
        # a new p in #chatOuptut with a class "server-response" should appear
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//div[@id='chatOutput']//p[contains(@class, 'server-response') and contains(text(), '{test_message}')]"))
            )
        except TimeoutException:
            self.fail("Loading took too much time!")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # Close the browser
        cls.process.terminate()  # Terminate Flask app process
        cls.process.join()

if __name__ == "__main__":
    unittest.main()
