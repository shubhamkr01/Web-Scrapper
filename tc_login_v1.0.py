import time
import re
from selenium import webdriver

#def tc_login():
browser=webdriver.Chrome()
browser.get('https://www.truecaller.com')
user=browser.find_element_by_css_selector('.searchbar-query')
user.send_keys('8800143011')
login=browser.find_element_by_css_selector('.searchbar-submit')
login.click()
time.sleep(5)
button=browser.find_element_by_css_selector('.sign-in-dialog-provider')
button.click()
time.sleep(5)
enter_mail=browser.find_element_by_css_selector('.whsOnd')
enter_mail.send_keys('mgreat972')
next_click=browser.find_element_by_css_selector('.RveJvd')
next_click.click()
time.sleep(5)
enter_pass=browser.find_element_by_css_selector('.whsOnd')
enter_pass.send_keys('defaulterishere')
next_click=browser.find_element_by_css_selector('.RveJvd')
next_click.click()
time.sleep(5)
regex='<div class="profile-details-text profile-details-text-concat"><div>(.+?)</div> <div>Email</div></div>'
pattern=re.compile(regex)
#html=urllib.urlopen(browser.current_url)
#htmltext=html.read()
mail=re.findall(pattern,browser.page_source)
print (mail)
