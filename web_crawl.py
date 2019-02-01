from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import lxml
import time

start=time.time()

urls="http://charliech17.pixnet.net/blog"

#driver = webdriver.PhantomJS()

chromeOptions = webdriver.ChromeOptions()
chromeOptions.headless = True
driver=webdriver.Chrome(chrome_options=chromeOptions)
driver.get(urls)
innerHTML = driver.execute_script("return document.body.innerHTML")
##print(driver.page_source)

import bs4
import re
from time import sleep

sleep(5)
root=bs4.BeautifulSoup(innerHTML,"lxml")
viewcount=root.find_all("span",attrs={'id':re.compile('blog_hit')}) #attrs={'class':'short-view-count style-scope yt-view-count-renderer'}

#viewcount=root.find_all("h2",attrs={'class':re.compile('capsule__title fixpadv--m')})
count=0
for span in viewcount:
 if count==0:
    print("本日人氣",span.string)
    count+=1
 else:
    print("累積人氣",span.string)
   


   
end=time.time()
sec=end-start
print("爬蟲花費時間",sec,"秒")
driver.quit()