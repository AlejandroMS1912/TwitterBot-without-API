from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

################################################### - Select Username or Hashtag - ####################################################

inputVariable = input("Select your index (hashtag or username): ")

while inputVariable != "username" and inputVariable != "hashtag":
    inputVariable = input("Wrong command, try again\nSelect your index (hashtag or username): ")

if inputVariable == "username":
    user = input("Type the username: ")
    hashtag = ""

if inputVariable == "hashtag":
    hashtag = input("Type the hashtag: ")
    user = ""

#####################################################################################################################################

class TwitterBot:
    def __init__(self, username, password):
        '''
        This method asign the username and the password parameters inputs in the driver that will be used in the following methods
        '''
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(executable_path='C:/Users/Usuario/Desktop/Twitterbot/chromedriver.exe')

    def login(self):
        '''
        In this method firstly the driver searchs the login page of twitter, then detects the user and the password boxes and clean
        and fill them with the established parameters
        '''
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)

        email = bot.find_element("xpath", '//input[@autocomplete="username"]')
        email.clear()
        email.send_keys(self.username)
        email.send_keys(Keys.RETURN)
        time.sleep(3)

        password = bot.find_element("xpath", '//input[@name="password"]')
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def likeTweets(self, inputVariable, user, hashtag):
        '''
        This method firstly reject the cookies pop-up to avoid future click problems, then there are two options:

        - If the command was "username", it search's the user inputed profile page.
        - If the command was "hashtag", it search the inputed hashtag page.
        
        After a quick scroll in that page it detects all the tweets and store them in a list, then it start's liking each of 
        them with the cooldown parameters established to make it in the most natural way posible in order to avoid possible bans.
        This is fully explained in the github documentation.
        '''

        bot = self.bot

        RejectCookies = bot.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]/div/span/span')        
        RejectCookies.click()

        if inputVariable == "username":

            bot.get("https://twitter.com/" + user)

        if inputVariable == "hashtag":

            bot.get("https://twitter.com/search?q=" + hashtag + "&src=typed_query")

        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)

        tweets = bot.find_elements("xpath", '//a[@dir="auto" and not(@rel)]')
        tweets_url = [tweet.get_attribute('href') for tweet in tweets]
        print("Tweets to like: (", (len(tweets_url) - 3), ")",  tweets_url)

        for url in tweets_url:
        
            bot.get(url)
            try:
                time.sleep(1)
                if url == 'https://twitter.com/i/keyboard_shortcuts':
                    continue
                    
                if url== "https://twitter.com/" + user + "/following":
                    continue
                
                if url== "https://twitter.com/" + user + "/followers":
                    continue
                 
                else:
                    time.sleep(2)
                    likeButton = bot.find_element("xpath", '//div[@data-testid="like"]')   
                    webdriver.ActionChains(bot).move_to_element(likeButton).click(likeButton).perform()
                    time.sleep(random.randint(15,20))

            except Exception as ex:
                print("Exception: ", ex)
                print(url + " is already liked")
                time.sleep(random.randint(2,5))

            time.sleep(2)


UserParameters = TwitterBot('Probando229', 'pepito3pepito3')
UserParameters.login()
UserParameters.likeTweets(inputVariable, user, hashtag)