from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
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
        self.bot = webdriver.Chrome(executable_path='C:/Users/Usuario/Desktop/TwitterBot-without-API-main/chromedriver.exe') # Copy YOUR chromedriver path

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

    def start_liking(self):
        '''
        This method works in the inputed page determined in the next method (where_to_like()) and in that page, after a quick 
        scroll, it detects all the like buttons and store's them in a list.
        
        Then it starts clicking each of them with the cooldown parameters established to control the number of likes and to make it
        in the most natural way posible in order to avoid possible bans. 
        
        This is fully explained in the README file.
        '''
        bot = self.bot

        ############################################# - Fit the parameters to your needs - ###############################################################

        num_likes = 50 # Max. number of likes of each serie (Recommended: 50)
        minutes = 5 # Cooldown between series of likes (Recommended: 5)
        interval_min, interval_max = (6,18) # Min. and Max. number of seconds of a random interval - Cooldown between each like (Recommended: (6,18))

        ##################################################################################################################################################
        
        count_likes = 0 # DO NOT CHANGE - Always has to be 0
        count_cooldown = 0 # DO NOT CHANGE - Always has to be 0

        time.sleep(3)
        for i in range(1, 1000):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            likeButton_list = bot.find_elements("xpath", '//div[@role="button" and @data-testid="like"]')             
            print("Tweets to Like: (", (len(likeButton_list)), ")")
            for likeButton in likeButton_list:
                try:
                    webdriver.ActionChains(bot).move_to_element(likeButton).click(likeButton).perform()
                    print("Tweet successfully liked")
                    count_cooldown += 1
                    count_likes += 1
                    
                    if count_cooldown > (num_likes - 1):
                        print("You have " + str(num_likes) +" consecutive likes, its time to stop (" + str(minutes) + " min). " 
                        + str(count_likes) + " in total.\n\n")
                        time.sleep(minutes*60)
                        count_cooldown = 0

                    if count_cooldown <= (num_likes - 1):
                        print("You have " + str(count_cooldown) + " consecutive likes, " + str(num_likes - count_cooldown) + " left for the next break (" + str(minutes)
                              + " min). " + str(count_likes) + " in total.\n")
                        time.sleep(random.randint(interval_min,interval_max))

                except StaleElementReferenceException:
                    continue

    def where_to_like(self, inputVariable, user, hashtag):
        '''
        This method firstly reject the cookies pop-up to avoid future click problems, then there are two options:

        - If the command was "username", it goes to the user inputed profile page to start the liking process explained in
        the previous method (start_liking())

        - If the command was "hashtag", it goes to the inputed hashtag page to start the liking process explained in
        the previous method (start_liking())
        '''
        bot = self.bot

        RejectCookies = bot.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]/div/span/span')        
        RejectCookies.click()

        if inputVariable == "username":
            bot.get("https://twitter.com/" + user)
            self.start_liking()

        if inputVariable == "hashtag":
            bot.get("https://twitter.com/search?q=" + hashtag + "&src=typed_query")
            self.start_liking()

UserParameters = TwitterBot('YourUsername', 'YourPassword') # Your ('username', 'password')
UserParameters.login()
UserParameters.where_to_like(inputVariable, user, hashtag)
