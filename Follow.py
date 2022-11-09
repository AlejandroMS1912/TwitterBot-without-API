from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException             
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
        time.sleep(4)

        email = bot.find_element("xpath", '//input[@autocomplete="username"]')
        email.clear()
        email.send_keys(self.username)
        email.send_keys(Keys.RETURN)
        time.sleep(4)

        password = bot.find_element("xpath", '//input[@name="password"]')
        password.send_keys(self.password)
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
        
        count_follows = 0 # DO NOT CHANGE - Always has to be 0

        for k in range(1, 1000):
                bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(5)

                usernames_detected = bot.find_elements("xpath", '//a[@role="link" and @aria-hidden="true"]')
                usernames_list = [arroba.get_attribute('href') for arroba in usernames_detected]

                cleaned_usernames_list = []
                for arroba in usernames_list[0:15]:
                    arroba = "@" + arroba.split("/")[3]
                    cleaned_usernames_list.append(arroba)

                print("List of '@' detected (", len(cleaned_usernames_list), "): ", cleaned_usernames_list)

                for n in cleaned_usernames_list:
                   
                    time.sleep(2)
                    try:
                        follow_button = bot.find_element(By.XPATH, "//div[@aria-label='Follow " + n + "']")
                        webdriver.ActionChains(bot).move_to_element(follow_button).click(follow_button).perform()
                        print("You have followed ", n)
                
                        time.sleep(2)

                        if count_follows <= (num_follows - 1):
                            count_follows += 1
                            print("You have " + str(count_follows) + " consecutive follows, " + str(num_follows - count_follows)
                             + " left for the next break (" + str(minutes) + " min)")
                            time.sleep(random.randint(interval_min,interval_max))


                        if count_follows > (num_follows - 1):
                            print("You have " + str(num_follows) + " consecutive follows, its time to stop (" + str(minutes) + " min)")
                            time.sleep(minutes*60)
                            count_follows = 0

                    except NoSuchElementException:
                        continue

    def where_to_follow(self, inputVariable, user, hashtag):
        '''
        This method firstly reject the cookies pop-up to avoid future click problems, then there are two options:

        - If the command was "username", it search's the user inputed and goes to his "following page" to start the following
        process explained in the previous method (start_following())

        - If the command was "hashtag", it search's the hashtag inputed and does a quick scroll to store in a list all the tweets
        and the usernames that had post them, then it goes to the profile and to the "following page" of each of that usernames
        to start the following process explained in the previous method (start_following()).
        '''
        bot = self.bot

        RejectCookies = bot.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]/div/span/span')        
        RejectCookies.click()
        
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
                bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(2)

                tweets = bot.find_elements("xpath", '//a[@dir="auto" and not(@rel)]')
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

UserParameters = TwitterBot('YourUsername', 'YourPassword') # Your ('username', 'password')
UserParameters.login()
UserParameters.where_to_follow(inputVariable, user, hashtag)
