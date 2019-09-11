from selenium import webdriver
import time
import numpy as np

DRIVER = webdriver.Chrome()

def get_stats_from_window(driver, handle_number):
    driver.switch_to.window(handle_number)
    new_link = driver.current_url
    statistics1=new_link[:-7]+"statistics;1"
    time.sleep(2)

    try:
        driver.get(statistics1)
        time.sleep(2)
        login_form=driver.find_element_by_xpath('//div[@id="tab-statistics-1-statistic"]')
        statistics1=login_form.text
        with open('half.txt', 'a') as f:
            f.write('-----')
            f.write(statistics1)
            f.write('-----')

        new_link = driver.current_url
        statistics2=new_link[:-7]+"statistics;0"
        driver.get(statistics2)
        time.sleep(2)
        login_form=driver.find_element_by_xpath('//div[@id="tab-statistics-0-statistic"]')
        statistics2=login_form.text
        with open('end.txt', 'a') as f:
            f.write('-----')
            f.write(statistics2)
            f.write('-----')

        new_link = driver.current_url
        goals=new_link[:-12]+"summary"
        time.sleep(2)
        driver.get(goals)
        time.sleep(2)
        login_form=driver.find_element_by_xpath('//div[@id="summary-content"]')
        goals=login_form.text
        with open('goal.txt', 'a') as f:
            f.write('-----')
            f.write(goals)
            f.write('-----')

        new_link = driver.current_url
        info=new_link[:-12]+"summary"
#         print(info)
        time.sleep(3)
        driver.get(info)
        time.sleep(3)
        login_form=driver.find_element_by_xpath('//td[@id="flashscore_column"]')
        info=login_form.text
#         print(info)
        with open('info.txt', 'a') as f:
            f.write('-----')
            f.write(info)
            f.write('-----')

    except:
        print("No Statistics for this game!!!")

if __name__ == '__main__':

    DRIVER.get("https://www.soccerstand.com/team/amiens-sc/lKkBAsxF/results/")
    time.sleep(2)
    action = webdriver.common.action_chains.ActionChains(DRIVER)
    ELEMENTS = DRIVER.find_elements_by_class_name('padr')

    for elem in ELEMENTS:
        time.sleep(3)
        print(elem, elem.text)
        DRIVER.execute_script("arguments[0].scrollIntoView();", elem)
        DRIVER.execute_script("$(arguments[0]).click();", elem)

        start_window = DRIVER.window_handles[0]
        current_window = DRIVER.window_handles[-1]
        get_stats_from_window(DRIVER, current_window)
        print(f'Successfully wrote data....')
        DRIVER.close() #closes the current window
        DRIVER.switch_to.window(start_window)

        assert len(DRIVER.window_handles) == 1
