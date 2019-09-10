from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.soccerstand.com/team/amiens-sc/lKkBAsxF/results/")
element=driver.find_element_by_class_name('padr')
location=element.location
size=element.location
#print(location)
time.sleep(3)
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(element, 0, 0)
action.click()
action.perform()
handles = driver.window_handles
size = len(handles)
for x in range(1,size):
    driver.switch_to.window(handles[x])
    new_link = driver.current_url
    statistics1=new_link[:-7]+"statistics;1"
    print(statistics1)
    driver.get(statistics1)

#    driver.close()

"""
for i in range(0,170,23):
    action.move_to_element_with_offset(element, 0, i)
    action.click()
    action.perform()
    print(i)
# coordinates (type to terminal):
# while true; do clear; xdotool getmouselocation; sleep 0.1; done
"""
