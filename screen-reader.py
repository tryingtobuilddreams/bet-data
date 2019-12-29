import cv2 as cv
import pytesseract
import numpy as np
import pandas as pd

all_times = pd.read_csv('screen_shot_times.csv')
all_text = pd.DataFrame(columns=['data','time'])

#3,1483
for idx in range(3,1483):
    # Read in screenshot and template image as grayscale
    base_img = cv.imread(str(idx) + '_LAC_LAL.png',0)
    crop_img = base_img[460:530, 100:850]

    # binary thresholding improves readability - 170
    ret,thresh1 = cv.threshold(crop_img,170,255,cv.THRESH_BINARY)

    subset_text = pytesseract.image_to_string(thresh1)

    # adds each value to the dataframe
    all_text.at[idx, 'data'] = subset_text
    all_text.at[idx, 'time'] = all_times.at[idx, 'times']

    print(subset_text)

all_text.to_csv('all_betting_data.csv')


# TODO identify common patterns and adjust for them 

# if spread
'''
 - 0 - 
"New Orleans Pelicans +85 (-110) +380 0214.5 (-115)
Live Match 35>
Denver Nuggets -B5 (125) 600 214.5 (115)"

- 5 -
"New Orleans Pelicans +85 (-110) +350 0218.5 (-115)
Live Match 35>
Denver Nuggets -B5 (125) 600 218.5 (115)"

'''