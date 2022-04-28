import numpy as np
import pandas as pd
import cv2


import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
from matplotlib.pyplot import figure

import os
from utils import *


from .Pre_processing_arabic import preprocessing_before_crop_Axis_arabic


def get_contour_precedence_date(contour_date, cols_date):
    tolerance_factor_date = 80
    origin_date = cv2.boundingRect(contour_date)
    return ((origin_date[1] // tolerance_factor_date) * tolerance_factor_date) * cols_date + origin_date[0]


def date_cropping_arabic(cropped_image):
    date_image = cropped_image[0:1000, 6200:9000]
    # detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
    contours_date, hierarchy_date = cv2.findContours(image=date_image, mode=cv2.RETR_TREE,
                                                     method=cv2.CHAIN_APPROX_SIMPLE)
    contours_date = list(contours_date)
    # sorting contours
    contours_date.sort(key=lambda x: get_contour_precedence_date(x, date_image.shape[1]))
    # Find contours, obtain bounding box, extract and save ROI
    ROI_number_date = 0
    for c in contours_date:
        x, y, w, h = cv2.boundingRect(c)
        if 107 < h < 300 and 50 < w < 200:  # DO NOT CHANGE ==========>>>>>> 107
            cv2.rectangle(date_image, (x, y), (x + w, y + h), (0, 0, 0), 2)
            ROI_date = date_image[y:y + h, x:x + w]
            cv2.imwrite(
                r'C:\Users\ADEM\Desktop\ESPRIT_Education\4er\PI DS\image preprocessing\Arabic cheques\segmented date arabic\ROI_{}.png'.format(
                    ROI_number_date), ROI_date)
            ROI_number_date += 1

    return date_image
