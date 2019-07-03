from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
#from PIL import Image
import numpy as np
import time
import urllib
from urllib.request import urlretrieve
from selenium.webdriver import ActionChains


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
time.sleep(3)
pos_all=[]
pos_sub=[]
print('start')
start = time.time()
i = 1
while((time.time()-start )<3):
    all_time = (time.time()-start)/0.2
    if int(all_time) == i:
        i += 1
        pos=driver.find_element_by_class_name('validate-drag-button').get_attribute('style')
        position = re.findall(r'left: ([0-9]+)px',pos)
        pos0 = int(position[0])
        pos_all.append(pos0)
        if(i>2):
            temp=pos_all[i-2]-pos_all[i-3]
            pos_sub.append(temp)
#print(pos_all)
#print(pos_sub)
