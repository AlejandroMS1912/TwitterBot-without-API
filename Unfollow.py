from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


class TwitterBot:
    def __init__(self, username, password):
        '''
        This method asign the username and the password parameters inputs in the driver that will be used in the following methods
        '''
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(
            executable_path='C:/Users/Usuario/Desktop/Twitterbot/chromedriver.exe')

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

        The method also has a counter to control the number of unfollows and a random interval of seconds to make it in the most 
        natural way posible in order to avoid possible bans. This is fully explained in the github documentation.
        '''

        bot = self.bot

        RejectCookies = bot.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]/div/span/span')        
        RejectCookies.click()
        
        bot.get("https://twitter.com/"+ username)
        time.sleep(3)
        bot.get("https://twitter.com/"+ username + "/following")
        time.sleep(3)

        usernames_detected = bot.find_elements("xpath", '//a[@role="link" and @aria-hidden="true"]')
        usernames_list = [arroba.get_attribute('href') for arroba in usernames_detected]

        cleaned_usernames_list = []
        for arroba in usernames_list:
            arroba = "@" + arroba.split("/")[3]
            cleaned_usernames_list.append(arroba)
        
        print("Lista de @ detectados (", len(cleaned_usernames_list), "): ", cleaned_usernames_list)

        count_unfollows = 0

        for n in cleaned_usernames_list:
                   
            time.sleep(2)
            unfollows_b = bot.find_element(By.XPATH, "//div[@aria-label='Following " + n + "']")
            webdriver.ActionChains(bot).move_to_element(unfollows_b).click(unfollows_b).perform()
            time.sleep(1)
            unfollows_b_confirm = bot.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
            unfollows_b_confirm.click()
            print("You have unfollowed ", n)
            time.sleep(2)

            if count_unfollows <= 19:
                count_unfollows += 1
                print("You have " + str(count_unfollows) + " consecutive unfollows, " 
                        + str(20 - count_unfollows) + " left for the next break (20 min)")
                time.sleep(random.randint(6,30))


            if count_unfollows > 19:
                print("You have 20 consecutive unfollows, its time to stop (20 min)")
                count_unfollows = 0
                time.sleep(10*60)
                
UserParameters = TwitterBot('Probando2847', 'Hello01134') # Your ('username', 'password')
UserParameters.login()
UserParameters.unfollow('Probando2847') # Your ('username')
