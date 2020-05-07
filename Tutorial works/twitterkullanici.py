from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        self.browserProfile= webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password
    
    def signIn(self):
      self.browser.get("https://twitter.com/login")
      time.sleep(1)
      usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
      passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")

      usernameInput.send_keys(self.username)
      passwordInput.send_keys(self.password)
      btnSubmit = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[3]/div/div")
      btnSubmit.click()
      time.sleep(1)

    def search(self, hashtag):
        searchInput= self.browser.find_elements_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        searchInput.send_keys(hashtag)
        time.sleep(1)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(1)

        try:
            list = self.browser.find_elements_by_xpath("//*[@id='react-root']/div[2]/div[2]/div/div/input")
            for item in list:
                print(item.text)
        except AttributeError:
            print("amk hatası")

twitter = Twitter(username, password)
#login
twitter.signIn()
twitter.search("python")