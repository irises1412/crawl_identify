from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
#from PIL import Image
import numpy as np
import time
import urllib
from urllib.request import urlretrieve
from selenium.webdriver import ActionChains

def make(path_small,path_big):
    img = Image.open(path_small)
    a = np.array(img,dtype = np.float16)
    img.close()
    img = Image.open(path_big)
    b = np.array(img,dtype = np.float16)
    img.close()
    a_r = a[0:,0:,0]/256
    b_r = b[55:110,0:,0]/256
    max_ = [0,0]
    for i in range(0,268-55):
        temp = b_r[0:,i:i+55]
        s1 = np.sum(np.multiply(a_r,temp))
        s2 = np.linalg.norm(a_r)*np.linalg.norm(temp)
        cos = s1/s2
        if cos > max_[1]:
            max_ = [i,cos]
    return max_[0]


def button_handle(driver):
    time.sleep(2)
    bkg_url=driver.find_element_by_id('validate-big').get_attribute('src')
    blk_url=driver.find_element_by_class_name('validate-block').get_attribute('src')
    
    urlretrieve(bkg_url, 'D://img_get/bkg1.jpg')
    urlretrieve(blk_url, 'D://img_get/blk1.jpg')
    
    distance=make('D://img_get/blk1.jpg','D://img_get/bkg1.jpg')
    pos=[0, 0, 0, 1, 11, 31, 59, 78, 80, 84, 86, 86, 86, 86, 86]
    pos_sub=[0, 0, 1, 10, 20, 28, 19, 2, 4, 2, 0, 0, 0, 0]
    tracks=[i*distance/86 for i in pos_sub]
    element = driver.find_element_by_class_name('drag-button')
    ActionChains(driver).click_and_hold(on_element=element).perform()
    for track in tracks:
        ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(driver).release(on_element=element).perform()

keyword = '5G'
url_base_pattern = 'https://www.toutiao.com/search/?keyword='
url = url_base_pattern + keyword
base_url = 'https://www.toutiao.com'
chrome_options = Options()
#chrome_options.add_argument('--headless')
chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
driver.get(url)
driver.implicitly_wait(10)
# try:
# #     main(url)
# # except:
# #     print("no identify")
# # #main(url)
while(True):
    try:
        button_handle(driver)
        time.sleep(1)
        element = driver.find_element_by_class_name('drag-button')
    except:
        break
driver.close()
print("success")
