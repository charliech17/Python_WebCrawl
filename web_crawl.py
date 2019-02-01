from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

start=time.time()

urls="http://charliech17.pixnet.net/blog"

#driver = webdriver.PhantomJS()

chromeOptions = webdriver.ChromeOptions()
chromeOptions.headless = True
driver=webdriver.Chrome(chrome_options=chromeOptions)
driver.get(urls)


inner_text1= driver.execute_script("return arguments[0].innerText;", driver.find_element(By.XPATH, '//*[@id="blog_hit_daily"]'))
inner_text2= driver.execute_script("return arguments[0].innerText;", driver.find_element(By.XPATH, '//*[@id="blog_hit_total"]'))

print("本日人氣 ",inner_text1,"\n")
print("累積人氣",inner_text2,"\n")
   
end=time.time()
sec=end-start
print("爬蟲花費時間",sec,"秒")
driver.quit()