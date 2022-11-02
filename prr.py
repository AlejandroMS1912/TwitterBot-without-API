from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import datetime


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(
            executable_path='C:/Users/Usuario/Desktop/Twitterbot/chromedriver.exe')

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        # En la nueva versión del login de twitter, el login está segmentado en dos partes
        time.sleep(3)
        email = bot.find_element("xpath", '//input[@autocomplete="username"]')
        # limpiamos por si las moscas
        email.clear()
        email.send_keys(self.username)
        email.send_keys(Keys.RETURN)
        time.sleep(3)

        password = bot.find_element("xpath", '//input[@name="password"]')
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def go_to_follow(self):

        bot = self.bot

        cookies = bot.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]/div/span/span')        
        cookies.click()

tb = TwitterBot('Probando229', 'pepito3pepito3')
tb.login()
tb.go_to_follow()