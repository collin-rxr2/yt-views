from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fp.fp import FreeProxy
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

banner = """
Y88b   d88P            88888888888       888               
 Y88b d88P                 888           888               
  Y88o88P                  888           888               
   Y888P  .d88b.  888  888 888  888  888 88888b.   .d88b.  
    888  d88""88b 888  888 888  888  888 888 "88b d8P  Y8b 
    888  888  888 888  888 888  888  888 888  888 88888888 
    888  Y88..88P Y88b 888 888  Y88b 888 888 d88P Y8b.     
    888   "Y88P"   "Y88888 888   "Y88888 88888P"   "Y8888  

888     888 d8b                                            
888     888 Y8P                                            
888     888                                                
Y88b   d88P 888  .d88b.  888  888  888 .d8888b             
 Y88b d88P  888 d8P  Y8b 888  888  888 88K                 
  Y88o88P   888 88888888 888  888  888 "Y8888b.            
   Y888P    888 Y8b.     Y88b 888 d88P      X88            
    Y8P     888  "Y8888   "Y8888888P"   88888P'            
by rblxcollin"""

print(banner)

url = input("URL > ")
times = input("VIEWS > ")

print("Please wait...")

for i in range(int(times)):
    capabilities = DesiredCapabilities.CHROME
    capabilities['proxy'] = {
        'httpProxy': FreeProxy(anonym=True, rand=True).get(),
        'noProxy': None,
        'proxyType': 'MANUAL',
        'class': 'org.openqa.selenium.Proxy',
        'autodetect': False
    }
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.minimize_window()
    driver.get(url)
    time.sleep(4)
    driver.close()
