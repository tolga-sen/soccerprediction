from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import numpy as np

PAUL_PATH='/Users/PaulWlodkowski/Documents/PythonWork/\
SPICED-Work/chromedriver/chromedriver'
DRIVER = webdriver.Chrome()

def get_stats_from_window(driver, handle_number):
    driver.switch_to.window(handle_number)
    new_link = driver.current_url
    time.sleep(1)
#    game_info = driver.find_elements_by_xpath('//span[@class="tname"]')
#    game_info = '-'.join([i.text for i in game_info])
#    print(f'TESTING!!!:{game_info}\n\n')
    game_info1 = DRIVER.find_elements_by_xpath('//td[@class="tname-home logo-enable"]')
    game_info2 = DRIVER.find_elements_by_xpath('//td[@class="tname-away logo-enable"]')
    #    game_info = '-'.join([i.text for i in game_info])
    game_info1 = '-'.join([i.text for i in game_info1])
    game_info2 = '-'.join([i.text for i in game_info2])
    game_info = game_info1+'_'+game_info2
    #print(f'TESTING!!!:{game_info3}\n\n')
    print(f'TESTING!!!:{game_info}\n\n')

    statistics1=new_link[:-7]+"statistics;1"
    time.sleep(1)

    try:
        driver.get(statistics1)
        time.sleep(1)
        login_form=driver.find_element_by_xpath('//div[@id="tab-statistics-1-statistic"]')
        statistics1=login_form.text
        print(statistics1)
        with open(f'game_data/eng1819/half_{game_info}.txt', 'a') as f:
            f.write(statistics1)

        new_link = driver.current_url
        statistics2=new_link[:-7]+"statistics;0"
        driver.get(statistics2)
        time.sleep(1)
        login_form=driver.find_element_by_xpath('//div[@id="tab-statistics-0-statistic"]')
        statistics2=login_form.text
        with open(f'game_data/eng1819/endd_{game_info}.txt', 'a') as f:
            f.write(statistics2)

        new_link = driver.current_url
        goals=new_link[:-12]+"summary"
        time.sleep(1)
        driver.get(goals)
        time.sleep(1)
        login_form=driver.find_element_by_xpath('//div[@id="summary-content"]')
        goals=login_form.text
        with open(f'game_data/eng1819/goal_{game_info}.txt', 'a') as f:
            f.write(goals)

        new_link = driver.current_url
        info=new_link[:-12]+"summary"
#         print(info)
        time.sleep(1)
        driver.get(info)
        time.sleep(1)
        login_form=driver.find_element_by_xpath('//td[@id="flashscore_column"]')
        info=login_form.text
#         print(info)
        with open(f'game_data/eng1819/info_{game_info}.txt', 'a') as f:
            f.write(info)

    except:
        print("No Statistics for this game!!!")

if __name__ == '__main__':

    DRIVER.get("https://www.soccerstand.com/soccer/england/premier-league-2018-2019/results/")
    time.sleep(2)

#   Action and showmore for the previous seasons where there is a button to load previous games !!
#   if you are working with a season where all the games are load the page, you don't need 'showmore' part

    action = webdriver.common.action_chains.ActionChains(DRIVER)
    showmore = DRIVER.find_element_by_xpath('//table[@class="link-more-games"]')
    time.sleep(2)
    count=4
    while count >1:
        showmore.location_once_scrolled_into_view
        actions = ActionChains(DRIVER)
        actions.click(showmore).perform()
        time.sleep(2)
        count-=1

        ELEMENTS = DRIVER.find_elements_by_class_name('padr')
    for elem in ELEMENTS:
        time.sleep(2)
        DRIVER.execute_script("$(arguments[0]).click();", elem)

        start_window = DRIVER.window_handles[0]
        current_window = DRIVER.window_handles[-1]
        print(current_window)
        get_stats_from_window(DRIVER, current_window)
        print(f'Successfully wrote data....')
        DRIVER.close() #closes the current window
        DRIVER.switch_to.window(start_window)

        assert len(DRIVER.window_handles) == 1
