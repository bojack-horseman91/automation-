# This is a sample Py
from selenium import webdriver
import time

followers=[]
followings=[]
def getFollowers():
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(1)
        scroll = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        last_h1, h1 = 0, 1

        while last_h1 != h1:
                last_h1 = h1
                time.sleep(3)
                h1 = driver.execute_script("""
                arguments[0].scrollTo(0,arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll)
        links = scroll.find_elements_by_tag_name('a')

        f = [name.text for name in links if name.text != '' and time.sleep(2)]
        print(f)
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
        return f
def getFollowings():
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(1)
        scroll = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        last_h1, h1 = 0, 1

        while last_h1 != h1:
                last_h1 = h1
                time.sleep(4)
                h1 = driver.execute_script("""
                        arguments[0].scrollTo(0,arguments[0].scrollHeight);
                        return arguments[0].scrollHeight;
                        """, scroll)
        links = scroll.find_elements_by_tag_name('a')

        f = [name.text  for name in links if name.text != '' and time.sleep()]
        time.sleep(4)
        print(f)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
        return f
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.instagram.com/');
time.sleep(3)
#ADD EMAIL HERE
EMAIL=''
#ADD PASSWORD HERE
password=''
#faceboook
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[5]/button/span[2]').click()
field=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input').send_keys(EMAIL)
field=driver.find_element_by_xpath('//input[@name=\"pass\"]').send_keys(password)
#login

driver.find_element_by_xpath('//button[@name=\"login\"]').click()
time.sleep(20)
print('trying...')

time.sleep(5)
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/form/div/div[1]/div[1]/div/div/div[3]/button[1]').click()
time.sleep(12)
#profile
driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a').click()
time.sleep(2)

time.sleep(2)

followers=getFollowers()
time.sleep(2)
followings=getFollowings()
time.sleep(2)
print(followings)
print(followers)
time.sleep(2)
imposters=[name for name in followings if followers.count(name)==0]
print(imposters)