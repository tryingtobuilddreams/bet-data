import cv2
import pytesseract
from bs4 import BeautifulSoup
import pandas as pd 
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


MINUTES_TO_RUN = 140
SEC_DELAY = 5
ITERATIONS = (60 / SEC_DELAY) * MINUTES_TO_RUN
ITERATIONS = int(ITERATIONS)
TEAM_ONE = 'LAC'
TEAM_TWO = 'LAL'

SOURCE_URL = 'https://www.bovada.lv/sports/basketball/nba/new-orleans-pelicans-denver-nuggets-201912252240'

with webdriver.Chrome() as driver:
    times = []
    # Retrieves the webpage
    wait = WebDriverWait(driver, 10) 
    driver.get(SOURCE_URL)
    row_ctr = 0
    for val in range(ITERATIONS):
        start_time = time.time()
        driver.save_screenshot(str(row_ctr) + '_' + TEAM_ONE + '_' + TEAM_TWO + '.png')
        time.sleep(SEC_DELAY)
        times.append(start_time)
        row_ctr += 1
    driver.quit()
    time_df = pd.DataFrame()
    time_df['times'] = times
    time_df.to_csv('screen_shot_times.csv')



'''
        image = cv2.imread('/data_screenshots/test_img.png')
        image_text = pytesseract.image_to_string(image)

'''