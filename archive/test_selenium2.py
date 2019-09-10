from selenium import webdriver
import time
import numpy as np

DRIVER = webdriver.Chrome('/Users/PaulWlodkowski/Documents/PythonWork/\
SPICED-Work/chromedriver/chromedriver')

def get_stats_from_window(driver, handle_number):
    driver.switch_to.window(handle_number)
    new_link = driver.current_url
    statistics1=new_link[:-7]+"statistics;1"
    time.sleep(2)

    try:
        driver.get(statistics1)
        time.sleep(2)
        login_form=driver.find_element_by_xpath('//div[@id="tab-statistics-1-statistic"]')
    #    if login_form:
        statistics1=login_form.text
        print(statistics1)
        with open('half.txt', 'a') as f:
            f.write(statistics1)
            f.write('-----')

        new_link = driver.current_url
        statistics2=new_link[:-7]+"statistics;0"
        print(statistics2)
        driver.get(statistics2)
        time.sleep(2)
        login_form=driver.find_element_by_xpath('//div[@id="tab-statistics-0-statistic"]')
        statistics2=login_form.text
        print(statistics2)
        with open('end.txt', 'a') as f:
            f.write(statistics2)
            f.write('-----')

        new_link = driver.current_url
        goals=new_link[:-12]+"summary"
        print(goals)
        time.sleep(2)
        driver.get(goals)
        time.sleep(2)
        login_form=driver.find_element_by_xpath('//div[@id="summary-content"]')
        goals=login_form.text
        print(goals)
        with open('goal.txt', 'a') as f:
            f.write(goals)
            f.write('-----')

        new_link = driver.current_url
        info=new_link[:-12]+"summary"
        print(info)
        time.sleep(3)
        driver.get(info)
        time.sleep(3)
        login_form=driver.find_element_by_xpath('//td[@id="flashscore_column"]')
        info=login_form.text
        print(info)
        with open('info.txt', 'a') as f:
            f.write(info)
            f.write('-----')

    except:
        print("No Statistics for this game!!!")


if __name__ == '__main__':

    DRIVER.get("https://www.soccerstand.com/team/amiens-sc/lKkBAsxF/results/")
    # LOCATION = ELEMENT.location

    time.sleep(3)
    action = webdriver.common.action_chains.ActionChains(DRIVER)
    ELEMENT = DRIVER.find_element_by_class_name('padr')
    print(ELEMENT)
    action.move_to_element_with_offset(ELEMENT, 0, 0)
    action.click()
    action.perform()

    HANDLES = DRIVER.window_handles
    print(HANDLES)

    # get_stats_from_window(DRIVER, HANDLES[-1])
    # DRIVER.close()


    # for i in range(0,70,23):
    #     action.move_to_element_with_offset(element, 0, i)
    #     action.click()
    #     action.perform()
    #     last_window=driver.window_handles[-1]
    #     driver.switch_to_window(last_window)
    #     time.sleep(3)
    #     current_window = driver.current_window_handle
    #     print('LAST WINDOW IS HERE:',last_window)
    #     print('CURRENT WINDOW IS HERE:',current_window)
    #     print('\n\n\n')
    #     print(i)
    #     time.sleep(4)
    #     handles=list(driver.window_handles)
    #     print('NUMBER OF WINDOWS OPEN:',len(handles))
    #     get_stats_from_window(last_window)
    #     driver.close()
    #     handles=list(driver.window_handles)
    #     print('NUMBER OF WINDOWS OPEN AFTER DRIVER CLOSE:',len(handles))
    #     driver.switch_to_window(handles[0])
    # driver.quit()
