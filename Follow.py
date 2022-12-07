from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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
    def __init__(self, username, password, inputVariable, user, hashtag):
        '''
        This method asign the username and the password parameters inputs in the driver that will be used in the following methods
        '''
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(executable_path='HERE') # Copy YOUR chromedriver path
        self.inputvariable = inputVariable
        self.user = user
        self.hashtag = hashtag
        
    def login(self):
        '''
        In this method firstly the driver searchs the login page of twitter, then detects the user and the password boxes and clean
        and fill them with the established parameters
        '''
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(4)

        email = bot.find_element("xpath", '//input[@autocomplete="username"]')
        email.clear()
        email.send_keys(self.username)
        email.send_keys(Keys.RETURN)
        time.sleep(4)

        password = bot.find_element("xpath", '//input[@name="password"]')
        password.send_keys(self.password)
        time.sleep(4)
        password.send_keys(Keys.RETURN)
        time.sleep(4)

    def start_following(self):
        '''
        This method works in the 'following page' determined in the next method (where_to_follow()) and in that page, after a quick 
        scroll, it detects all the usernames and store's them in a list.
        
        Then it starts following each of them with the cooldown parameters established to control the number of follows and to make
        it in the most natural way posible in order to avoid possible bans.
        
        This is fully explained in the README file.
        '''
        bot = self.bot

        ############################################# - Fit the parameters to your needs - ###############################################################

        num_follows = 20 # Max. number of follows of each serie (Recommended: 20)
        minutes = 10 # Cooldown between series of follows (Recommended: 10)
        interval_min, interval_max = (6,18) # Min. and Max. number of seconds of a random interval - Cooldown between each follow (Recommended: (6,18))

        ##################################################################################################################################################
        
        count_follows = 0 # DO NOT CHANGE 
        count_cooldown = 0 # DO NOT CHANGE 
        count_scrolls = 0 # DO NOT CHANGE 
        memory = [] # DO NOT CHANGE 
        usernames_prelist = [] # DO NOT CHANGE
        usernames_list = [] # DO NOT CHANGE

        for k in range(1, 1000):
            if count_scrolls > 0:
                bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(5)
            try: 
                usernames_detected = bot.find_elements("xpath", '//a[@role="link" and @aria-hidden="true"]')
                usernames_prelist = [arroba.get_attribute('href') for arroba in usernames_detected]
            except StaleElementReferenceException:
                pass

            if len(usernames_prelist) == 0:
                break

            for t in usernames_prelist:
                if t not in memory:
                    usernames_list.append(t)
                    memory.append(t)

            print("Memory:", len(memory))

            cleaned_usernames_list = []
            for arroba in usernames_list:
                arroba = "@" + arroba.split("/")[3]
                cleaned_usernames_list.append(arroba)

            print("List of '@' detected (", len(cleaned_usernames_list), "): ", cleaned_usernames_list)

            for n in cleaned_usernames_list:
                   
                time.sleep(2)
                try:
                    follow_button = bot.find_element(By.XPATH, "//div[@aria-label='Follow " + n + "']")
                    webdriver.ActionChains(bot).move_to_element(follow_button).click(follow_button).perform()
                    print("You have followed ", n)
                    count_cooldown += 1
                    count_follows += 1
                    time.sleep(2)

                    if count_cooldown >= (num_follows):
                        print("\n-------------------------------------------------------")
                        print("You have " + str(num_follows) + " consecutive follows, its time to stop (" + str(minutes) + " min). " 
                                  + str(count_follows) + " follows in total.")
                        print("-------------------------------------------------------\n")
                        time.sleep(minutes*60)
                        count_cooldown = 0

                    if count_cooldown < (num_follows):                    
                        print("You have " + str(count_cooldown) + " consecutive follows, " + str(num_follows - count_cooldown)
                             + " left for the next break (" + str(minutes) + " min). " + str(count_follows) + " in total.\n")
                        time.sleep(random.randint(interval_min,interval_max))

                except NoSuchElementException:
                    continue

            count_scrolls += 1

    def where_to_follow(self):
        '''
        This method firstly reject the cookies pop-up to avoid future click problems, then there are two options:

        - If the command was "username", it search's the user inputed and goes to his "following page" to start the following
        process explained in the previous method (start_following())

        - If the command was "hashtag", it search's the hashtag inputed and does a quick scroll to store in a list all the tweets
        and the usernames that had post them, then it goes to the profile and to the "following page" of each of that usernames
        to start the following process explained in the previous method (start_following()).
        '''
        bot = self.bot
        count_scrolls = 0
        
        try:
            RejectCookies = bot.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]/div/span/span')        
            webdriver.ActionChains(bot).move_to_element(RejectCookies).click(RejectCookies).perform()

        except NoSuchElementException:
            pass
        
        if inputVariable == "username":

            bot.get("https://twitter.com/"+ user)
            time.sleep(3)
            bot.get("https://twitter.com/"+ user + "/followers")
            time.sleep(3)

            self.start_following()

        if inputVariable == "hashtag":

            bot.get("https://twitter.com/search?q=" + hashtag + "&src=typed_query")
            time.sleep(3)
            for i in range(1, 1000):
                if count_scrolls == 0:
                    time.sleep(random.uniform(2 - 0.5, 2 + 0.5))
                    bot.execute_script('window.scrollTo(0,document.body.scrollHeight/3)')
                    time.sleep(random.uniform(2 - 0.5, 2 + 0.5))
                    time.sleep(3)
                if count_scrolls > 0:
                    time.sleep(random.uniform(2 - 0.5, 2 + 0.5))
                    bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                    time.sleep(random.uniform(2 - 0.5, 2 + 0.5))
                    time.sleep(3)

                tweets = bot.find_elements("xpath", '//a[@dir="ltr" and @role="link"]')
                tweets_url = [tweet.get_attribute('href') for tweet in tweets]

                for url in tweets_url:
                    bot.get(url)
                    time.sleep(3)

                    if url == 'https://twitter.com/i/keyboard_shortcuts':
                        continue
                    else:
                        time.sleep(1)
                        size = len(url)
                        url = url[:size - 27]
                        bot.get(url)
                        time.sleep(1)
                        url = url + "/followers"
                        bot.get(url)
                        time.sleep(4)
                        self.start_following()

                count_scrolls += 1

UserParameters = TwitterBot('YourUsername', 'YourPassword', inputVariable, user, hashtag) # Type your username and password
UserParameters.login()
UserParameters.where_to_follow()
