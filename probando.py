from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(
            executable_path='C:/Users/Usuario/Desktop/Twitterbot/chromedriver.exe')

    def login(self):
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

    def Follow_from_hashtag(self, hashtag):

        bot = self.bot
        bot.get("https://twitter.com/search?q=" + hashtag + "&src=typed_query")
        time.sleep(3)
        for i in range(1, 3):
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

                arrobas = bot.find_elements("xpath", '//a[@role="link" and @aria-hidden="true"]')
                lista_arrobas = [arroba.get_attribute('href') for arroba in arrobas]
                #print(lista_arrobas)

                lista_arr_def = []
                for arroba in lista_arrobas:
                    arroba = "@" + arroba.split("/")[3]
                    lista_arr_def.append(arroba)
                    #print(arroba)
                print("Lista de @ detectados", lista_arr_def)

                cont_follows = 0
                for n in lista_arr_def:
                   
                    follows_b = bot.find_element(By.XPATH, "//div[@aria-label='Follow " + n + "']")
                    webdriver.ActionChains(bot).move_to_element(follows_b).click(follows_b).perform()
                    print("Has empezado a seguir a ", n)

                    if cont_follows <= 20:
                        cont_follows += 1
                        print("Llevas " + str(cont_follows) + " follows consecutivos, te quedan " 
                               + str(20 - cont_follows) + " para el siguiente descanso (20 min)")
                        time.sleep(random.randint(6,30))


                    if cont_follows > 20:
                        print("Llevas 20 follows consecutivos, te toca descansar (20 min)")
                        cont_follows = 0
                        time.sleep(1200)




UserParameters = TwitterBot('Probando229', 'pepito3pepito3')
UserParameters.login()
UserParameters.Follow_from_hashtag('drop handles')