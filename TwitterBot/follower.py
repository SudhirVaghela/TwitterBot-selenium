from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBott:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(25)

    def Scrollpage(self, hashtag1):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag1 + '&src=typed_query& = live')
        time.sleep(30)
        for i in range(1, 10):
            bot.execute_script('window.scrollBy(0,500)')
            time.sleep(10)
            print('procced is done')


tb = TwitterBott('username', 'password')
tb.login()
tb.Scrollpage('machinelearning')
