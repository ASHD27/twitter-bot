from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear() #to get clear input-text box in webpage
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)
        for i in range(1,8):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)') #javascript this line
            time.sleep(5)
            tweets = bot.find_elements(By.XPATH, '//*[@data-testid="tweet"]//a[@dir="auto"]')       
            links = [elem.get_attribute('href') for elem in tweets]
            print(links)
            for link in links:
                bot .get(link)
                try:
                    #bot.find_elements(By.XPATH,'//div[@data-testid="like"]').click() 
                    #bot.find_element_by_xpath('//div[@data-testid="like"]').click()
                    
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(30)


ed = TwitterBot('tosh564@gmail.com', 'Tosh564@')
ed.login()
ed.like_tweet('opensource')
