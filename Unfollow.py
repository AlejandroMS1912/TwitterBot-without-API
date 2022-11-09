from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException             
import time
import random


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

    def unfollow(self, username):
        '''
        This method firstly reject the cookies pop-up to avoid future click problems, then search your profile page and your 
        "following page". After a quick scroll in that page detects all the usernames and store them in a list that will
        later be the index from wich unfollow each of them.

        Then it starts unfollowing each of them with the cooldown parameters established to control the number of follows and to make
        it in the most natural way posible in order to avoid possible bans. This is fully explained in the README file.
        '''
        bot = self.bot

        ############################################# - Fit the parameters to your needs - ###############################################################

        num_unfollows = 20 # Max. number of unfollows of each serie (Recommended: 20)
        minutes = 10 # Cooldown between series of unfollows (Recommended: 10)
        interval_min, interval_max = (6,18) # Min. and Max. number of seconds of a random interval - Cooldown between each unfollow (Recommended: (6,18))

        ##################################################################################################################################################
        
        count_unfollows = 0 # DO NOT CHANGE - Always has to be 0

        RejectCookies = bot.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]/div/span/span')        
        RejectCookies.click()
        
        bot.get("https://twitter.com/"+ username)
        time.sleep(3)
        bot.get("https://twitter.com/"+ username + "/following")
        time.sleep(3)

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
                        unfollows_b = bot.find_element(By.XPATH, "//div[@aria-label='Following " + n + "']")
                        webdriver.ActionChains(bot).move_to_element(unfollows_b).click(unfollows_b).perform()
                        time.sleep(1)
                        unfollows_b_confirm = bot.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
                        unfollows_b_confirm.click()
                        print("You have unfollowed ", n)
                        time.sleep(2)

                        if count_unfollows <= (num_unfollows - 1):
                            count_unfollows += 1
                            print("You have " + str(count_unfollows) + " consecutive follows, " + str(num_unfollows - count_unfollows)
                             + " left for the next break (" + str(minutes) + " min)")
                            time.sleep(random.randint(interval_min, interval_max))


                        if count_unfollows > (num_unfollows - 1):
                            print("You have " + str(num_unfollows) + " consecutive follows, its time to stop (" + str(minutes) + " min)")
                            time.sleep(minutes*60)
                            count_unfollows = 0

                    except NoSuchElementException:
                        continue
                
UserParameters = TwitterBot('YourUsername', 'YourPassword') # Your ('username', 'password')
UserParameters.login()
UserParameters.unfollow('YourUsername') # Your ('username')
