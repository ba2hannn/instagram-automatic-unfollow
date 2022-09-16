from re import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
username = input('Lütfen kullanıcı adını giriniz: ') 
password = input('Lütfen şifrenizi giriniz: ')  
class Unfollow:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()    

    def open_file(self):
        file_followers1 = open("takipetmeyenlerasil.txt" , "r+" , encoding="UTF-8")
        file_followers_read1 = file_followers1.readlines()
        self.file_followers_readed1 = [x[:-1] for x in file_followers_read1]
        self.file_takip_cik = open("takiptencikilanlar.txt", "a" , encoding="UTF-8")


    def open_insta(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        
        time.sleep(2)
        
        self.browser.maximize_window()
        
        time.sleep(2)
                
        username1 = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        Password1 = self.browser.find_element(By.XPATH , "//*[@id='loginForm']/div/div[2]/div/label/input")
        username1.send_keys(self.username)
        Password1.send_keys(self.password)
                
        time.sleep(2)
                
        giris_yap = self.browser.find_element(By.XPATH , "//*[@id='loginForm']/div/div[3]/button")
        giris_yap.click()
                
        time.sleep(8)

    def open_browser(self):
        uzunluk = len(self.file_followers_readed1)
        a = -1
        while True:
            a += 1
            if a == uzunluk:
                self.browser.close()
                break
            else:                
                self.browser.get(f'https://www.instagram.com/{self.file_followers_readed1[a]}/')
                time.sleep(3)

                self.insta_unfollow= self.browser.find_element(By.CSS_SELECTOR,"._ab8w._ab94._ab99._ab9h._ab9k._ab9p._ab9-._abcm").click()
                time.sleep(2)

                self.insta_unfollow1= self.browser.find_element(By.CSS_SELECTOR,"._a9--._a9-_").click()
                time.sleep(1)
                self.file_takip_cik.write(self.file_followers_readed1[a]+'\n')
                time.sleep(1)

                with open('TakipEtmeyenlerAsil.txt', 'r+', encoding='utf-8') as fin:
                    data = fin.read().splitlines(True)
                with open('TakipEtmeyenlerAsil.txt', 'w', encoding='utf-8') as fout:
                    fout.writelines(data[1:])

                time.sleep(40)





work = Unfollow(username,password)
work.open_file()
work.open_insta()
work.open_browser()