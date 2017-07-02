import re
import time
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.truecaller.com')
user=browser.find_element_by_css_selector('.searchbar-query')
user.send_keys('')#any mobile no. registered with truecaller
login=browser.find_element_by_css_selector('.searchbar-submit')
login.click()
time.sleep(5)
button=browser.find_element_by_css_selector('.sign-in-dialog-provider')
button.click()
time.sleep(5)
enter_mail=browser.find_element_by_css_selector('.whsOnd')
enter_mail.send_keys('')#gmail ID here
next_click=browser.find_element_by_css_selector('.RveJvd')
next_click.click()
time.sleep(5)
enter_pass=browser.find_element_by_css_selector('.whsOnd')
enter_pass.send_keys('')#gmail password here
next_click=browser.find_element_by_css_selector('.RveJvd')
next_click.click()
time.sleep(10)
regex='<div class="profile-details-text profile-details-text-concat"><div>(.+?)</div> <div>Email</div></div>'
pattern=re.compile(regex)
#html=urllib.urlopen(browser.current_url)
#htmltext=html.read()
mail=re.findall(pattern,browser.page_source)
print (mail)
mail_list=[]
mail_list.append(mail)
count=1
#entering into the loop
for i in range(300):
    if(len(mail_list)<200):
        try:
            if((i*5+(8-i))%3==0):
                browser.execute_script("window.history.go(-1)")
                time.sleep(20+i)
                browser.execute_script("window.history.go(+1)")
            browser.find_element_by_css_selector('#app > div.navbar > div:nth-child(2) > div > div.searchbar-inputs > input').clear()
            next_no=browser.find_element_by_css_selector('#app > div.navbar > div:nth-child(2) > div > div.searchbar-inputs > input')
            next_no.send_keys(list_of_nos[i])
            next_click=browser.find_element_by_css_selector('#app > div.navbar > div:nth-child(2) > div > div.searchbar-inputs > button.searchbar-submit')
            next_click.click()
            time.sleep(10 + 3*(i%5))
            regex='<div class="profile-details-text profile-details-text-concat"><div>(.+?)</div> <div>Email</div></div>'
            pattern=re.compile(regex)
            #html=urllib.urlopen(browser.current_url)
            #htmltext=html.read()
            mail=re.findall(pattern,browser.page_source)
            if (mail==[]):
                print('0')
            else:
                print (mail)
                if(mail in mail_list):
                    pass
                else:
                    mail_list.append(mail)
                    count+=1
            #end of loop
        #except selenium.common.exceptions.WebDriverException:
        #   print("Selenium Error")
        except ConnectionResetError:
            print("You reset or closed conection")
            pass
for j in range(len(mail_list)):
    print(mail_list[j])
with open('test.csv','w',newline='') as fp:
    a=csv.writer(fp,delimiter=',')
    data=[['Mail_id']]
    a.writerows(data)
    a.writerows(mail_list)

