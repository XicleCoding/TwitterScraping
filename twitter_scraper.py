import csv
from getpass import getpass
from lib2to3.pgen2 import driver
from pickletools import optimize
from sqlite3 import Timestamp
from ssl import Options
from time import sleep, time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from msedge.selenium_tools import Edge, EdgeOptions

options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)

#navigate in session to login screen
driver.get('https://twitter.com/login')
driver.maximize_window()
sleep(5)

#Enter the username/email
username = driver.find_element_by_xpath('//input[@name="text"]')                                #Find the xpath for email/username box
username.send_keys('TwittyScrapy')                                                              #Write the email/username
username.send_keys(Keys.RETURN)                                                                 #Press ENTER
sleep(3)                                                                                        #Wait 3 seconds

#Enter the password
password = driver.find_element_by_xpath('//input[@name="password"]')                            #Find the xpath for password box
password.send_keys('masterthesis')                                                              #Write the password
password.send_keys(Keys.RETURN)                                                                 #Press ENTER
sleep(3)                                                                                        #Wait 3 seconds

#Search someting
search_input = driver.find_element_by_xpath('//input[@aria-label="Consulta de busca"]')         #Find the xpath for search box
search_input.send_keys('futebol')                                                               #Write the search text
search_input.send_keys(Keys.RETURN)                                                             #Press ENTER
sleep(3)                                                                                        #Wait 3 seconds

#Most recent tweets about the search
driver.find_element_by_link_text('Principais').click()                                          #Find and click on "Mais recentes" option
sleep(3)

'''
#Check infos from a single tweet
userTag = driver.find_element_by_xpath('//div[@data-testid="User-Names"]').text                 #Save username that posted the tweet
print(f'username: {userTag}')
timeStamp = driver.find_element_by_xpath('//time').get_attribute('datetime')                    #Save the tweet Timestamp
print(f'time: {timeStamp}')
tweetText = driver.find_element_by_xpath('//div[@data-testid="tweetText"]').text                #Save the tweet text
print(f'tweet text: {tweetText}')
reply = driver.find_element_by_xpath('//div[@data-testid="reply"]').text
print(f'reply: {reply}')
reTweet = driver.find_element_by_xpath('//div[@data-testid="retweet"]').text
print(f'reTweets: {reTweet}')
likes = driver.find_element_by_xpath('//div[@data-testid="reply"]').text
print(f'likes: {likes}')
'''
cards = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')                        #Save all tweets that page have loaded
card = cards[0]                                                                                 #Choose the 1st tweet

username = card.find_element_by_xpath('.//span').text                                           #Save the tweet username
print(f'username: {username}')

atUsername = card.find_element_by_xpath('.//span[contains(text(), "@")]').text                  #Save the tweet username @
print(f'username @: {atUsername}')

timeStamp = card.find_element_by_xpath('.//time').get_attribute('datetime')                     #Save the tweet timestamp
print(f'time: {timeStamp}')

tweetText = card.find_element_by_xpath('.//div[@data-testid="tweetText"]').text                 #Save the tweet text
print(f'tweet text: {tweetText}')

reply = card.find_element_by_xpath('.//div[@data-testid="reply"]').text                         #Save the tweet repply count
print(f'reply: {reply}')    
    
reTweet = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text                     #Save the tweet retweet count
print(f'retweets: {reTweet}')

likes = card.find_element_by_xpath('.//div[@data-testid="like"]').text                          #Save the tweet likes count
print(f'likes: {likes}')

