from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import re
import time
from lxml.html import fromstring
import numpy as np
import urllib.request

#获取滑块应移动的距离
def get_distance(path_big,path_small):
    img = Image.open(path_small)
    a = np.array(img,dtype = np.float16)
    img.close()
    img = Image.open(path_big)
    b = np.array(img,dtype = np.float16)
    img.close()
    a_r = a[0:,0:,0:3]/256
    b_r = b[55:110,0:,0:3]/256
    max_ = [0,0]
    for i in range(0,268-55):
        temp = b_r[0:,i:i+55,0:]
        s1 = np.sum(np.multiply(a_r,temp))
        s2 = np.linalg.norm(a_r)*np.linalg.norm(temp)
        cos = s1/s2
        if cos > max_[1]:
            max_ = [i,cos]
    return max_[0]
#     print(max_)
#     b[55:110,max_[0]:max_[0]+55,0] = b_r[0:,max_[0]:max_[0]+55]*256
#     return Image.fromarray(np.uint8(b))

def crackCAPTCH_test(driver): 
    time.sleep(2)
    bkg_url = driver.find_element_by_id('validate-big').get_attribute('src')
    blk_url = driver.find_element_by_class_name('validate-block').get_attribute('src')
    req = urllib.request.Request(bkg_url)
    f_bkg = open(r'D://bkg.jpg','wb+')
    f_bkg.write(urllib.request.urlopen(req).read())
    f_bkg.close()
    req = urllib.request.Request(blk_url)
    f_blk = open(r'D://blk.jpg','wb+')
    f_blk.write(urllib.request.urlopen(req).read())
    f_blk.close()
    
    distance = get_distance(r'D://bkg.jpg',r'D://blk.jpg')
    
    tracks=[]
    current=0
    mid=distance*4/5
    v = 0
    t = 0.2
    while current < distance:
        if current < mid:
            a=2
        else:
            a=-3
        v0 = v
        v=v0+a*t
        s=v0*t+0.5*a*(t**2)
        current+=s
        tracks.append(round(s))
    
    drag_button = driver.find_element_by_class_name('drag-button')
    ActionChains(driver).click_and_hold(on_element= drag_button).perform()
    for track in tracks: 
        ActionChains(driver).move_by_offset(xoffset=track,yoffset=0).perform()
    time.sleep(1)
    ActionChains(driver).release(on_element= drag_button).perform()
    
# keyword_list= ['iPhone','特斯拉','耐克']

keyword = '5G'
url_base_pattern = 'https://www.toutiao.com/search/?keyword='
# for keyword in keyword_list:  
url = url_base_pattern + keyword
chrome_options = Options()
#chrome_options.add_argument('--headless')
chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
driver.get(url)
driver.implicitly_wait(10)
while (True):
    try:
        crackCAPTCH_test(driver)
        time.sleep(1)
        drag_button = driver.find_element_by_class_name('drag-button')
        print('loop')
    except:
        break
driver.close()
print('success')
